
document.querySelectorAll('.animated-count').forEach((countElement) => {
    let countTo = parseInt(countElement.textContent, 10);
    let count = 0;
    let increment = Math.ceil(countTo / 100); // Adjust increment for smoother/faster count up

    function updateCount() {
        if (count < countTo) {
            count += increment;
            countElement.textContent = count;
            setTimeout(updateCount, 20); // Adjust speed of counting
        } else {
            countElement.textContent = countTo; // Ensure final value is set correctly
        }
    }

    updateCount();
});
