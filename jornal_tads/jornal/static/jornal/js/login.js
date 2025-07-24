document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.getElementById("login_form");
    loginForm.addEventListener("submit", function(event) {
        event.preventDefault();
        const formData = new FormData(this);
        fetch("", {
            method: "POST",
            body: formData,
            headers: {"X-CSRFToken": formData.get("csrfmiddlewaretoken")}
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.href = data.redirect;
            } else {
                const loginError = document.getElementById("login_error");
                loginError.style.display = "block";
                loginError.innerHTML = data.error;
            }
        })
        .catch(error => console.log(error));
    })
})