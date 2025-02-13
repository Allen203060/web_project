// Toggle like button
function toggleLike(icon) {
    icon.classList.toggle('liked');
    if (icon.classList.contains('liked')) {
        icon.style.color = '#ff5757';
    } else {
        icon.style.color = '#333';
    }
}

// Toggle save button
function toggleSave(icon) {
    icon.classList.toggle('saved');
    if (icon.classList.contains('saved')) {
        icon.style.color = '#ff5757';
    } else {
        icon.style.color = '#333';
    }
}

// Toggle comments section
function openStory(imageSrc, songSrc) {
    // Create the story modal
    const storyModal = document.createElement("div");
    storyModal.classList.add("story-modal");
    storyModal.innerHTML = `
        <div class="story-content">
            <button class="close-story" onclick="closeStory()">&#10094; Back</button>
            <img src="${imageSrc}" alt="Story Image">
            <audio autoplay>
                <source src="${songSrc}" type="audio/mpeg">
            </audio>
        </div>
    `;

    document.body.appendChild(storyModal);

    // Auto-close story after 15 seconds
    setTimeout(() => {
        closeStory();
    }, 15000);
}

// Function to close the story modal
function closeStory() {
    const storyModal = document.querySelector(".story-modal");
    if (storyModal) {
        storyModal.remove();
    }
}
