// Beyond - Frontend JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Form validation feedback
    const forms = document.querySelectorAll('.needs-validation');
    forms.forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });

    // Rating star visualization
    const ratingInputs = document.querySelectorAll('input[name="rating"]');
    if (ratingInputs.length > 0) {
        ratingInputs.forEach(input => {
            input.addEventListener('change', function() {
                updateRatingDisplay(this.value);
            });
        });
    }

    // Expertise tags input helper
    const expertiseInput = document.querySelector('input[name="expertise"]');
    if (expertiseInput) {
        expertiseInput.addEventListener('blur', function() {
            // Clean up expertise input - remove extra spaces
            const cleaned = this.value.split(',').map(s => s.trim()).filter(s => s).join(', ');
            this.value = cleaned;
        });
    }

    // Search form - handle empty inputs
    const searchForm = document.querySelector('#searchForm');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            const roleInput = this.querySelector('input[name="role"]');
            const expertiseInput = this.querySelector('input[name="expertise"]');
            
            if (!roleInput.value && !expertiseInput.value) {
                e.preventDefault();
                alert('Please enter at least a role or expertise to search');
            }
        });
    }

    // Confirm delete actions
    const deleteButtons = document.querySelectorAll('.btn-delete');
    deleteButtons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
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
});

// Helper function to update rating display
function updateRatingDisplay(rating) {
    const container = document.querySelector('.rating-preview');
    if (container) {
        let stars = '';
        for (let i = 1; i <= 5; i++) {
            stars += i <= rating ? '★' : '☆';
        }
        container.innerHTML = `<span class="rating-stars">${stars}</span>`;
    }
}

// Helper function to format dates
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString(undefined, options);
}

// Copy to clipboard functionality
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showToast('Copied to clipboard!');
    }).catch(err => {
        console.error('Failed to copy:', err);
    });
}

// Show toast notification
function showToast(message) {
    const toast = document.createElement('div');
    toast.className = 'alert alert-success position-fixed top-0 end-0 m-3';
    toast.style.zIndex = '9999';
    toast.textContent = message;
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.remove();
    }, 3000);
}

