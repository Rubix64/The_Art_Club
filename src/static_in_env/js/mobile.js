let menuIcon = document.getElementById("menu-icon");
let bar=document.querySelectorAll(".menu-icon .bar");
let menuMobile=document.querySelector(".nav-bar2 .mobile .links");
menuIcon.addEventListener("click",()=>{
    menuIcon.classList.toggle("anim-moveright");
    bar[0].classList.toggle("anim-rot-45c");
    bar[1].classList.toggle("anim-disappear");
    bar[2].classList.toggle("anim-rot-45a");
    menuMobile.classList.toggle("anim-mobile-right");
})