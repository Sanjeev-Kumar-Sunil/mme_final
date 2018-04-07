$(document).ready(start);

function start(){
    switching();
  $(window).resize(
     function(){
      if(window.innerWidth <768){

          $(".bottomHeader").css({"display":"none"});
          $(".bottomHeaderSm").css({"display":"block"});
      }
      if(window.innerWidth >=768){
      $(".bottomHeader").css({"display":"block"});
      $(".bottomHeaderSm").css({"display":"none"});
    }
  }
);
}


function switching(){
      if(window.innerWidth <768){

          $(".bottomHeader").css({"display":"none"});
          $(".bottomHeaderSm").css({"display":"block"});
      }
      if(window.innerWidth >=768){
      $(".bottomHeader").css({"display":"block"});
      $(".bottomHeaderSm").css({"display":"none"});
    }
  }
