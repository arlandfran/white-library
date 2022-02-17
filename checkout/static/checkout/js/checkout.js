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
const submitBtn = document.querySelector("#submit-payment-form");
const messageContainer = document.querySelector("#payment-errors");

paymentForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  paymentElement.update({ disabled: true });
  submitBtn.disabled = true;
  submitBtn.innerHTML = `
      <div class="flex justify-center items-center p-4">
        <div class="spinner-border animate-spin inline-block w-8 h-8 border-4 rounded-full" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      </div>
    `;
  messageContainer.textContent = "";
  await stripe
    .confirmPayment({
      elements,
      redirect: "if_required",
    })
    .then(function (result) {
      if (result.error) {
        paymentElement.update({ disabled: false });
        submitBtn.disabled = false;
        submitBtn.innerHTML = "<div class='p-5'>place order</div>";
        messageContainer.textContent = `Error: ${result.error.message}`;
      } else {
        paymentForm.submit();
      }
    });
});
