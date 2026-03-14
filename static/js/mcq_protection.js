// MCQ Content Protection Script
(function () {
    'use strict';

    console.log('MCQ Protection Script Loaded');

    // Disable right-click context menu
    document.addEventListener('contextmenu', function (e) {
        if (e.target.closest('.protected-content')) {
            e.preventDefault();
            return false;
        }
    });

    // Disable copy
    document.addEventListener('copy', function (e) {
        if (e.target.closest('.protected-content')) {
            e.preventDefault();
            return false;
        }
    });

    // Disable cut
    document.addEventListener('cut', function (e) {
        if (e.target.closest('.protected-content')) {
            e.preventDefault();
            return false;
        }
    });

    // Disable keyboard shortcuts (only in protected content)
    document.addEventListener('keydown', function (e) {
        // Only apply to protected content
        if (!e.target.closest('.protected-content')) {
            return;
        }

        // Disable F12, Ctrl+Shift+I, Ctrl+Shift+J, Ctrl+U (dev tools)
        if (e.keyCode == 123 ||
            (e.ctrlKey && e.shiftKey && (e.keyCode == 73 || e.keyCode == 74)) ||
            (e.ctrlKey && e.keyCode == 85)) {
            e.preventDefault();
            return false;
        }

        // Disable Ctrl+C, Ctrl+X, Ctrl+A (copy/cut/select all)
        if (e.ctrlKey && (e.keyCode == 67 || e.keyCode == 88 || e.keyCode == 65)) {
            e.preventDefault();
            return false;
        }

        // Disable Print Screen
        if (e.keyCode == 44) {
            e.preventDefault();
            return false;
        }
    });

    console.log('Protection: All protections enabled');

})();
