const scrollContentContainer = document.querySelector('.scroll-content');
const scrollContainer1 = document.querySelector('.scroll-container1');
const scrollContainer3 = document.querySelector('.scroll-container3'); // Select the third scroll container

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

    // Auto transition
    setInterval(nextImage, 5000); // Change image every 5 seconds
}

document.addEventListener('DOMContentLoaded', function() {
    const container1 = document.querySelector('.scroll-container1');
    const movies1 = container1.querySelectorAll('.movie');
    let currentIndex1 = 0;

    function showMovie1(index) {
        movies1.forEach((movie, i) => {
            if (i === index) {
                movie.style.display = 'block';
                movie.style.margin = '0 auto'; // Center align the image
            } else {
                movie.style.display = 'none';
            }
        });
        container1.scrollTo({
            left: container1.clientWidth * index,
            behavior: 'smooth'
        });
    }

    function nextMovie1() {
        currentIndex1 = (currentIndex1 + 1) % movies1.length;
        showMovie1(currentIndex1);
    }

    function prevMovie1() {
        currentIndex1 = (currentIndex1 - 1 + movies1.length) % movies1.length;
        showMovie1(currentIndex1);
    }

    // Add event listeners for next and previous buttons if they exist
    document.querySelector('.scroll-container1 .scroll-btn.right').addEventListener('click', nextMovie1);
    document.querySelector('.scroll-container1 .scroll-btn.left').addEventListener('click', prevMovie1);

    // Initially show the first movie
    showMovie1(currentIndex1);

    // Auto transition
    setInterval(nextMovie1, 5000); // Change movie every 5 seconds
});

document.addEventListener('DOMContentLoaded', function() {
    const container3 = document.querySelector('.scroll-container3');
    const movies3 = container3.querySelectorAll('.movie');
    let currentIndex3 = 0;

    function showMovie3(index) {
        movies3.forEach((movie, i) => {
            if (i === index) {
                movie.style.display = 'block';
                movie.style.margin = '0 auto'; // Center align the image
            } else {
                movie.style.display = 'none';
            }
        });
        container3.scrollTo({
            left: container3.clientWidth * index,
            behavior: 'smooth'
        });
    }

    function nextMovie3() {
        currentIndex3 = (currentIndex3 + 1) % movies3.length;
        showMovie3(currentIndex3);
    }

    function prevMovie3() {
        currentIndex3 = (currentIndex3 - 1 + movies3.length) % movies3.length;
        showMovie3(currentIndex3);
    }

    // Add event listeners for next and previous buttons if they exist
    document.querySelector('.scroll-container3 .scroll-btn.right').addEventListener('click', nextMovie3);
    document.querySelector('.scroll-container3 .scroll-btn.left').addEventListener('click', prevMovie3);

    // Initially show the first movie
    showMovie3(currentIndex3);

    // Auto transition
    setInterval(nextMovie3, 5000); // Change movie every 5 seconds
});

if (scrollContainer3) {
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

    document.querySelector('.scroll-container3 .scroll-btn.left').addEventListener('click', () => {
        customScrollContentBy(scrollContainer3, -350, 500); // Adjust the duration for faster speed
    });

    document.querySelector('.scroll-container3 .scroll-btn.right').addEventListener('click', () => {
        customScrollContentBy(scrollContainer3, 350, 500); // Adjust the duration for faster speed
    });
}