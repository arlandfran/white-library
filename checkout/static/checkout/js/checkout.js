// Stripe class imported in base.html
// eslint-disable-next-line no-undef
const stripe = Stripe(
  document.querySelector("#payment-form").dataset.publicKey
);

const options = {
  clientSecret: document.querySelector("#payment-form").dataset.secret,
  appearance: {
    theme: "flat",
    variables: {
      fontFamily:
        'Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
      borderRadius: "0",
    },
    rules: {
      ".Label": {
        fontSize: "1rem",
      },
      ".Input": {
        border: "1px solid #6b7280",
      },
      ".Input:focus": {
        boxShadow:
          "rgb(255, 255, 255) 0px 0px 0px 0px, rgb(0, 0, 0) 0px 0px 0px 1px, rgba(0, 0, 0, 0) 0px 0px 0px 0px",
      },
    },
  },
};

const elements = stripe.elements(options);

const paymentElement = elements.create("payment");
paymentElement.mount("#payment-element");

paymentElement.addEventListener("change", function (e) {
  const errorDiv = document.querySelector("#payment-errors");
  if (e.error) {
    const html = `
      <span role="alert">
        {% bs_icon "exclamation-circle" size="1.5em" extra_classes="fill-red-500" %}
      </span>
      <span>${e.error.message}</span>
    `;
    errorDiv.innerHTML(html);
  } else {
    errorDiv.textContent = "";
  }
});
