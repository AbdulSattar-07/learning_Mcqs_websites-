// MCQ Content Protection Script

(function () {
    'use strict';

    // Disable right-click context menu
    document.addEventListener('contextmenu', function (e) {
        e.preventDefault();
        return false;
    });

    // Disable text selection via mouse (but allow buttons to work)
    document.addEventListener('selectstart', function (e) {
        // Allow buttons and interactive elements to work
        if (e.target.tagName === 'BUTTON' || e.target.closest('button')) {
            return true;
        }
        if (e.target.closest('.protected-content')) {
            e.preventDefault();
            return false;
        }
    });

    // Disable keyboard shortcuts
    document.addEventListener('keydown', function (e) {
        // Disable Ctrl+C (Copy)
        if (e.ctrlKey && e.key === 'c') {
            e.preventDefault();
            return false;
        }

        // Disable Ctrl+X (Cut)
        if (e.ctrlKey && e.key === 'x') {
            e.preventDefault();
            return false;
        }

        // Disable Ctrl+V (Paste)
        if (e.ctrlKey && e.key === 'v') {
            e.preventDefault();
            return false;
        }

        // Disable Ctrl+U (View Source)
        if (e.ctrlKey && e.key === 'u') {
            e.preventDefault();
            return false;
        }

        // Disable Ctrl+S (Save)
        if (e.ctrlKey && e.key === 's') {
            e.preventDefault();
            return false;
        }

        // Disable F12 (Developer Tools)
        if (e.key === 'F12') {
            e.preventDefault();
            return false;
        }

        // Disable Ctrl+Shift+I (Developer Tools)
        if (e.ctrlKey && e.shiftKey && e.key === 'I') {
            e.preventDefault();
            return false;
        }

        // Disable Ctrl+Shift+J (Console)
        if (e.ctrlKey && e.shiftKey && e.key === 'J') {
            e.preventDefault();
            return false;
        }

        // Disable Ctrl+Shift+C (Inspect Element)
        if (e.ctrlKey && e.shiftKey && e.key === 'C') {
            e.preventDefault();
            return false;
        }

        // Disable PrintScreen (limited effectiveness)
        if (e.key === 'PrintScreen') {
            e.preventDefault();
            return false;
        }
    });

    // Disable copy event
    document.addEventListener('copy', function (e) {
        if (e.target.closest('.protected-content')) {
            e.preventDefault();
            return false;
        }
    });

    // Disable cut event
    document.addEventListener('cut', function (e) {
        if (e.target.closest('.protected-content')) {
            e.preventDefault();
            return false;
        }
    });

    // Disable paste event
    document.addEventListener('paste', function (e) {
        if (e.target.closest('.protected-content')) {
            e.preventDefault();
            return false;
        }
    });

    // Disable drag events
    document.addEventListener('dragstart', function (e) {
        if (e.target.closest('.protected-content')) {
            e.preventDefault();
            return false;
        }
    });

    // Detect developer tools (basic detection)
    let devtoolsOpen = false;
    const threshold = 160;

    setInterval(function () {
        if (window.outerWidth - window.innerWidth > threshold ||
            window.outerHeight - window.innerHeight > threshold) {
            if (!devtoolsOpen) {
                devtoolsOpen = true;
                console.clear();
            }
        } else {
            devtoolsOpen = false;
        }
    }, 1000);

    // Clear console periodically
    setInterval(function () {
        console.clear();
    }, 2000);

    // Disable print
    window.addEventListener('beforeprint', function (e) {
        e.preventDefault();
        alert('Printing is disabled for this content.');
        return false;
    });

})();
