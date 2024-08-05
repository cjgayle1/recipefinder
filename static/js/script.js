// document.addEventListener("DOMContentLoaded", function() {
//     var modal = document.getElementById("recipeModal");
//     var span = document.getElementsByClassName("close")[0];

//     // Updated to accept an element and use data-title
//     window.openRecipeCard = function(element) {
//         var title = JSON.parse(element.getAttribute('data-title'));
//         document.getElementById("modalBody").innerHTML = "Details for " + title;
//         modal.style.display = "block";
//     }

//     span.onclick = function() { modal.style.display = "none"; }
//     window.onclick = function(event) { if (event.target == modal) { modal.style.display = "none"; } }
// });

// document.addEventListener("DOMContentLoaded", function() {
//     const modal = document.getElementById("recipeModal");
//     const span = document.getElementsByClassName("close")[0];
//     const themeToggle = document.getElementById("theme-toggle");

//     window.openRecipeCard = function(element) {
//         const title = JSON.parse(element.getAttribute('data-title'));
//         document.getElementById("modalBody").innerHTML = "Details for " + title; // Enhance this as needed
//         modal.style.display = "block";
//     }

//     span.onclick = function() { modal.style.display = "none"; }
//     window.onclick = function(event) { if (event.target == modal) { modal.style.display = "none"; } }

//     // Theme toggle functionality
//     themeToggle.addEventListener('click', function() {
//         document.body.classList.toggle('dark-theme');
//         const newSrc = document.body.classList.contains('dark-theme') ? "{{ url_for('static', filename='images/moon-icon.png') }}" : "{{ url_for('static', filename='images/sun-icon.png') }}";
//         themeToggle.setAttribute('src', newSrc);
//     });
// });

// document.addEventListener("DOMContentLoaded", function() {
//     const modal = document.getElementById("recipeModal");
//     const span = document.getElementsByClassName("close")[0];

//     // Open recipe details in a modal
//     window.openRecipeCard = function(element) {
//         const title = JSON.parse(element.getAttribute('data-title'));
//         document.getElementById("modalBody").innerHTML = "Details for " + title; // Consider enhancing this to include more details
//         modal.style.display = "block";
//     }

//     // Close the modal when the close button is clicked
//     span.onclick = function() { modal.style.display = "none"; }

//     // Close the modal when clicking outside of it
//     window.onclick = function(event) { if (event.target == modal) { modal.style.display = "none"; } }

//     // Theme switcher logic
//     const themeSlider = document.getElementById('theme-slider');
//     themeSlider.addEventListener('change', () => {
//         document.body.classList.toggle('dark-theme');
//         // Save the theme preference
//         localStorage.setItem('theme', document.body.classList.contains('dark-theme') ? 'dark' : 'light');
//     });

//     // Load and apply saved theme preference
//     if(localStorage.getItem('theme') === 'dark') {
//         document.body.classList.add('dark-theme');
//         themeSlider.checked = true;
//     }
// });



document.addEventListener("DOMContentLoaded", function() {
    const modal = document.getElementById("recipeModal");
    const closeSpan = document.getElementsByClassName("close")[0];
    const themeSlider = document.getElementById('theme-slider');

    // Function to open the modal with recipe details
    // window.openRecipeCard = function(element) {
    //     console.log("openRecipeCard called", element);
    //     // Retrieve the recipe title stored in the data-title attribute
    //     const title = (element.getAttribute('data-title'));
    //     const instructions = element.getAttribute('data-instructions');
    //     // Populate the modal's body with details; consider fetching more details if necessary
    //     document.getElementById("modalBody").innerHTML = "Details for " + title + "Instructions:" + instructions;


    //     // Display the modal
    //     modal.style.display = "block";
    // };

    window.openRecipeCard = function(element) {
        const title = element.getAttribute('data-title');
        const imageName = element.getAttribute('data-image-name');
        const imagePath = "https://recipe-images-ai-generator.s3.us-east-2.amazonaws.com/" + (imageName ? imageName + '.jpg' : 'default_image.jpg');
        const ingredientsJson = element.getAttribute('data-ingredients');
        const instructions = element.getAttribute('data-instructions');
    
        // const ingredients = JSON.parse(ingredientsJson || '[]');
    
        let contentHtml = `<h2>${title}</h2><img src="${imagePath}" alt="${title}" style="width:55%">`;
        contentHtml += `<h3>Ingredients</h3><p>${ingredientsJson}</p><ul>`;
        // ingredients.forEach(ing => {
        //     contentHtml += `<li>${ing}</li>`;
        //     // console.log(ing);
        // });
        contentHtml += `</ul>`;
        contentHtml += `<h3>Instructions</h3><p>${instructions}</p>`;
    
        document.getElementById("modalBody").innerHTML = contentHtml;
        modal.style.display = "block";
    };
    
    function closeModal() {
        const modal = document.getElementById("recipeModal");
        modal.style.display = "none";
    }
    
    
    
    // Close the modal when the close (X) button is clicked
    closeSpan.onclick = function() {
        modal.style.display = "none";
    };

    // Close the modal if the user clicks outside of it
    window.onclick = function(event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    };

    // Listen for changes on the theme slider (checkbox) to toggle the theme
    themeSlider.addEventListener('change', function() {
        console.log("themeSlider called", element);
        alert("theme slider");
        // Toggle the 'dark-theme' class on the body
        document.body.classList.toggle('dark-theme');
        // Save the current theme preference to localStorage
        localStorage.setItem('theme', document.body.classList.contains('dark-theme') ? 'dark-theme' : 'light-theme');
    });

    // Check localStorage for a saved theme preference and apply it on page load
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        document.body.className = savedTheme; // Apply the saved theme
        themeSlider.checked = savedTheme === 'dark-theme'; // Adjust the slider position based on the saved theme
    }
});
