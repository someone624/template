document.addEventListener("DOMContentLoaded", function() {
    // Example function to display a welcome message on page load
    const userName = document.querySelector("h1");
    if (userName) {
        userName.textContent = "Welcome, user!"; // Modify if needed
    }
    
    // Add any other JS functionalities as needed
    console.log("App Loaded");
});
