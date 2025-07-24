document.addEventListener("DOMContentLoaded", () => {
    const createNewsForm = document.getElementById("create_news_form");
    const createNews = document.getElementById("create_news");
    const title = document.getElementById("titulo");
    const titleError = document.getElementById("titulo_error");
    const content = document.getElementById("conteudo");
    const contentError = document.getElementById("conteudo_error");
    const titleRegex = /^.{10,}$/;
    const contentRegex = /^.{100,}$/;
    
    createNews.addEventListener("click", function() {
        createNewsForm.style.display = "block";
    })

    const validateField = (regex, field, fieldError, value) => {
        if (!regex.test(field.value)) {
            fieldError.style.display = "block";
            fieldError.innerHTML = value;
        } else {
            fieldError.style.display = "none";
            fieldError.innerHTML = "";
        }
    }
    
    document.addEventListener("input", function(event) {
        if (event.target == title) {
            validateField(titleRegex, title, titleError, "O título da notícia deve possuir no mínimo 10 caracteres");
        }
        if (event.target == content) {
            validateField(contentRegex, content, contentError, "O título da notícia deve possuir no mínimo 100 caracteres");
        }
    })

    document.addEventListener("blur", function(event) {
        if (event.target == title) {
            validateField(titleRegex, title, titleError, "O título da notícia deve possuir no mínimo 10 caracteres");
        }
        if (event.target == content) {
            validateField(contentRegex, content, contentError, "O título da notícia deve possuir no mínimo 100 caracteres");
        }
    })

    createNewsForm.addEventListener("submit", function(event) {
        if (titleError.innerHTML !== "" || contentError.innerHTML !== "") {
            event.preventDefault();
        } else {
            this.style.display = "none";
        }
    })

})