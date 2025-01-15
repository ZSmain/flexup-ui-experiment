document.addEventListener('DOMContentLoaded', function () {
    const sidebarToggle = document.getElementById('sidebarToggle');
    const sidebarToggleDesktop = document.getElementById('sidebarToggleDesktop');
    const sidebar = document.getElementById('sidebar');
    let isCollapsed = window.innerWidth < 768;

    function updateSidebarState() {
        if (window.innerWidth < 768) {
            sidebar.style.width = isCollapsed ? '0rem' : '16rem'
        }

    }
    updateSidebarState();

    function toggleSidebar() {
        isCollapsed = !isCollapsed;
        updateSidebarState();
        if (window.innerWidth >= 768) {
            sidebar.style.width = isCollapsed ? '4rem' : '16rem';
        }
    }

    sidebarToggle?.addEventListener('click', toggleSidebar);
    sidebarToggleDesktop?.addEventListener('click', toggleSidebar);

    window.addEventListener('resize', function () {
        isCollapsed = window.innerWidth < 768;
        updateSidebarState();
        if (window.innerWidth >= 768) {
            sidebar.style.width = isCollapsed ? '4rem' : '16rem'
        }
    });
});