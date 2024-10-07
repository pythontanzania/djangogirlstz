// Function to animate the counting of numbers
function animateCount() {
    const counters = document.querySelectorAll('.counter');

    counters.forEach(counter => {
        const target = +counter.getAttribute('data-target'); // Get the target value from the 'data-target' attribute
        const speed = 200; // Adjust this value to control how fast the numbers count up
        
        const updateCount = () => {
            const current = +counter.innerText.replace('+', ''); // Get the current number
            
            const increment = target / speed; // Calculate the increment based on the target
            
            if (current < target) {
                counter.innerText = Math.ceil(current + increment) + " +";
                setTimeout(updateCount, 30); // Call the update function every 30ms
            } else {
                counter.innerText = target + " +"; // Ensure the final number is displayed correctly
            }
        };

        updateCount();
    });
}

// Start the counting animation when the page loads
document.addEventListener('DOMContentLoaded', animateCount);
