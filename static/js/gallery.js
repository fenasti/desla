document.addEventListener("DOMContentLoaded", function () {
    const filterLinks = document.querySelectorAll(".filter-nav");
    const galleryItems = document.querySelectorAll(".gallery-item");

    filterLinks.forEach(link => {
        link.addEventListener("click", function (event) {
            event.preventDefault(); // Prevent page reload

            const category = this.getAttribute("data-category");

            galleryItems.forEach(item => {
                if (category === "all" || item.getAttribute("data-category") === category) {
                    item.style.display = "block"; // Show matching items
                } else {
                    item.style.display = "none"; // Hide non-matching items
                }
            });
        });
    });
});