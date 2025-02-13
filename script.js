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
        customScrollContentBy(scrollContentContainer, -350, 550); // Adjust the duration for speed
    });

    document.querySelector('.scroll-container .scroll-btn.right').addEventListener('click', () => {
        customScrollContentBy(scrollContentContainer, 350, 550); // Adjust the duration for speed
    });
}

if (scrollContainer1) {
    function customScrollContainerBy(element, amount, duration) {
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

    document.querySelector('.scroll-container1 .scroll-btn.left').addEventListener('click', () => {
        customScrollContainerBy(scrollContainer1, -window.innerWidth, 550); // Adjust the duration for speed
    });

    document.querySelector('.scroll-container1 .scroll-btn.right').addEventListener('click', () => {
        customScrollContainerBy(scrollContainer1, window.innerWidth, 550); // Adjust the duration for speed
    });
}
