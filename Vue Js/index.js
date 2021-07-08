new Vue({
    el:"#vue-app",
    data:{
        text:"What's up",
        text2:"You good?",
        name:"Eduardo",
        email:"https://mailto:collinsvictoromondi@gmail.com",
        divt:'<div class="divs">We are back online. Grab your favourite items on our <a href="http://www.fineteklabs.com">Website</a>',
        dwnlink:"",
        comida:"",
        timer:10,
        start:'<button v-on:click="startgame" ref="start">Start</button>',
        words:0,
        avg:0,
        speed:10,highest:0

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
update: function(event){
    // console.log(event);
    this.comida=this.$refs.likes.value.toUpperCase();
        console.log(this.$refs);
        },
        startgame: function (){
            txt=this.$refs.likes;
            txt.onpaste = e => {
                e.preventDefault();
                return false}
            
           this.timer-=1;
           if(this.timer<=0){
               txt.disabled=true;
               document.getElementById("startbtn").style.display="none";
               document.getElementById("gameover").style.display="block";
               a=this.comida.length;
               word=this.words=this.comida.split(" ");
            //    word = word.every(myFunction);

            // function myFunction(value) {
            // if(value!=""){return value};}
            
               this.words=word.length;
               this.avg=parseInt(a/this.words);
               this.speed=this.words*6;if(this.speed>this.highest){this.highest=this.speed}
               console.log(this.comida)
               return
            }
           
           setTimeout(this.startgame,1000)
                       

        },
        restart:function(){
            this.$refs.likes.value="",
            this.timer=10;
            this.$refs.likes.disabled=false;
            document.getElementById("startbtn").style.display="block";
            document.getElementById("gameover").style.display="none";
            }
    
    }

});


