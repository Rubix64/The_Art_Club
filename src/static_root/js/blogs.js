let addart=document.querySelector('.addart');
let addartform=document.querySelector('.addart-form');
let addartclose=document.querySelector('.addart-form .close');
addart.addEventListener('click', ()=>{
    addartform.classList.add("addart-form-show");
})
addartclose.addEventListener('click', ()=>{
    addartform.classList.remove("addart-form-show");
})
