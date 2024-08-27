// static/js/user_signup.js
document.addEventListener('DOMContentLoaded', function() {
    var passwordAuthField = document.querySelector('input[name="password_based_authentication"]');
    if (passwordAuthField) {
        passwordAuthField.checked = true;
    }
});