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
    a.innerText=greet;
    a.style.marginRight="10px"
    setTimeout(Greeting,1000)
}
 function navlink(n){
     var x=document.getElementsByClassName('navlink');
     var i=0;
     for(i;i<x.length;i++){x[i].style.borderBottom="none"}
     x[n].style.borderBottom="2px #209cee";
 }

 function Viewpass(a,n){
    if(a=="log"){a=document.getElementById("password1");
    b=document.getElementById("view");
    if(n==1){
        a.type="text";
        b.style.display="none";
    }
    else{
        a.type="password";
        b.style.display="inline";
    }
    }
    else{
        a=document.getElementById("password1");
        b=document.getElementById("view");
    if(n==1){
        a.type="text";
        b.style.display="none";
    }
    else{
        a.type="password";
        b.style.display="inline";
    }
    }
}