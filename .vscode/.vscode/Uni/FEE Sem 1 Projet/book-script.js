document.addEventListener('DOMContentLoaded', function() {
    const params = new URLSearchParams(window.location.search);
    const bookTitle = params.get('title');

    if (bookTitle) {
        fetchBookDetails(bookTitle);
    }
});

async function fetchBookDetails(title) {
    const response = await fetch('books.json');
    const books = await response.json();
    const book = books.find(b => b.title === title);

    if (book) {
        document.getElementById('book-title').textContent = book.title;
        document.getElementById('book-heading').textContent = book.title;
        document.getElementById('book-price').textContent = `MRP - ${book.price}`;
        document.getElementById('book-image').src = book.image;
        document.getElementById('book-caption').textContent = `${book.title} - ${book.author}`;
        document.getElementById('book-summary').textContent = book.summary;
    } else {
        document.getElementById('book-heading').textContent = 'Book Not Found';
        document.getElementById('book-summary').textContent = 'The book you are looking for does not exist.';
    }
}