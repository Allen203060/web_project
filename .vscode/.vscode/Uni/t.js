// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
// Check if the element is in the viewport
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}
// Add 'visible' class to elements in the viewport
function checkElements() {
    const elements = document.querySelectorAll('.fade-in');
    elements.forEach(element => {
        if (isInViewport(element)) {
            element.classList.add('visible');
        }
    });
}
// Listen for scroll and resize events
window.addEventListener('scroll', checkElements);
window.addEventListener('resize', checkElements);
// Check elements on initial load
checkElements();
// Dark mode toggle functionality
const toggleButton = document.getElementById('dark-mode-toggle');
const body = document.body;
toggleButton.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
});
// Modal functionality
const modal = document.getElementById('contact-modal');
const btn = document.querySelector('.button button');
const span = document.querySelector('.close');
btn.onclick = function() {
    modal.style.display = "block";
}
span.onclick = function() {
    modal.style.display = "none";
}
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}