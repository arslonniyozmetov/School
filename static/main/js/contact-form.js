document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contact-form');
    const errorMessage = document.getElementById('error');
    const successMessage = document.getElementById('success');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const name = document.getElementById('id_name').value.trim();
        const contact = document.getElementById('id_contact_info').value.trim();
        const message = document.getElementById('id_message').value.trim();


        if (!name || !contact || !message) {
            errorMessage.textContent = "Iltimos, barcha maydonlarni to'ldiring!";
            errorMessage.classList.remove('d-none');
            successMessage.classList.add('d-none');
            return;
        }

        const formData = new FormData(form);



        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',  // Bu AJAX so'rov ekanligini bildiradi
            }
        })

        .then(response => response.json())
        .then(data => {
            if (data.response === 'success') {
                form.reset();
                successMessage.textContent = data.Message;
                successMessage.classList.remove('d-none');
                errorMessage.classList.add('d-none');

                setTimeout(() => {
                    successMessage.classList.add('d-none');
                }, 5000);
            } else {
                errorMessage.textContent = data.Message;
                errorMessage.classList.remove('d-none');
                successMessage.classList.add('d-none');
            }
        })
        .catch(error => {
            errorMessage.textContent = 'Xatolik yuz berdi. Iltimos, qayta urinib ko\'ring.';
            errorMessage.classList.remove('d-none');
            successMessage.classList.add('d-none');
        });
    });
});