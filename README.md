# The Book Review Platform

## Project Description:
BRP is a dynamic online platform designed to foster a vibrant community of book lovers, where they can share their thoughts, discover new reads, and engage in meaningful discussions. With a user-friendly  interface and  seamless  integration  of  external  APIs, BRP offers  an  immersive experience for bibliophiles.

### Here are the key features:
1. Book Reviews and Ratings: Users can write and publish detailed reviews for their favorite books. Whether it’s a classic novel, a thrilling mystery, or a thought-provoking non-fiction work, BRP provides a space to express opinions and insights. Readers can rate books on a scale of 1 to 5 stars, allowing others to gauge the overall quality and popularity of a title.
2. Book Details and Recommendations: Leveraging an external API, BRP fetches comprehensive information about books, including author details, publication dates, genres, and cover images. The  platform  suggests  personalized  book  recommendations  based  on  users’ reading history, preferences, and trending titles.

## Running backend:

- Go to `backend` directory
- `poetry install`
- `poetry run start`

## Running frontend:

- Go to `frontend` directory
- `poetry install`
- `poetry run streamlit run app/main.py`

## Running tests

### Backend

```bash
poetry run pytest . --cov=app
```

### Frontend

```bash
cd frontend
poetry run pytest . --cov=app
```