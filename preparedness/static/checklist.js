function saveProgress(checkbox) {
    localStorage.setItem(checkbox.parentElement.innerText, checkbox.checked);
}

window.onload = () => {
    document.querySelectorAll("input[type='checkbox']").forEach(cb => {
        cb.checked = localStorage.getItem(cb.parentElement.innerText) === "true";
    });
};
