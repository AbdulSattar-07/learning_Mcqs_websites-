// ============================================
// PROFESSIONAL UI ANIMATIONS & INTERACTIONS
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

    // Animate Elements on Scroll
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

    // Observe all cards
    document.querySelectorAll('.card').forEach(card => {
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

    // Button Ripple Effect
    document.querySelectorAll('.btn').forEach(button => {
        button.addEventListener('click', function (e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;

            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.classList.add('ripple');

            this.appendChild(ripple);

            setTimeout(() => ripple.remove(), 600);
        });
    });

    // Add ripple styles
    const rippleStyle = document.createElement('style');
    rippleStyle.textContent = `
        .btn {
            position: relative;
            overflow: hidden;
        }
        
        .ripple {
            position: absolute;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.6);
            transform: scale(0);
            animation: ripple-animation 0.6s ease-out;
            pointer-events: none;
        }
        
        @keyframes ripple-animation {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(rippleStyle);

    // Form Input Animations
    document.querySelectorAll('.form-control, .form-select').forEach(input => {
        input.addEventListener('focus', function () {
            this.parentElement.classList.add('input-focused');
        });

        input.addEventListener('blur', function () {
            this.parentElement.classList.remove('input-focused');
        });
    });

    // Card Hover 3D Effect
    document.querySelectorAll('.card').forEach(card => {
        card.addEventListener('mousemove', function (e) {
            const rect = this.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const centerX = rect.width / 2;
            const centerY = rect.height / 2;

            const rotateX = (y - centerY) / 20;
            const rotateY = (centerX - x) / 20;

            this.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-8px) scale(1.02)`;
        });

        card.addEventListener('mouseleave', function () {
            this.style.transform = '';
        });
    });

    // Navbar Scroll Effect
    let lastScroll = 0;
    const navbar = document.querySelector('.navbar');

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

    // Alert Auto Dismiss
    document.querySelectorAll('.alert').forEach(alert => {
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

    // Loading Spinner for Buttons
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

    // Tooltip Enhancement
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl, {
            animation: true,
            delay: { show: 300, hide: 100 }
        });
    });

    // Badge Pulse Animation on Hover
    document.querySelectorAll('.badge').forEach(badge => {
        badge.addEventListener('mouseenter', function () {
            this.style.animation = 'pulse 0.5s ease-in-out';
        });

        badge.addEventListener('animationend', function () {
            this.style.animation = '';
        });
    });

    // Stagger Animation for Lists
    document.querySelectorAll('.row > div').forEach((item, index) => {
        item.style.animationDelay = `${index * 0.1}s`;
    });

    // Parallax Effect for Background
    window.addEventListener('scroll', function () {
        const scrolled = window.pageYOffset;
        const parallax = document.querySelector('body::before');
        if (parallax) {
            document.body.style.backgroundPosition = `0 ${scrolled * 0.5}px`;
        }
    });

    // Count Up Animation for Numbers
    function animateValue(element, start, end, duration) {
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            element.textContent = Math.floor(progress * (end - start) + start);
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };
        window.requestAnimationFrame(step);
    }

    // Animate numbers when visible
    document.querySelectorAll('[data-count]').forEach(element => {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const target = parseInt(element.getAttribute('data-count'));
                    animateValue(element, 0, target, 2000);
                    observer.unobserve(element);
                }
            });
        });
        observer.observe(element);
    });

    // Smooth Page Transitions
    document.querySelectorAll('a:not([href^="#"])').forEach(link => {
        link.addEventListener('click', function (e) {
            if (this.hostname === window.location.hostname) {
                e.preventDefault();
                const href = this.getAttribute('href');

                document.body.style.animation = 'fadeOut 0.3s ease-out';

                setTimeout(() => {
                    window.location.href = href;
                }, 300);
            }
        });
    });

    const transitionStyle = document.createElement('style');
    transitionStyle.textContent = `
        @keyframes fadeOut {
            to {
                opacity: 0;
                transform: scale(0.98);
            }
        }
    `;
    document.head.appendChild(transitionStyle);

    // Console Welcome Message
    console.log('%c🎓 MCQ Learning Platform', 'font-size: 20px; font-weight: bold; color: #4f46e5;');
    console.log('%cWelcome to the National Skill Competency Test Platform', 'font-size: 14px; color: #6b7280;');

});

// Page Load Animation
window.addEventListener('load', function () {
    document.body.style.animation = 'fadeIn 0.5s ease-out';
});
