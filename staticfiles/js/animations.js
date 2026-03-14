// ============================================
// PROFESSIONAL UI ANIMATIONS & INTERACTIONS
// FIXED VERSION - No interference with MCQ buttons
// ============================================

document.addEventListener('DOMContentLoaded', function () {

    // Smooth Scroll for Anchor Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Animate Elements on Scroll - DISABLED for MCQ cards
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe only non-MCQ cards
    document.querySelectorAll('.card:not(.mcq-card)').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        observer.observe(card);
    });

    // Add animation class
    const style = document.createElement('style');
    style.textContent = `
        .animate-in {
            animation: fadeInUp 0.6s ease-out forwards;
        }
        
        @keyframes fadeInUp {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    `;
    document.head.appendChild(style);

    // Form Input Animations
    document.querySelectorAll('.form-control, .form-select').forEach(input => {
        input.addEventListener('focus', function () {
            this.parentElement.classList.add('input-focused');
        });

        input.addEventListener('blur', function () {
            this.parentElement.classList.remove('input-focused');
        });
    });

    // Navbar Scroll Effect
    let lastScroll = 0;
    const navbar = document.querySelector('.navbar');

    if (navbar) {
        window.addEventListener('scroll', function () {
            const currentScroll = window.pageYOffset;

            if (currentScroll > 100) {
                navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.1)';
                navbar.style.padding = '0.5rem 0';
            } else {
                navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.05)';
                navbar.style.padding = '1rem 0';
            }

            lastScroll = currentScroll;
        });
    }

    // Alert Auto Dismiss
    document.querySelectorAll('.alert:not(.alert-success):not(.alert-info)').forEach(alert => {
        setTimeout(() => {
            alert.style.animation = 'slideOutRight 0.5s ease-out';
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });

    const alertStyle = document.createElement('style');
    alertStyle.textContent = `
        @keyframes slideOutRight {
            to {
                opacity: 0;
                transform: translateX(100px);
            }
        }
    `;
    document.head.appendChild(alertStyle);

    // Loading Spinner for Forms (excluding MCQ buttons)
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function (e) {
            const submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn && !submitBtn.disabled) {
                submitBtn.disabled = true;
                const originalText = submitBtn.innerHTML;
                submitBtn.innerHTML = '<span class="loading"></span> Processing...';

                // Re-enable after 3 seconds (in case of error)
                setTimeout(() => {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalText;
                }, 3000);
            }
        });
    });

    // Console Welcome Message
    console.log('%c🎓 MCQ Learning Platform', 'font-size: 20px; font-weight: bold; color: #4f46e5;');
    console.log('%cWelcome to the National Skill Competency Test Platform', 'font-size: 14px; color: #6b7280;');

});

// Page Load Animation
window.addEventListener('load', function () {
    document.body.style.animation = 'fadeIn 0.5s ease-out';
});
