
$(document).ready(function(){
	a('#one1','#two2','#three3','#four4');
  $('a[href^="#"]').click(function(e){
    e.preventDefault();
    var target = this.hash;
    $('.bigimg img').hide()
    $(target).fadeIn(1000)
  });
  $('.imglist').fadeTo(0, 0.5)
  $('.imglist').hover(
  	function(){
      $(this).fadeTo('fast',1)
  	},
  	function(){
      $(this).fadeTo('fast',0.5)
  	});
})

function a(v1, v2, v3, v4){
   $(v1).fadeOut(1000)
   $(v2).fadeIn(1000, function(){
       a(v2,v3,v4,v1);
   })
}