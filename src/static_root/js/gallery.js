artpics=[
`https://i.pinimg.com/564x/6f/5a/b1/6f5ab1b470beeeeaf285bb451c63ac8f.jpg`,
`../images/gallery images/art1.jpeg`,
`../images/gallery images/art2.jpg`,
`../images/gallery images/art3.jpeg`,
`../images/gallery images/art4.jpg`,
`../images/gallery images/art5.jpg`,
`../images/gallery images/art6.jpg`,
`../images/gallery images/art7.jpeg`,
`../images/gallery images/art8.jpg`,
`../images/gallery images/art9.jpg`
]

arttitles = ['Flower Embroidery Hoop Art','Carnival - Design','Colors','Cartoon art Abstract','Fungi','Abstract Potraits','Toy Architecture','Joy of Life','Balloons in the Midnight','The Aging Leaves']

artists=['Name1','Name2','Name3','Name4','Name5','Name6','Name7','Name8','Name9','Name10']

let notclickheart=1;

let imagecontentcreate=document.querySelector('.image-containers');
let container=document.querySelectorAll('.image-containers .container');
for(let i=0;i<artpics.length-1;i++){ //artpics.length-1 since there's an already existing .container class
    let containerclone=container[0].cloneNode(true);
    imagecontentcreate.appendChild(containerclone);
}

let imageContainers=document.querySelectorAll('.image-containers .container');
imageContainers.forEach((element,index)=>{
    element.style.backgroundImage=`url('${artpics[index]}')`;
    // console.log(element.children);
    element.children[0].children[1].children[0].textContent=arttitles[index];
    element.children[0].children[2].children[1].textContent=artists[index];
})

let heart=document.querySelectorAll('.image-containers .container .overlay .heart');
// console.log(heart);
heart.forEach(element=>{
    element.addEventListener('click', ()=>{
        if(element.children[0].style.display == 'none'){
            element.children[0].style.display='block';
            element.children[1].style.display='none';
        }
        else{
            element.children[1].style.display='block';
            element.children[0].style.display='none';
        }
    })
})

imageContainers.forEach((element, index)=>{
    element.addEventListener('click',()=>{
        // element.children[0].children[0].addEventListener('click',()=>{
        //     notclickheart=0;
        // })
        heart.forEach(element=>{
            element.onclick=()=>{
                notclickheart=0;
            }
        })
        if(notclickheart){
            // console.log('a');
        let imagedisplay=document.querySelectorAll(".image-display");
        imagedisplay[0].classList.add('image-display-show');
        imagedisplay[0].children[1].children[0].setAttribute("src",artpics[index]);
        imagedisplay[0].children[1].children[0].setAttribute("alt",arttitles[index]);
        }
        notclickheart=1;
    }) 
})

let imageDisplay=document.querySelectorAll('.image-display');
let imgDisplayClose=document.querySelectorAll('.image-display .close');
imgDisplayClose[0].addEventListener('click', ()=>{
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