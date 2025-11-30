// Countdown Timer
function updateCountdown() {
    // Get wedding date from data attribute or use default
    const weddingDateStr = document.body.getAttribute('data-wedding-date') || '2024-06-15';
    const weddingDate = new Date(weddingDateStr).getTime();
    const now = new Date().getTime();
    const distance = weddingDate - now;

    if (distance < 0) {
        // Wedding has passed
        document.getElementById('days').textContent = '0';
        document.getElementById('hours').textContent = '0';
        document.getElementById('minutes').textContent = '0';
        document.getElementById('seconds').textContent = '0';
        return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById('days').textContent = days;
    document.getElementById('hours').textContent = hours.toString().padStart(2, '0');
    document.getElementById('minutes').textContent = minutes.toString().padStart(2, '0');
    document.getElementById('seconds').textContent = seconds.toString().padStart(2, '0');
}

// Update countdown every second
updateCountdown();
setInterval(updateCountdown, 1000);

