document.addEventListener("DOMContentLoaded", function () {
    const partSelect = document.getElementById("id_part");
    const mainQuestionRow = document.querySelector(".form-row.field-main_question");
    const mainQuestionInput = document.getElementById("id_main_question");

    if (!partSelect || !mainQuestionRow) return;

    function toggleMainQuestion() {
        if (partSelect.value === "part2") {
            console.log("part2 selected");
            mainQuestionRow.style.display = "";
        } else {
            console.log("part2 unselected");
            mainQuestionRow.style.display = "none";
            mainQuestionInput.value = "";
        }
    }

    toggleMainQuestion();
    partSelect.addEventListener("change", toggleMainQuestion);
});