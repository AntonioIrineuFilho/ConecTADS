document.addEventListener("DOMContentLoaded", () => {
    const registerForm = document.getElementById("register_form");
    registerForm.addEventListener("submit", function(event) {
        event.preventDefault();
        const formData = new FormData(this);
        fetch("", {
            method: "POST",
            body: formData,
            headers: { "X-CSRFToken": formData.get("csrfmiddlewaretoken") }
        }) 
        .then(response => response.json()) 
        .then(data => {
            if (data.success) {
                window.location.href = data.redirect;
            } else {
                const usernameError = document.getElementById("username_error");
                const emailError = document.getElementById("email_error");
                if (data.errors.username[0]) {
                    usernameError.style.display = "block";
                    usernameError.innerHTML = data.errors.username[0];
                } else {
                    usernameError.style.display = "none";
                    usernameError.innerHTML= "";
                }
                if (data.errors.email[0]) {
                    emailError.style.display = "block";
                    emailError.innerHTML = data.errors.email[0];
                } else {
                    emailError.style.display = "none";
                    emailError.innerHTML = "";
                }
            }
        })
        .catch(error => console.log(error));
    })
})