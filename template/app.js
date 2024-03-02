function setCopyright() {
  const currentYear = document.querySelector("#currentYear");
  currentYear.innerHTML = new Date().getFullYear();
}
function debug() {
  const root = document.querySelector(":root");
  root.style.setProperty("--outline-color", "green");
}

function displayProgress() {
  let downloadSpeed = document.getElementById("download-speed");
  let downloadStatus = document.getElementById("download-status");
}
function toggleTab() {
  // TODO
}

displayProgress();
setCopyright();
toggleTab();
// debug();
