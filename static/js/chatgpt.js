document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.category-buttons button');
    const inputSections = document.querySelectorAll('.input-section');

    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const target = this.getAttribute('data-target');
            
            // Deactivate all buttons and hide all input sections
            buttons.forEach(btn => btn.classList.remove('active'));
            inputSections.forEach(section => section.style.display = 'none');
            
            // Activate clicked button and show corresponding input section
            this.classList.add('active');
            document.getElementById(`${target}-input`).style.display = 'block';
        });
    });
});