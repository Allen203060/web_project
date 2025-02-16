const items = [
    { name: 'Captain America: Brave New World', image: 'https://cdn.kinocheck.com/i/w=1200/dgyqcoda86.jpg' },
    { name: 'Presence', image: 'https://th.bing.com/th/id/OIP.rrmbJq6isvQg5aI5dg4ZgQHaEK?rs=1&pid=ImgDetMain' },
    { name: 'The Gorge', image: 'https://th.bing.com/th/id/OIP.PiDROO-dhQgm49RnPyYN9gHaD4?rs=1&pid=ImgDetMain' },
    { name: 'Bridget Jones: Mad About the Boy', image: 'https://static1.moviewebimages.com/wordpress/wp-content/uploads/2024/11/bridget-jones-mad-about-the-boy-movie-poster-with-renee-zelweger.jpg' },
    { name: 'Conclave', image: 'https://th.bing.com/th/id/OIP.Q_of37Jm5nzihqhcj_OAVAHaEa?rs=1&pid=ImgDetMain' }
];

function populateList() {
    const itemList = document.getElementById('itemList');
    items.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item.name;
        itemList.appendChild(li);
    });
}

function search() {
    const input = document.getElementById('searchInput').value.toLowerCase();
    const searchResults = document.getElementById('searchResults');

    if (input.length > 0) {
        searchResults.style.display = 'block';
        searchResults.innerHTML = '';

        items.forEach(item => {
            if (item.name.toLowerCase().includes(input)) {
                const resultItem = document.createElement('div');
                resultItem.classList.add('result-item');

                const img = document.createElement('img');
                img.src = item.image;
                img.alt = item.name;

                const name = document.createElement('p');
                name.textContent = item.name;

                resultItem.appendChild(img);
                resultItem.appendChild(name);
                searchResults.appendChild(resultItem);
            }
        });
    } else {
        searchResults.style.display = 'none';
    }
}

// Populate the list when the page loads
window.onload = populateList;

// Add event listener to the search input field
document.getElementById('searchInput').addEventListener('input', search);