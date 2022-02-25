const checkboxes = document.querySelectorAll(".delete-all");

for (const checkbox of checkboxes) {
  checkbox.addEventListener("change", (event) => {
    const elements = document.querySelectorAll(".delete");
    if (event.target.checked) {
      for (const element of elements) {
        element.checked = true;
      }
    } else {
      for (const element of elements) {
        element.checked = false;
      }
    }
  });
}
