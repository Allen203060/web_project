const scrollContentContainer = document.querySelector('.scroll-content');
const scrollContainer1 = document.querySelector('.scroll-container1');

if (scrollContentContainer) {
    function customScrollContentBy(element, amount, duration) {
        const start = element.scrollLeft;
        const startTime = performance.now();

        function scrollStep(timestamp) {
            const progress = timestamp - startTime;
            const percent = Math.min(progress / duration, 1);
            element.scrollLeft = start + amount * percent;
            if (percent < 1) {
                requestAnimationFrame(scrollStep);
            }
        }

        requestAnimationFrame(scrollStep);
    }

    document.querySelector('.scroll-container .scroll-btn.left').addEventListener('click', () => {
        customScrollContentBy(scrollContentContainer, -350, 500); // Adjust the duration for faster speed
    });

    document.querySelector('.scroll-container .scroll-btn.right').addEventListener('click', () => {
        customScrollContentBy(scrollContentContainer, 350, 500); // Adjust the duration for faster speed
    });
}

if (scrollContainer1) {
    let currentImageIndex = 0;
    const movies = document.querySelectorAll('.scroll-container1 .movie');

    function showImage(index) {
        movies.forEach((movie, i) => {
            movie.classList.remove('active');
            if (i === index) {
                movie.classList.add('active');
            }
        });
    }

    function nextImage() {
        currentImageIndex = (currentImageIndex + 1) % movies.length;
        showImage(currentImageIndex);
    }

    function previousImage() {
        currentImageIndex = (currentImageIndex - 1 + movies.length) % movies.length;
        showImage(currentImageIndex);
    }

    document.querySelector('.scroll-container1 .scroll-btn.left').addEventListener('click', previousImage);
    document.querySelector('.scroll-container1 .scroll-btn.right').addEventListener('click', nextImage);
}

document.addEventListener('DOMContentLoaded', function() {
    const container = document.querySelector('.scroll-container1');
    const movies = container.querySelectorAll('.movie');
    let currentIndex = 0;

    function showMovie(index) {
        movies.forEach((movie, i) => {
            if (i === index) {
                movie.style.display = 'block';
                movie.style.margin = '0 auto'; // Center align the image
            } else {
                movie.style.display = 'none';
            }
        });
        container.scrollTo({
            left: container.clientWidth * index,
            behavior: 'smooth'
        });
    }

    function nextMovie() {
        currentIndex = (currentIndex + 1) % movies.length;
        showMovie(currentIndex);
    }

    function prevMovie() {
        currentIndex = (currentIndex - 1 + movies.length) % movies.length;
        showMovie(currentIndex);
    }

    // Add event listeners for next and previous buttons if they exist
    document.querySelector('.scroll-btn.right').addEventListener('click', nextMovie);
    document.querySelector('.scroll-btn.left').addEventListener('click', prevMovie);

    // Initially show the first movie
    showMovie(currentIndex);
});
