from fastapi import FastAPI, Depends, HTTPException, Security
from sqlalchemy.orm import Session
from fastapi.security.api_key import APIKeyHeader
import app.database.models as models
import app.database.database as database
import jwt
from app.service.books import Books
import httpx
from fastapi import Request
from fastapi.responses import JSONResponse
from typing import List, Optional
import uvicorn


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


def start():
    print("Starting service...")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    start()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Auth details
API_KEY_NAME = "Authorization"

api_key_header_auth = APIKeyHeader(name=API_KEY_NAME, auto_error=True)


@app.exception_handler(httpx.HTTPStatusError)
async def general_exception_handler(request: Request, exc: httpx.HTTPStatusError):
    return JSONResponse(
        status_code=exc.response.status_code,
        content={"message": "An error occurred", "details": str(exc)},
    )


async def validate_jwt(api_key_header_auth: str = Security(api_key_header_auth)):
    try:
        # Validate JWT
        payload = jwt.decode(api_key_header_auth, options={"verify_signature": False})

        # Get user name from JWT payload
        username = payload.get("email")
        if username is None:
            raise HTTPException(
                status_code=400, detail="Invalid JWT: No username provided in payload"
            )

        return username

    except (jwt.PyJWTError, ValueError):
        raise HTTPException(
            status_code=400,
            detail="Invalid JWT"
        ) from None


@app.post("/user")
def get_or_create_user(
    db: Session = Depends(get_db), username: str = Depends(validate_jwt)
):
    # Check if user exists
    db_user = db.query(models.User).filter(models.User.name == username).first()

    # If user does not exist, create them
    if not db_user:
        db_user = models.User(name=username)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

    # Return user info
    return {"username": db_user.name, "created_at": db_user.created_at}


@app.get("/search_books")
async def search_books(
    name: Optional[str] = None,
    author: Optional[str] = None,
    tags: List[str] = None,
    page: int = 1,
    size: int = 1,
):
    result = await Books.search_books(
        name=name, author=author, tags=tags, page=page, size=size
    )
    return result


@app.get("/book/{book_id}")
async def get_book_by_id(book_id: str):
    book = await Books.get_book_by_id(id=book_id)
    return book


@app.post("/user/{username}/books")
async def choose_favorites(
    username: str, books: List[str], db: Session = Depends(get_db)
):
    db_user = db.query(models.User).filter(models.User.name == username).first()

    if len(books) == 0 or not db_user:
        raise HTTPException(status_code=400, detail="Invalid input data")

    unique_books = list(set(books))

    for book in unique_books:
        await Books.get_book_by_id(book)

    try:
        for book_id in unique_books:
            # Check if the book already exists in favorites
            existing_book = (
                db.query(models.FavoriteBook)
                .filter(
                    models.FavoriteBook.user_id == db_user.id,
                    models.FavoriteBook.book_id == book_id,
                )
                .first()
            )
            if not existing_book:
                new_favorite = models.FavoriteBook(user_id=db_user.id, book_id=book_id)
                db.add(new_favorite)

        db.commit()
        return {"message": "Favorites updated successfully"}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/user/{username}/books/{book_id}")
async def delete_favorites(username: str, book_id: str, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.name == username).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid input data")
    favorite_book = (
        db.query(models.FavoriteBook)
        .filter(
            models.FavoriteBook.user_id == db_user.id,
            models.FavoriteBook.book_id == book_id,
        )
        .first()
    )
    if not favorite_book:
        raise HTTPException(status_code=404, detail="Favorite book not found")

    try:
        # Delete the favorite book entry
        db.delete(favorite_book)
        db.commit()
        return {"message": "Favorite book deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/user/{username}/books")
async def get_favorites(username: str, brief: bool, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.name == username).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="No such user")

    books = [favorite_book.book_id for favorite_book in db_user.favorite_books]
    if brief:
        return books

    return [await Books.get_book_by_id(book) for book in books]


@app.get("/user/{username}/books/recommendation")
async def get_recommendation(username: str, db: Session = Depends(get_db)):
    return


@app.get("/check")
async def check_function(book_id: str):
    book = await Books.get_recommendation(book_id)
    return book
