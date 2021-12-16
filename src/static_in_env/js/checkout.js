let phnoWrong=document.getElementById('phno-wrong');
let zipcodeWrong=document.getElementById('zipcode-wrong');
let checkoutform=document.forms["checkoutform"];
function checkoutValidate(){
    let phno=checkoutform['phno'].value;
    let zipcode=checkoutform['zipcode'].value;
    let regex=/^[0-9]{10}$/;
    if(phno.length!=10){
        zipcodeWrong.style.display='none';
        phnoWrong.style.display='block';
        phnoWrong.innerHTML="Phone number must be 10 digits long."
        return false;
    }
    else if(!phno.match(regex)){
        zipcodeWrong.style.display='none';
        phnoWrong.style.display='block';
        phnoWrong.innerHTML="Please enter a valid phone number."
        return false;
    }
    else if(zipcode.length!=6){
        phnoWrong.style.display='none';
        zipcodeWrong.style.display='block';
        zipcodeWrong.innerHTML="Zipcode must be 6 digits long."
        return false;
    }
    else if(!zipcode.match(/^[0-9]{6}$/)){
        phnoWrong.style.display='none';
        zipcodeWrong.style.display='block';
        zipcodeWrong.innerHTML="Please enter a valid zipcode."
        return false;
    }
    return true;
}