// script.js
document.addEventListener('DOMContentLoaded', () => {
    const cursor = document.getElementById('cursor');
    document.addEventListener('mousemove', (event) => {
        cursor.style.left = `${event.pageX}px`;
        cursor.style.top = `${event.pageY}px`;
    });
});
