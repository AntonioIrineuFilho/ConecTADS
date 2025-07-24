document.addEventListener("DOMContentLoaded", () => {
    const today = new Date().toISOString().split("T")[0];
    document.getElementById("data").setAttribute("max", today);
    const createEdition = document.getElementById("create_edition");
    const createEditionForm = document.getElementById("create_edition_form");
    createEdition.addEventListener("click", function() {
        createEditionForm.style.display = "block";
    });
    createEditionForm.addEventListener("submit", function() {
        createEditionForm.style.display = "none";
    });
})