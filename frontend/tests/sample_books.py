from app.models.book import Book

img_url = "https://encrypted-tbn0.gstatic.com/\
    images?q=tbn:ANd9GcSlP-hjqtPh4uELBSTIuSremu9HZTVju0_H4o25tr2yRg&s"

sample_books_json = [
    {
        "id": "id1",
        "title": "To Kill a Mockingbird1",
        "author": "Harper Lee",
        "rating": 4.5,
        "genre": "fiction",
        "cover_link": img_url,
        "description": """To Kill a Mockingbird is a novel by the American \
            author Harper Lee. It was published in June 1960 and became \
            instantly successful. In the United States, it is widely \
            read in high schools and middle schools. To Kill a \
            Mockingbird has become a classic of modern American \
            literature; a year after its release, \
            it won the Pulitzer Prize. The plot and \
            characters are loosely based on \
            Lee's observations of her family, her neighbors and \
            an event that occurred near \
            her hometown of Monroeville, Alabama, in 1936, \
            when she was ten.""",
    },
    {
        "id": "id2",
        "title": "To Kill a Mockingbird2",
        "author": "Harper Lee",
        "rating": 4,
        "genre": "science",
        "cover_link": img_url,
    },
]

books = [Book(**book_json) for book_json in sample_books_json]

selected_book = books[0]
