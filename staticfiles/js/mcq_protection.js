// MCQ Content Protection Script - FIXED
(function () {
    'use strict';

    console.log('MCQ Protection Script Loaded');

    // Disable right-click context menu (but NOT on buttons)
    document.addEventListener('contextmenu', function (e) {
        // Allow context menu on buttons and interactive elements
        if (e.target.closest('button, .btn, input, select, textarea, a')) {
            return true;
        }

        if (e.target.closest('.protected-content')) {
            e.preventDefault();
            return false;
        }
    });

    // Disable copy (but NOT on buttons)
    document.addEventListener('copy', function (e) {
        // Allow copy on input fields
        if (e.target.closest('input, textarea')) {
            return true;
        }

        if (e.target.closest('.protected-content')) {
            e.preventDefault();
            return false;
        }
    });

    // Disable cut (but NOT on buttons)
    document.addEventListener('cut', function (e) {
        // Allow cut on input fields
        if (e.target.closest('input, textarea')) {
            return true;
        }

        if (e.target.closest('.protected-content')) {
            e.preventDefault();
            return false;
        }
    });

    // Disable keyboard shortcuts (only in protected content, NOT on interactive elements)
    document.addEventListener('keydown', function (e) {
        // Allow all keyboard events on buttons and interactive elements
        if (e.target.closest('button, .btn, input, select, textarea, a')) {
            return true;
        }

        // Only apply to protected content
        if (!e.target.closest('.protected-content')) {
            return true;
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

    console.log('Protection: All protections enabled (buttons excluded)');

})();
