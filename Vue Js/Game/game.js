mygame=new Vue({
    el:"#gamediv",
    data:{
        image1:"Images/Din1.jpg",
        image2:"Images/Din-duck.jpg",
        obs1:"obs1",
        obs2:"obs2",
        obs3:"obs3",
        index:0,
        obs:"",
        bar1:{post:"right:40px",offs:0},
        bar2:{post:"right:100px",offs:0},
        bar3:{post:"right:500px",offs:0},
        dino:{top:0,offs:0}
        
    },
    methods:{
        incindex: function() {
            this.index += 1;
            
            setTimeout(this.incindex,200)
          },
          jump:function(event){
            y=document.getElementById("dino");
            y.classList.add("jump");
            
            
            setTimeout(function(){ y.classList.remove("jump");},1000)
            console.log(this.$refs);
            // this.$refs.dino.offsetLeft = 500;
            // document.getElementById("dino").style.margin="100px";

            console.log(this.$refs.obs1.offsetLeft)


        },
        duck: function(){
            this.image1=this.image2;
            
        },
        obstacle: function(){
            x = Math.floor((Math.random() * 3) + 1);
            if(x==1){this.obs=this.obs1}
            else if(x==2){this.obs=this.obs2}
            else if(x==3){this.obs=this.obs3}
            else{obs=""}
            t=document.getElementById(this.obs);
            
            t.classList.add("obstacle")
            // setTimeout(function(){ t.classList.remove("obstacle")},6000)
            setTimeout(this.obstacle,2000)

        },
        remover:function(){
            t=document.getElementsByClassName("obstacle")[0];
            t.classList.remove("obstacle");
            // t=document.getElementById(this.obs);
            // t.classList.remove("obstacle")
            f=document.getElementById(this.obs);
            setTimeout(this.remover,6000)
        },
        offset: function(){
            this.dino.offs=a=this.$refs.dino.offsetLeft;
            this.bar1.offs=b=this.$refs.obs1.offsetLeft;
            this.bar2.offs=c=this.$refs.obs2.offsetLeft;
            this.bar3.offs=d=this.$refs.obs3.offsetLeft;
            this.dino.top=e=this.$refs.dino.offsetTop;
            if(a>=b||a>=c||a>=d){
                if(this.$refs.obs1.offsetHeight-e<=0){alert("WRECK!")}
            else if(a>=c){tolook=this.$refs.obs1.offsetHeight}
            else if(a>=d){tolook=this.$refs.obs1.offsetHeight}

            // setTimeout(this.offset,100)

            }
            
            setTimeout(this.offset,50)

        }

    },
    computed:{
        
    }
})
// mygame.incindex()