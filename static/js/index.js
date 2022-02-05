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
