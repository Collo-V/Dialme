new Vue({
    el:"#vue-app",
    data:{
        text:"What's up",
        text2:"You good?",
        name:"Eduardo",
        email:"https://mailto:collinsvictoromondi@gmail.com",
        divt:'<div class="divs">We are back online. Grab your favourite items on our <a href="http://www.fineteklabs.com">Website</a>',
        dwnlink:"",
    },
    methods:{
        Show:function(){
        
        this.dwnlink='<a href="http://www.finetek.com">Website</a>';
        
    },
      greet: function(){
            var time=new Date().getHours();
    if( time <3){
        greet="Hola"
    }
    else if (time<11){
        greet="Buenos dias"
    }
    else if(time<16){
            greet="Buenas tardes"
        }
    else{
        greet="Buenas noches"
    }
    return greet+" "+this.name+". Como estas?"
        },
    
    }

});


