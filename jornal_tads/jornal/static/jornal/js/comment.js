document.addEventListener("DOMContentLoaded", () => {
    const content = document.getElementById("conteudo");
    const contentError = document.getElementById("conteudo_error");
    const createComment = document.getElementById("create_comment");
    const createCommentForm = document.getElementById("create_comment_form");

    const validateContent = (content, contentError) => {
        if (content.value.trim() == "") {
            contentError.style.display = "block";
            contentError.innerHTML = "O comentário não pode estar vazio";
        } else {
            contentError.style.display = "none";
            contentError.innerHTML = "";
        }
    }

    content.addEventListener("input", function() {
        validateContent(content, contentError);
    })

    content.addEventListener("blur", function() {
        validateContent(content, contentError);
    })

    createComment.addEventListener("click", function() {
        createCommentForm.style.display = "block";
    })

   createCommentForm.addEventListener("submit", function(event) {
        event.preventDefault();
        validateContent(content, contentError);
        if (contentError.innerHTML == "") {
            this.style.display = "none";
            const formData = new FormData(this);
            const formActionUrl = this.action;
            fetch(formActionUrl, {
                method: "POST",
                body: formData,
                headers: { "X-CSRFToken": formData.get("csrfmiddlewaretoken") }
            }) 
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const commentSection = document.getElementById("async_comments");
                    const newComment = `
                    <div class="box is-dark mb-4">
                        <p class="title is-5 has-text-white">${data.comment.username}</p>
                        <p class="content has-text-white-ter">${data.comment.conteudo}</p>
                    </div>
                    `;
                    commentSection.insertAdjacentHTML("afterbegin", newComment);
                }
            })
            .catch(error => console.log(error));
        }
            
    })
})