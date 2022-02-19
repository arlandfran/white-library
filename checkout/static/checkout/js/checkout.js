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
        padding: "0.75rem 0.5rem",
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
        <div class="inline-block w-8 h-8 rounded-full border-4 animate-spin spinner-border" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      </div>
    `;
  messageContainer.textContent = "";

  const saveInfo = document.querySelector("#id-save-info").checked;

  await fetch("/checkout/cache_checkout_data/", {
    method: "POST",
    // csrfToken defined in index.js
    // eslint-disable-next-line no-undef
    headers: { "X-CSRFToken": csrfToken },
    contentType: "application/json",
    body: JSON.stringify({
      client_secret: document.querySelector("#payment-form").dataset.secret,
      save_info: saveInfo,
    }),
  })
    .then(async () => {
      await stripe
        .confirmPayment({
          elements,
          redirect: "if_required",
          confirmParams: {
            payment_method_data: {
              billing_details: {
                address: {
                  line1: paymentForm.street_address1.value.trim(),
                  line2: paymentForm.street_address2.value.trim(),
                  city: paymentForm.town_or_city.value.trim(),
                  country: paymentForm.country.value.trim(),
                  state: paymentForm.county.value.trim(),
                },
                email: paymentForm.email.value.trim(),
                name: paymentForm.full_name.value.trim(),
                phone: paymentForm.phone_number.value.trim(),
              },
            },
            shipping: {
              address: {
                line1: paymentForm.street_address1.value.trim(),
                line2: paymentForm.street_address2.value.trim(),
                city: paymentForm.town_or_city.value.trim(),
                country: paymentForm.country.value.trim(),
                postal_code: paymentForm.postcode.value.trim(),
                state: paymentForm.county.value.trim(),
              },
              name: paymentForm.full_name.value.trim(),
              phone: paymentForm.phone_number.value.trim(),
            },
          },
        })
        .then(function (result) {
          if (result.error) {
            paymentElement.update({ disabled: false });
            submitBtn.disabled = false;
            submitBtn.innerHTML = "<div class='p-5'>place order</div>";
            messageContainer.textContent = `Error: ${result.error.message}`;
          } else {
            if (result.paymentIntent.status === "succeeded") {
              paymentForm.submit();
            }
          }
        });
    })
    .catch(() => {
      location.reload();
    });
});
