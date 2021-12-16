let imageDisplay=document.querySelectorAll('.image-display');
let imgDisplayClose=document.querySelectorAll('.image-display .close');
let success = document.querySelector('.image-display .image-fulldisplay img');
imgDisplayClose[0].addEventListener('click', ()=>{
    success.innerHTML="";
    imageDisplay[0].classList.remove('image-display-show');
})

let addart=document.querySelector('.addart');
let addartform=document.querySelector('.addart-form');
let addartclose=document.querySelector('.addart-form .close');
addart.addEventListener('click', ()=>{
    addartform.classList.add("addart-form-show");
})
addartclose.addEventListener('click', ()=>{
    addartform.classList.remove("addart-form-show");
})