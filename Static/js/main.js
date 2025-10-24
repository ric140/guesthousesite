document.addEventListener('DOMContentLoaded', function () {
    
    // --- Mobile Menu Logic ---
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenuCloseButton = document.getElementById('mobile-menu-close-button');
    const mobileMenuPanel = document.getElementById('mobile-menu-panel');

    if (mobileMenu && mobileMenuButton && mobileMenuCloseButton && mobileMenuPanel) {
        const openMenu = () => {
            mobileMenu.classList.remove('hidden');
            // A tiny delay is needed to allow the DOM to update before starting the transition
            setTimeout(() => {
                mobileMenuPanel.classList.remove('-translate-x-full');
            }, 20);
        };

        const closeMenu = () => {
            mobileMenuPanel.classList.add('-translate-x-full');
            // Hide the menu completely after the transition finishes
            setTimeout(() => {
                mobileMenu.classList.add('hidden');
            }, 300); // This duration should match the transition duration in the HTML
        };

        mobileMenuButton.addEventListener('click', openMenu);
        mobileMenuCloseButton.addEventListener('click', closeMenu);
        // Also close the menu if the user clicks the overlay
        document.getElementById('mobile-menu-overlay').addEventListener('click', closeMenu);
    }

    // --- Upgraded Navbar Scroll Logic (from before) ---
    const header = document.getElementById('main-header');
    // ... (The rest of your navbar scroll logic remains the same)

    // --- Upsell Engine Logic (from before) ---
    const upsellEngine = document.getElementById('upsell-engine');
    // ... (The rest of your upsell engine logic remains the same)
});