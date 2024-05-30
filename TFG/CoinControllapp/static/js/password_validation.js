// password_validation.js

$(document).ready(function() {
    $('#id_password').on('input', function() {
        var password = $(this).val();
        var passwordError = $('#password-error');

        var errors = [];

        if (password.length < 6) {
            errors.push('La contraseña debe tener al menos 6 caracteres');
        }
        if (!/\d/.test(password)) {
            errors.push('La contraseña debe contener al menos un número');
        }
        if (!/[A-Z]/.test(password)) {
            errors.push('La contraseña debe contener al menos una letra mayúscula');
        }

        passwordError.html(errors.join('</br>'));
    });
    $('#id_password2').on('input', function() {
        var password = $(this).val();
        var passwordError = $('#password-error2');

        var errors = [];

        if (password.length < 6) {
            errors.push('La contraseña debe tener al menos 6 caracteres');
        }
        if (!/\d/.test(password)) {
            errors.push('La contraseña debe contener al menos un número');
        }
        if (!/[A-Z]/.test(password)) {
            errors.push('La contraseña debe contener al menos una letra mayúscula');
        }

        passwordError.html(errors.join('</br>'));
    });
});
