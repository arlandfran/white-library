function openSidebar() {
  if (window.innerWidth < 475) {
    document.getElementById("sidebar").style.width = "100%";
  } else {
    document.getElementById("sidebar").style.width = "400px";
  }
}

function closeSidebar() {
  document.getElementById("sidebar").style.width = "0%";
}

function selectCategory() {
  var select = document.getElementById("category_selector");
  var currentUrl = new URL(window.location);

  var category = select.value;

  if (category != "reset") {
    currentUrl.searchParams.set("category", category);
    window.location.replace(currentUrl);
  } else {
    currentUrl.searchParams.delete("category");
    window.location.replace(currentUrl);
  }
}

function sortProducts() {
  var select = document.getElementById("sort_selector");
  var currentUrl = new URL(window.location);

  var val = select.value;

  if (val != "reset") {
    var sort = val.split("_")[0];
    var direction = val.split("_")[1];

    currentUrl.searchParams.set("sort", sort);
    currentUrl.searchParams.set("direction", direction);
    window.location.replace(currentUrl);
  } else {
    currentUrl.searchParams.delete("sort");
    currentUrl.searchParams.delete("direction");
    window.location.replace(currentUrl);
  }
}

// show button if user scrolls down 20px from the top
window.onscroll = function () {
  scrollHandler();
};

function scrollHandler() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("scrollToTop").style.display = "block";
  } else {
    document.getElementById("scrollToTop").style.display = "none";
  }
}

function scrollToTop() {
  document.body.scrollTop = 0; // Safari
  document.documentElement.scrollTop = 0;
}
