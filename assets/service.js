function choices(){
    var c=document.getElementById("choice").value;
    var d=document.getElementById("div"+c);
    
    
    var x=document.getElementsByClassName("servicediv");
    for(var i=0;i<x.length;i++){
        x[i].style.display="none";
    }
    d.style.display="block";
}
    function topchoices(n){
        var a=document.getElementsByClassName('topchoice');
        var y=document.getElementById("recp");
        for(var i=0;i<a.length;i++){a[i].removeAttribute('style')}
        a[n].style.borderBottom="solid 5px #209cee";
        if(n==0){y.style.display="none";y.getElementsByTagName("input")[0].value=""}
        if(n==1){document.getElementById("recp").style.display="block"}
    }


  var body=document.getElementsByTagName("body")[0];
    body.addEventListener("load",function Greeting(){
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
    })
    

function limits(n){
    document.getElementById("okoatake").value=n;
}

function View(n){
    var a=document.getElementById("password1");
    var b=document.getElementById("view");
    if(n==1){
        a.type="text";
        b.style.display="none";
    }
    else{
        a.type="password";
        b.style.display="inline";
    }
   
}