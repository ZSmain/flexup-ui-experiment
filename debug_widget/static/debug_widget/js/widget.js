function toggleDebugWidget() {
    const widget = document.getElementById('debug-widget');
    widget.classList.toggle('active');

    // Save state in localStorage
    localStorage.setItem('debugWidgetOpen', widget.classList.contains('active'));
}

document.addEventListener('DOMContentLoaded', function () {
    const widget = document.getElementById('debug-widget');
    const isOpen = localStorage.getItem('debugWidgetOpen') === 'true';

    if (isOpen) {
        widget.classList.add('active');
    }

    // Add collapse event handlers
    document.querySelectorAll('.debug-section-header').forEach(header => {
        header.addEventListener('click', function () {
            const icon = this.querySelector('i');
            const isExpanded = this.getAttribute('aria-expanded') === 'true';

            if (isExpanded) {
                icon.style.transform = 'rotate(0deg)';
            } else {
                icon.style.transform = 'rotate(90deg)';
            }
        });
    });
});