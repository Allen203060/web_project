document.addEventListener('DOMContentLoaded', function() {
    fetchBooks();
});

async function fetchBooks() {
    const response = await fetch('books.json');
    const books = await response.json();
    displayBooks(books);
}

function displayBooks(books) {
    const bookList = document.getElementById('book-list');
    bookList.innerHTML = '';

    books.forEach(book => {
        const bookElement = document.createElement('a');
        bookElement.href = `book-template.html?title=${book.title}`
        bookElement.classList.add('figs');
        bookElement.innerHTML = `
            <figure>
                <div class="mrp">MRP - ${book.price}</div>
                <img src="${book.image}" alt="${book.title}">
                <figcaption>${book.title} - ${book.author}</figcaption>
            </figure>
            <div class="button-container">
                <button class="btn add-to-cart">Add to Cart</button>
                <button class="btn buy-now">Buy Now</button>
            </div>
            <section class="book-summary">
                <h3>Book Summary</h3>
                <p>${book.summary}</p>
            </section>
            <div class="feedb">
                <button class="btn open-popup" onclick="openPopup()">Feedback Form</button>
                <div id="reviewsContainer"></div>
                <div class="button-container btns">
                    <button class="btn prev-review">Previous</button>
                    <button class="btn next-review">Next</button>
                </div>
            </div>
        `;
        bookList.appendChild(bookElement);
    });
}

function showBookDetails(title) {
    fetch('books.json')
        .then(response => response.json())
        .then(books => {
            const book = books.find(b => b.title === title);
            if (book) {
                const bookDetails = `
                    <h2>${book.title}</h2>
                    <p>By ${book.author}</p>
                    <p>Price: ${book.price}</p>
                    <img src="${book.image}" alt="${book.title}">
                    <p>${book.summary}</p>
                    <a href="${book.pdf}" target="_blank">Read Now</a>
                `;
                document.getElementById('book-details').innerHTML = bookDetails;
                document.getElementById('popupForm').style.display = 'block';
            } else {
                document.getElementById('book-details').innerHTML = '<p>Book not found.</p>';
            }
        })
        .catch(error => {
            console.error('Error fetching book details:', error);
            document.getElementById('book-details').innerHTML = '<p>Error loading book details. Please try again later.</p>';
        });
}

function closePopup() {
    document.getElementById('popupForm').style.display = 'none';
}
