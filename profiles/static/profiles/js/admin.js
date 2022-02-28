const checkboxes = document.querySelectorAll(".delete-all");
const deleteForms = document.querySelectorAll(".delete-form");

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

for (const form of deleteForms) {
  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const form_id = event.target.dataset.formId;

    const checked = document.querySelectorAll(
      `input[type=checkbox]:checked[data-form-id*="${form_id}"]`
    );
    let products = [];

    for (const checkbox of checked) {
      const product = checkbox.dataset.productName;
      if (product !== undefined) {
        products.push(product);
      }
    }

    let message = `Are you sure you want to delete ${
      products.length
    } item(s)? \n\n${products.join("\r\n")}`;

    if (confirm(message)) {
      event.target.submit();
    }
  });
}
