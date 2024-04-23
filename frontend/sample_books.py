from frontend.book import Book


sample_books_json = [
    {
        "title": "To Kill a Mockingbird1",
        "author": "Harper Lee",
        "rating": 4.5,
        "genre": "fiction",
        "cover_image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlP-hjqtPh4uELBSTIuSremu9HZTVju0_H4o25tr2yRg&s",
        "description": "To Kill a Mockingbird is a novel by the American author Harper Lee. It was published in June 1960 and became instantly successful. In the United States, it is widely read in high schools and middle schools. To Kill a Mockingbird has become a classic of modern American literature; a year after its release, it won the Pulitzer Prize. The plot and characters are loosely based on Lee's observations of her family, her neighbors and an event that occurred near her hometown of Monroeville, Alabama, in 1936, when she was ten."
    },
    {
        "title": "To Kill a Mockingbird2",
        "author": "Harper Lee",
        "rating": 4,
        "genre": "science",
        "cover_image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlP-hjqtPh4uELBSTIuSremu9HZTVju0_H4o25tr2yRg&s",
    },
    {
        "title": "To Kill a Mockingbird3",
        "author": "Harper Lee",
        "rating": 3.5,
        "genre": "fiction",
        "cover_image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlP-hjqtPh4uELBSTIuSremu9HZTVju0_H4o25tr2yRg&s",
    },
    {
        "title": "To Kill a Mockingbird4",
        "author": "Harper Lee",
        "rating": 3,
        "genre": "fiction",
        "cover_image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlP-hjqtPh4uELBSTIuSremu9HZTVju0_H4o25tr2yRg&s",
    },
    {
        "title": "To Kill a Mockingbird5",
        "author": "Harper Lee",
        "rating": 2.5,
        "genre": "fiction",
        "cover_image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlP-hjqtPh4uELBSTIuSremu9HZTVju0_H4o25tr2yRg&s",
    },
    {
        "title": "To Kill a Mockingbird6",
        "author": "Harper Lee",
        "rating": 2,
        "genre": "fiction",
        "cover_image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlP-hjqtPh4uELBSTIuSremu9HZTVju0_H4o25tr2yRg&s",
    },
    {
        "title": "To Kill a Mockingbird7",
        "author": "Harper Lee",
        "rating": 1.5,
        "genre": "fiction",
        "cover_image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlP-hjqtPh4uELBSTIuSremu9HZTVju0_H4o25tr2yRg&s",
    },
    {
        "title": "To Kill a Mockingbird8",
        "author": "Harper Lee",
        "rating": 1.5,
        "genre": "fiction",
        "cover_image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlP-hjqtPh4uELBSTIuSremu9HZTVju0_H4o25tr2yRg&s",
    },
    {
        "title": "To Kill a Mockingbird9",
        "author": "Harper Lee",
        "rating": 4.5,
        "genre": "fiction",
        "cover_image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlP-hjqtPh4uELBSTIuSremu9HZTVju0_H4o25tr2yRg&s",
    },
    {
        "title": "To Kill a Mockingbird10",
        "author": "Harper Lee",
        "rating": 4.5,
        "genre": "fiction",
        "cover_image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlP-hjqtPh4uELBSTIuSremu9HZTVju0_H4o25tr2yRg&s",
    },
]

books = [Book(**book_json) for book_json in sample_books_json]

selected_book= books[0]