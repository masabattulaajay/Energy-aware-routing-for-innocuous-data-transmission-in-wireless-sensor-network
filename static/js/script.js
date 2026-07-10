// -----------------------------
// Project Loaded
// -----------------------------
document.addEventListener("DOMContentLoaded", function () {
    console.log("Energy-Aware WSN Project Loaded");
});


// -----------------------------
// Login Validation
// -----------------------------
function validateLogin() {

    let username = document.getElementsByName("username")[0].value;
    let password = document.getElementsByName("password")[0].value;

    if (username === "" || password === "") {
        alert("Please enter Username and Password");
        return false;
    }

    return true;
}


// -----------------------------
// Network Validation
// -----------------------------
function validateNodes() {

    let nodes = document.getElementsByName("nodes")[0].value;

    if (nodes < 5 || nodes > 100) {
        alert("Number of nodes should be between 5 and 100.");
        return false;
    }

    return true;
}


// -----------------------------
// Transmission Validation
// -----------------------------
function validateMessage() {

    let message = document.getElementsByName("message")[0].value;

    if (message.trim() === "") {
        alert("Please enter sensor data.");
        return false;
    }

    return true;
}


// -----------------------------
// Confirmation Before Logout
// -----------------------------
function confirmLogout() {

    return confirm("Are you sure you want to logout?");
}