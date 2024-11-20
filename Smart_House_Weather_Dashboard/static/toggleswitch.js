let toggle = document.querySelector(".toggle");
let text = document.querySelector(".text");

function animatedToggle() {
  toggle.classList.toggle("active");
  if (toggle.classList.contains("active")) {
    text.innerHTML = "ON";
    console.log("ON");
  } else {
      console.log("OFF");
      text.innerHTML = JSON.parse("{{data}}");
  }
}
