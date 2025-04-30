form.addEventListener('submit', function (e) {
    e.preventDefault();

    const name = document.getElementById('id_name').value.trim();
    const contact = document.getElementById('id_contact_info').value.trim();
    const message = document.getElementById('id_message').value.trim();

    if (!name || !contact || !message) {
        errorMessage.classList.remove('d-none');
        successMessage.classList.add('d-none');
        return;
    }

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch("{% url 'contactform' %}", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrfToken
        },
        body: new URLSearchParams({
            'name': name,
            'contact_info': contact,
            'message': message
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (data.success) {
            form.reset();
            successMessage.classList.remove('d-none');
            errorMessage.classList.add('d-none');

            // 3 soniyadan so'ng xabarni yashirish
            setTimeout(() => {
                successMessage.classList.add('d-none');
            }, 3000);
        } else {
            throw new Error(data.error || 'Xatolik yuz berdi.');
        }
    })
    .catch(error => {
        errorMessage.textContent = error.message;
        errorMessage.classList.remove('d-none');
        successMessage.classList.add('d-none');
    });
});