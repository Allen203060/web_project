class FlipBook {
    constructor(options) {
        this.container = options.container;
        this.pdf = options.pdf;
        this.init();
    }
    async init() {
        // Create an iframe to embed the PDF viewer
        const iframe = document.createElement('iframe');
        iframe.src = `https://flipbookpdf.net/viewer.html?file=${encodeURIComponent(this.pdf)}`;
        iframe.style.width = '100%';
        iframe.style.height = '100%';
        iframe.style.border = 'none';
        this.container.appendChild(iframe);
    }
}
// Example usage of the FlipBook class
document.addEventListener('DOMContentLoaded', function() {
    const flipbookContainer = document.querySelector('.flip-book-container');
    if (flipbookContainer) {
        const pdfSrc = flipbookContainer.getAttribute('src');
        new FlipBook({
            container: flipbookContainer,
            pdf: pdfSrc
        });
    }
});