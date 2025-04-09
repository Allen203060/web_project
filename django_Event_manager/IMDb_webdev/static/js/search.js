const items = ['Apple', 'Banana', 'Cherry', 'Date', 'Fig', 'Grape'];

function populateList() {
    const itemList = document.getElementById('itemList');
    items.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item;
        itemList.appendChild(li);
    });
}

function search() {
    var query = document.getElementById('searchInput').value.toLowerCase();
    var listItems = document.querySelectorAll('#itemList li');

    listItems.forEach(function(item) {
        if (item.textContent.toLowerCase().includes(query)) {
            item.style.display = '';
        } else {
            item.style.display = 'none';
        }
    });
}

// Populate the list when the page loads
window.onload = populateList;
m