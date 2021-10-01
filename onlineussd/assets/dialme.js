inp=document.getElementById('id_username');
inp.type="number";
inp.maxlength=100;
// inp.max=10

Greeting()
function Greeting(){
    var a=document.getElementById('greeting');
    var time=new Date().getHours();
    if( time <3){
        greet="Hello There"
    }
    else if (time<11){
        greet="Good Morning"
    }
    else if(time<16){
            greet="Good Afternoon"
        }
    else{
        greet="Good Evening"
    }
    a.innerHTML=greet
    setTimeout(Greeting,1000)
}

function Authenticate(){
    var form=document.getElementById("signup");
    form.addEventListener("onclick",function(){
        pass1=document.getElementById("id_password").Value;
        pass2=document.getElementById("password2").Value;
        if(pass1!=pass2){
            document.getElementById("passworderror").innerHTML="Passwords do not match"
            
        }
        mpin1=document.getElementById("mpin1").Value;
        mpin2=document.getElementById("mpin2").Value;
        if(mpin1!=mpin2){
            document.getElementById("pinerror").innerHTML="PINs do not match"
            
        }
    }
} 