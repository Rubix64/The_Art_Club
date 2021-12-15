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

let loginlink=document.getElementById("loginlink");
let login=document.getElementById("login");
let X1=document.getElementById("X1");
loginlink.addEventListener('click', ()=>{
    login.style.display='block';
})
X1.addEventListener('click', ()=>{
    login.style.display='none';
})

let signuplink=document.getElementById("signuplink");
let signup=document.getElementById("signup");
let X2=document.getElementById("X2");
signuplink.addEventListener('click', ()=>{
    signup.style.display='block';
})
X2.addEventListener('click', ()=>{
    signup.style.display='none';
})

let signupform=document.forms["signupform"];
let wrong=document.querySelectorAll("#signup .loginform .wrong");

// function signupvalidate(){
//     let pwd=signupform["password"].value;
//     let confirmpwd=signupform["confirmpassword"].value;
//     wrong.forEach(element => {
//         element.style.display='none';
//     });
//     if(pwd.length<8){
//         wrong[2].innerHTML="Password must aleast be of 8 characters";
//         wrong[2].style.display="block";
//         return false;
//     }
//     else if(pwd != confirmpwd){
//         wrong[3].innerHTML="Password doesn't match";
//         wrong[3].style.display='block';
//         return false;
//     }
//     else{
//         return true;
//     }
// }

