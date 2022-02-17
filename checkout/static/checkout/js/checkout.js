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
        border: "1px solid black",
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

const paymentForm = document.querySelector("#payment-form");

paymentForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const { error } = await stripe.confirmPayment({
    elements,
    redirect: "if_required",
  });

  if (error) {
    const messageContainer = document.querySelector("#payment-errors");
    messageContainer.textContent = `Error: ${error.message}`;
  } else {
    paymentForm.submit();
  }
});
