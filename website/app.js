const hamburger_menu = document.querySelector(".hamburger-menu");
const container = document.querySelector(".container");

hamburger_menu.addEventListener("click", () => {
  container.classList.toggle("active");
});


// MOUSE PointerEvent

document.querySelector(
  "body").addEventListener("mousemove", eyeball);
  function eyeball() {
      var eye = document.querySelectorAll(".eye");
      eye.forEach(function (eye) {
          let x =
eye.getBoundingClientRect().left + eye.clientWidth / 3;
          let y =
eye.getBoundingClientRect().top + eye.clientHeight / 3;
          let radian =
      Math.atan2(event.pageX - x, event.pageY - y);
          let rot =
  radian * (200 / Math.PI) * 25 + 70;
          eye.style.transform =
          "rotate(" + rot + "deg)";
      });
  }



// FEEDBACK

var svgcircle = document.getElementById("svgcircle");
var step1 = document.getElementById("step1");
var step2 = document.getElementById("step2");
var step3 = document.getElementById("step3");
var step4 = document.getElementById("step4");
var step5 = document.getElementById("step5");
var feedback = document.getElementById("feedback");
var userbox = document.getElementById("userbox");

feedback.style.backgroundImage = "url(images/feed/SVG/img-3.jpg)";

step1.addEventListener('click', ()=>{
  svgcircle.style.strokeDashoffset = "1004";
  feedback.style.backgroundImage = "url(images/feed/SVG/img-2.jpg)";
  userbox.style.top = "-350px"
})
step2.addEventListener('click', ()=>{
  svgcircle.style.strokeDashoffset = "753";
  feedback.style.backgroundImage = "url(images/feed/SVG/img-3.jpg)";
  userbox.style.top = "-800px"
})
step3.addEventListener('click', ()=>{
  svgcircle.style.strokeDashoffset = "502";
  feedback.style.backgroundImage = "url(images/feed/SVG/img-4.jpg)";
  userbox.style.top = "-1250px"
})
step4.addEventListener('click', ()=>{
  svgcircle.style.strokeDashoffset = "251";
  feedback.style.backgroundImage = "url(images/feed/SVG/img-5.jpg)";
  userbox.style.top = "-170px"
})
step5.addEventListener('click', ()=>{
  svgcircle.style.strokeDashoffset = "1004";
  feedback.style.backgroundImage = "url(images/feed/SVG/img-1.jpg)";
  userbox.style.top = "100px"
})
