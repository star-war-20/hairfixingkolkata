/* ═══════════════════════════════════════════════
   HAIR FIXING SERVICE KOLKATA — MAIN JS
   Lead Funnel Interactions & Animations
   ═══════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {

    // ── Sticky Header with Scroll Effect ──
    const header = document.querySelector('.header');
    const urgencyBanner = document.querySelector('.urgency-banner');

    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 60) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    }

    // ── Mobile Menu Toggle ──
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    const navOverlay = document.querySelector('.nav-overlay');

    if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', () => {
            menuToggle.classList.toggle('active');
            navLinks.classList.toggle('open');
            if (navOverlay) navOverlay.classList.toggle('active');
            document.body.style.overflow = navLinks.classList.contains('open') ? 'hidden' : '';
        });

        if (navOverlay) {
            navOverlay.addEventListener('click', () => {
                menuToggle.classList.remove('active');
                navLinks.classList.remove('open');
                navOverlay.classList.remove('active');
                document.body.style.overflow = '';
            });
        }

        // Close mobile menu on link click
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                menuToggle.classList.remove('active');
                navLinks.classList.remove('open');
                if (navOverlay) navOverlay.classList.remove('active');
                document.body.style.overflow = '';
            });
        });
    }

    // ── FAQ Accordion ──
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        const answer = item.querySelector('.faq-answer');

        if (question && answer) {
            question.addEventListener('click', () => {
                const isActive = item.classList.contains('active');

                // Close all other items
                faqItems.forEach(otherItem => {
                    if (otherItem !== item) {
                        otherItem.classList.remove('active');
                        const otherAnswer = otherItem.querySelector('.faq-answer');
                        if (otherAnswer) otherAnswer.style.maxHeight = null;
                    }
                });

                // Toggle current
                item.classList.toggle('active');
                if (!isActive) {
                    answer.style.maxHeight = answer.scrollHeight + 'px';
                } else {
                    answer.style.maxHeight = null;
                }
            });
        }
    });

    // ── Scroll Reveal Animation ──
    const revealElements = document.querySelectorAll('.reveal');
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                revealObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    revealElements.forEach(el => revealObserver.observe(el));

    // ── Hero Staggered Entrance Animation ──
    const heroStaggerEls = document.querySelectorAll('.hero-stagger');
    if (heroStaggerEls.length > 0) {
        const heroObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    // Trigger parent container first, then stagger children
                    const parent = entry.target.closest('.hero-content');
                    if (parent) {
                        const staggerItems = parent.querySelectorAll('.hero-stagger');
                        staggerItems.forEach((item) => {
                            const delay = parseInt(item.getAttribute('data-delay') || '0') * 150;
                            setTimeout(() => {
                                item.classList.add('animated');
                            }, delay);
                        });
                    }
                    heroObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });

        // Only observe the first stagger element to trigger all
        heroObserver.observe(heroStaggerEls[0]);
    }

    // ── Button Hover Ripple Effect ──
    const rippleButtons = document.querySelectorAll('.hero-btn-whatsapp, .hero-btn-call');
    rippleButtons.forEach(btn => {
        btn.addEventListener('mouseenter', (e) => {
            const ripple = btn.querySelector('.btn-ripple');
            if (ripple) {
                ripple.classList.remove('active');
                // Force reflow
                void ripple.offsetWidth;
                const rect = btn.getBoundingClientRect();
                ripple.style.left = (e.clientX - rect.left) + 'px';
                ripple.style.top = (e.clientY - rect.top) + 'px';
                ripple.classList.add('active');
            }
        });

        btn.addEventListener('mouseleave', () => {
            const ripple = btn.querySelector('.btn-ripple');
            if (ripple) {
                setTimeout(() => ripple.classList.remove('active'), 600);
            }
        });
    });

    // ── Magnetic Tilt Effect on Form Card ──
    const formCard = document.getElementById('heroFormCard');
    if (formCard) {
        const heroSection = document.getElementById('hero');

        heroSection.addEventListener('mousemove', (e) => {
            const rect = formCard.getBoundingClientRect();
            const cardCenterX = rect.left + rect.width / 2;
            const cardCenterY = rect.top + rect.height / 2;

            const deltaX = (e.clientX - cardCenterX) / rect.width;
            const deltaY = (e.clientY - cardCenterY) / rect.height;

            // Only apply tilt when mouse is reasonably close
            const distance = Math.sqrt(deltaX * deltaX + deltaY * deltaY);
            if (distance < 2) {
                const tiltX = deltaY * 3;  // subtle tilt
                const tiltY = -deltaX * 3;
                formCard.style.transform = `perspective(800px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) translateY(${formCard.style.animationPlayState === 'paused' ? 0 : ''}px)`;
                formCard.style.boxShadow = `${-deltaX * 15}px ${-deltaY * 15}px 60px rgba(0, 0, 0, 0.5), 0 0 30px rgba(212, 168, 83, ${0.05 + distance * 0.05})`;
            }
        });

        heroSection.addEventListener('mouseleave', () => {
            formCard.style.transform = '';
            formCard.style.boxShadow = '';
        });
    }

    // ── Counter Animation ──
    const counters = document.querySelectorAll('[data-count]');
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                const target = parseInt(el.getAttribute('data-count'));
                const suffix = el.getAttribute('data-suffix') || '';
                let current = 0;
                const increment = Math.max(1, Math.ceil(target / 60));
                const timer = setInterval(() => {
                    current += increment;
                    if (current >= target) {
                        current = target;
                        clearInterval(timer);
                    }
                    el.textContent = current + suffix;
                }, 30);
                counterObserver.unobserve(el);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(el => counterObserver.observe(el));

    // ── Countdown Timer for Urgency ──
    const countdownEl = document.querySelector('.countdown-timer');
    if (countdownEl) {
        let hours = 2, minutes = 47, seconds = 33;

        const updateCountdown = () => {
            seconds--;
            if (seconds < 0) { seconds = 59; minutes--; }
            if (minutes < 0) { minutes = 59; hours--; }
            if (hours < 0) { hours = 0; minutes = 0; seconds = 0; }

            const h = String(hours).padStart(2, '0');
            const m = String(minutes).padStart(2, '0');
            const s = String(seconds).padStart(2, '0');
            countdownEl.textContent = `${h}:${m}:${s}`;
        };

        setInterval(updateCountdown, 1000);
    }

    // ── Form Handling ──
    const forms = document.querySelectorAll('.lead-form');
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();

            const name = form.querySelector('[name="name"]');
            const phone = form.querySelector('[name="phone"]');
            const service = form.querySelector('[name="service"]');

            // Basic validation
            let valid = true;

            if (name && !name.value.trim()) {
                name.style.borderColor = '#ef4444';
                valid = false;
            } else if (name) {
                name.style.borderColor = '';
            }

            if (phone && (!phone.value.trim() || phone.value.trim().length < 10)) {
                phone.style.borderColor = '#ef4444';
                valid = false;
            } else if (phone) {
                phone.style.borderColor = '';
            }

            if (!valid) return;

            // Construct WhatsApp message
            const nameVal = name ? name.value.trim() : '';
            const phoneVal = phone ? phone.value.trim() : '';
            const serviceVal = service ? service.value : 'General Enquiry';

            const message = encodeURIComponent(
                `Hi! I'm ${nameVal}.\n` +
                `Phone: ${phoneVal}\n` +
                `I'm interested in: ${serviceVal}\n` +
                `I filled the form on hairfixingservicekolkata.com`
            );

            window.open(`https://wa.me/916297517526?text=${message}`, '_blank');

            // Show success state
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                const originalText = submitBtn.innerHTML;
                submitBtn.innerHTML = '✓ Sent! Redirecting to WhatsApp...';
                submitBtn.style.background = '#22c55e';
                setTimeout(() => {
                    submitBtn.innerHTML = originalText;
                    submitBtn.style.background = '';
                    form.reset();
                }, 3000);
            }
        });
    });

    // ── Smooth Scroll for Anchor Links ──
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                const offset = 100;
                const targetPos = target.getBoundingClientRect().top + window.pageYOffset - offset;
                window.scrollTo({ top: targetPos, behavior: 'smooth' });
            }
        });
    });

    // ── Gallery Filter ──
    const filterBtns = document.querySelectorAll('.filter-btn');
    const galleryItems = document.querySelectorAll('.gallery-item');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filter = btn.getAttribute('data-filter');

            galleryItems.forEach(item => {
                if (filter === 'all' || item.getAttribute('data-category') === filter) {
                    item.style.display = '';
                    item.style.opacity = '1';
                    item.style.transform = 'scale(1)';
                } else {
                    item.style.opacity = '0';
                    item.style.transform = 'scale(0.8)';
                    setTimeout(() => { item.style.display = 'none'; }, 300);
                }
            });
        });
    });

    // ── Active Nav Link ──
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-links a').forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPage || (currentPage === '' && href === 'index.html')) {
            link.classList.add('active');
        }
    });

    // ── Luxury Services 3D Tilt & Glow ──
    const luxuryCards = document.querySelectorAll('.luxury-tilt-card');
    luxuryCards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            // 3D Tilt calculation
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const deltaX = (x - centerX) / centerX;
            const deltaY = (y - centerY) / centerY;

            const tiltX = deltaY * 6; // subtle tilt intensity
            const tiltY = -deltaX * 6;

            card.style.transform = `perspective(1000px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) scale3d(1.02, 1.02, 1.02)`;
            card.style.boxShadow = `${-deltaX * 20}px ${-deltaY * 20}px 40px rgba(0,0,0,0.6), 0 0 25px rgba(212,168,83,0.15)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = '';
            card.style.boxShadow = '';
        });
    });

    // ── Luxury Services Parallax Background ──
    const servicesSection = document.querySelector('.luxury-services');
    const servicesBg = document.querySelector('.services-bg-overlay');
    if (servicesSection && servicesBg) {
        window.addEventListener('scroll', () => {
            const rect = servicesSection.getBoundingClientRect();
            if (rect.top <= window.innerHeight && rect.bottom >= 0) {
                const shiftY = (rect.top / window.innerHeight) * 60; // 60px max parallax movement
                servicesBg.style.transform = `translateY(${shiftY}px)`;
            }
        });
    }

    // ── Stagger Reveal for Modern Cards ──
    const serviceGrid = document.querySelector('.modern-cards');
    if (serviceGrid) {
        const cards = serviceGrid.querySelectorAll('.reveal');
        cards.forEach((card, index) => {
            card.style.transitionDelay = `${index * 0.15}s`;
        });
    }

    // ── Gold Particles Animation ──
    const canvas = document.getElementById('gold-particles');
    if (canvas && servicesSection) {
        const ctx = canvas.getContext('2d');
        let width = canvas.width = window.innerWidth;
        let height = canvas.height = servicesSection.offsetHeight;
        let particles = [];

        window.addEventListener('resize', () => {
            width = canvas.width = window.innerWidth;
            height = canvas.height = servicesSection.offsetHeight;
        });

        class Particle {
            constructor() {
                this.x = Math.random() * width;
                this.y = Math.random() * height;
                this.radius = Math.random() * 2 + 0.5;
                this.speedX = Math.random() * 0.4 - 0.2;
                this.speedY = Math.random() * -0.8 - 0.2; // soft float up
                this.opacity = Math.random() * 0.5 + 0.1;
            }

            update() {
                this.x += this.speedX;
                this.y += this.speedY;

                if (this.y < 0) this.y = height;
                if (this.x < 0) this.x = width;
                if (this.x > width) this.x = 0;
            }

            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                ctx.fillStyle = `rgba(212, 168, 83, ${this.opacity})`;
                ctx.fill();
            }
        }

        for (let i = 0; i < 60; i++) {
            particles.push(new Particle());
        }

        function animateParticles() {
            ctx.clearRect(0, 0, width, height);
            for (let i = 0; i < particles.length; i++) {
                particles[i].update();
                particles[i].draw();
            }
            requestAnimationFrame(animateParticles);
        }
        animateParticles();
    }

});
