	// Sam Clark Tribe 2012
  // javascript for shirtview.html logic
  // slider and displaying / interacting with shirt data

  // disable submit so we can override
	$('.shirt_form').submit(function() {return false;});
	$('.send_shirt').click(function(event){
		var $form = $(this).parent("form");
		var url = $form.attr("action")
		var shirt_data = $form.serialize();
		console.log("hereee")
		$.post(url,shirt_data, {} ,'json')
	});

	// modified from bxSlider example
	$(document).ready(function(){
    	$('.bx_slider').bxSlider({
    		controls:false,
    		prevText:"",
    		nextText:""
    	});
  	});

	$(function(){
  // assign the slider to a variable
 		 var slider = $('.bx_slider').bxSlider({
    	controls: false,
  	});

  // assign a click event to the external thumbnails
    $('.thumbs a').click(function(){
    	// jequery element to change description and pattern name
    	var description_html = $('.shirt_description .description_text');
    	var pattern_name_html = $('.shirt_description .pattern_name')
    	// jquery for thumbnail click
   		var thumbIndex = $('.thumbs a').index(this);

   		// change description, pattern based on shirt clicked
   		pattern_name_html.html("<h2> django_shirt.pattern </h2>")
   		description_html.html("<p> django_shirt.description </p>")



    	slider.goToSlide(thumbIndex);

  
    // remove all active classes
    $('.thumbs a').removeClass('pager-active');
    // assisgn "pager-active" to clicked thumb
    $(this).addClass('pager-active');
    // very important! you must kill the links default behavior
    	return false;
  	});

  // assign "pager-active" class to the first thumb
 	$('.thumbs a:first').addClass('pager-active');
	});

