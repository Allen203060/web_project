document.getElementById('reviewForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('aname').value;
    const email = document.getElementById('mail').value;
    const review = document.getElementById('review').value;
    const rating = document.getElementById('rating').value;
    const reviewElement = document.createElement('div');
    reviewElement.className = 'review';
    reviewElement.innerHTML = `
        <p class="rating">Rating: ${'★'.repeat(rating)}${'☆'.repeat(5 - rating)}</p>
        <p class="review-content">"${review}"</p>
    `;
    const reviews = document.getElementById('reviews');
    reviews.appendChild(reviewElement);
    updatePagination();
});
let currentPage = 1;
const reviewsPerPage = 3;
function updatePagination() {
    const reviews = document.querySelectorAll('#reviews .review');
    const totalPages = Math.ceil(reviews.length / reviewsPerPage);
    document.getElementById('prevPage').disabled = currentPage === 1;
    document.getElementById('nextPage').disabled = currentPage === totalPages;
    reviews.forEach((review, index) => {
        review.style.display = 'none';
        if (index >= (currentPage - 1) * reviewsPerPage && index < currentPage * reviewsPerPage) {
            review.style.display = 'block';
        }
    });
}
document.getElementById('prevPage').addEventListener('click', () => {
    if (currentPage > 1) {
        currentPage--;
        updatePagination();
    }
});
document.getElementById('nextPage').addEventListener('click', () => {
    const reviews = document.querySelectorAll('#reviews .review');
    if (currentPage < Math.ceil(reviews.length / reviewsPerPage)) {
        currentPage++;
        updatePagination();
    }
}); 
updatePagination();