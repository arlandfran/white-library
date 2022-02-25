const scrollToTopBtn = document.querySelector("#scrollToTop");
const categorySelect = document.querySelector("#category_selector");
const sortSelect = document.querySelector("#sort_selector");
const currentUrl = new URL(window.location);

// show button if user scrolls down 20px from the top
window.onscroll = function () {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    scrollToTopBtn.style.display = "block";
  } else {
    scrollToTopBtn.style.display = "none";
  }
};

const scrollToTop = () => {
  document.body.scrollTop = 0; // Safari
  document.documentElement.scrollTop = 0;
};

const selectCategory = () => {
  const category = categorySelect.value;
  if (category != "reset") {
    currentUrl.searchParams.set("category", category);
    window.location.replace(currentUrl);
  } else {
    currentUrl.searchParams.delete("category");
    window.location.replace(currentUrl);
  }
};

const sortProducts = () => {
  const sortValue = sortSelect.value;
  if (sortValue != "reset") {
    const sort = sortValue.split("_")[0];
    const direction = sortValue.split("_")[1];
    currentUrl.searchParams.set("sort", sort);
    currentUrl.searchParams.set("direction", direction);
    window.location.replace(currentUrl);
  } else {
    currentUrl.searchParams.delete("sort");
    currentUrl.searchParams.delete("direction");
    window.location.replace(currentUrl);
  }
};

scrollToTopBtn.addEventListener("click", scrollToTop);
categorySelect.addEventListener("change", selectCategory);
sortSelect.addEventListener("change", sortProducts);
