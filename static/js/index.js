const hamburger = document.querySelector("#hamburger");
const sidebar = document.querySelector("#sidebar");
const closeBtn = document.querySelector("#close-btn");
const sidebarElements = document.querySelectorAll(".sidebar-focusable");
const bag = document.querySelector("#bag");
const bagPreview = document.querySelector("#bag-preview");
const closeBagPreviewBtn = document.querySelector("#close-bag-preview");
const removeItemBtn = document.querySelectorAll(".remove-item-btn");
const clearBagBtn = document.querySelector("#clear-bag");
const csrfToken = document.cookie
  .split("; ")
  .find((row) => row.startsWith("csrftoken="))
  .split("=")[1];

const openSidebar = () => {
  const width = getComputedStyle(sidebar).width;
  if (width === "1px") {
    if (window.innerWidth < 475) {
      sidebar.style.width = "100%";
    } else {
      sidebar.style.width = "400px";
    }
    sidebarElements.forEach((element) => {
      element.setAttribute("tabindex", "0");
    });
  }
};

const closeSidebar = () => {
  sidebar.style.width = "0%";
  sidebarElements.forEach((element) => {
    element.setAttribute("tabindex", "-1");
  });
};

const toggleBagPreview = () => {
  if (bagPreview) {
    const classList = bagPreview.classList;
    const message = document.querySelector(".js-snackbar__close");
    // close message
    if (message) message.click();
    if (classList.contains("hidden")) {
      openBagPreview(classList);
    } else {
      closeBagPreview(classList);
    }
  }
};

const openBagPreview = (classList) => {
  classList.replace("hidden", "flex");
  window.setTimeout(function () {
    classList.replace("scale-y-0", "scale-y-100");
    classList.replace("opacity-0", "opacity-100");
  }, 0);
};

const closeBagPreview = (classList) => {
  classList.replace("opacity-100", "opacity-0");
  classList.replace("scale-y-100", "scale-y-0");
  window.setTimeout(function () {
    classList.replace("flex", "hidden");
  }, 100);
};

const removeItem = async (item) => {
  const itemId = item.dataset.itemId;
  const url = `/bag/remove/${itemId}/`;
  await fetch(url, {
    method: "POST",
    headers: { "X-CSRFToken": csrfToken },
  }).then(() => location.reload());
};

const clearBag = async () => {
  const url = `/bag/clear`;
  await fetch(url, {
    method: "POST",
    headers: { "X-CSRFToken": csrfToken },
  }).then(() => location.reload());
};

hamburger.addEventListener("click", openSidebar);
closeBtn.addEventListener("click", closeSidebar);
if (bag) bag.addEventListener("click", toggleBagPreview);
if (closeBagPreviewBtn)
  closeBagPreviewBtn.addEventListener("click", closeBagPreview);
if (removeItemBtn) {
  removeItemBtn.forEach((button) => {
    button.addEventListener("click", function () {
      removeItem(this);
    });
  });
}
if (clearBagBtn) clearBagBtn.addEventListener("click", clearBag);
