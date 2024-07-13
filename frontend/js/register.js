$(document).ready(function() {
    $("#registerForm").validate({
        rules: {
            username: "required",
            password: "required",
            email: {
                required: true,
                email: true
            },
            first_name: "required",
            last_name: "required",
            address: "required",
            phone_number: "required"
        },
        submitHandler: function(form) {
            $.ajax({
                url: '/http://localhost:8000/api/usuarios/',
                type: 'POST',
                data: $(form).serialize(),
                success: function(response) {
                    alert('Usuario registered successfully!');
                    window.location.href = 'login.html';
                    console.log(response);
                },
                error: function(response) {
                    alert('An error occurred while registering the user. Please try again.');
                }
            });
        }
    });
});
