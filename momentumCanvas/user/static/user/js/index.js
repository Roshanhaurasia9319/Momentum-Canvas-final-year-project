
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById('multiStepForm');
    const steps = Array.from(document.querySelectorAll('.form-step'));
    let currentStep = 0;

    function showStep(index) {
        steps.forEach((step, i) => {
            if (i === index) {
                step.classList.add('active');
            } else {
                step.classList.remove('active');
            }
        });
    }

    function nextStep() {
        // Validate current step
        const currentFormStep = steps[currentStep];
        const inputs = currentFormStep.querySelectorAll('input');
        let valid = true;
        inputs.forEach(input => {
            if (!input.checkValidity()) {
                input.classList.add('is-invalid');
                valid = false;
            } else {
                input.classList.remove('is-invalid');
            }
        });
        if (!valid) return;

        currentStep++;
        if (currentStep < steps.length) {
            showStep(currentStep);
        }
    }

    function skipStep() {
        currentStep++;
        if (currentStep < steps.length) {
            showStep(currentStep);
        }
    }

    document.querySelectorAll('.next-btn').forEach(button => {
        button.addEventListener('click', nextStep);
    });

    document.querySelectorAll('.skip-btn').forEach(button => {
        button.addEventListener('click', skipStep);
    });

    // Handle form submission
    form.addEventListener('submit', function (e) {
        // Optionally, add additional validation or processing here
        // For example, confirm submission
        // e.preventDefault();
        // alert('Form submitted!');
    });
});
