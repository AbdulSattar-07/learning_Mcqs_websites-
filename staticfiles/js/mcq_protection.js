// MCQ Content Protection Script - DISABLED FOR DEBUGGING
// This script is temporarily disabled to fix button functionality

(function () {
    'use strict';

    console.log('MCQ Protection Script Loaded (Minimal Mode)');

    // Only keep essential protection, remove anything that blocks interactions

    // Disable right-click context menu (keep this)
    document.addEventListener('contextmenu', function (e) {
        if (e.target.closest('.protected-content')) {
            e.preventDefault();
            return false;
        }
    });

    // Disable copy (keep this)
    document.addEventListener('copy', function (e) {
        if (e.target.closest('.protected-content')) {
            e.preventDefault();
            return false;
        }
    });

    console.log('Protection: Right-click and copy disabled only');

})();
