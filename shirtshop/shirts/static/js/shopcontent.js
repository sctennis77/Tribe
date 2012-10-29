	// Sam Clark Tribe 2012
  // javascript for shirtview.html logic
  // slider and displaying / interacting with shirt data

  // disable submit so we can override
	$('.shirt_form').submit(function() {return false;});
	$('.send_shirt').click(function(event){
		var $form = $(this).parent("form");
		var url = $form.attr("action")
		var shirt_data = $form.serialize();
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
    
      // jquery for thumbnail click
      var thumbIndex = $('.thumbs a').index(this);
      change_shirt_info(thumbIndex);

      // change description, pattern based on shirt clicked
   



      slider.goToSlide(thumbIndex);

  
    // remove all active classes
    $('.thumbs a').removeClass('pager-active');
    // assisgn "pager-active" to clicked thumb
    $(this).addClass('pager-active');
    // very important! you must kill the links default behavior
      return false;
    });

    function change_shirt_info(idx)
    {
      console.log(idx);
      var description_text_html = $('.shirt_description .description_text');
      var pattern_name_html = $('.shirt_description .pattern_name');
      // instead of shirt_list[0] this will be shirt_list[idx] where idx
      // is the thumbnail clicked
      var pattern_name = shirt_list[idx].fields.pattern;
      var description_text = shirt_list[idx].fields.description;
      pattern_name_html.html(make_html_text("<h2>",pattern_name,"</h2>"));
      description_text_html.html(make_html_text("<p>",description_text,"<p>"));
    }
    function make_html_text(tag,text,endtag)
    {
      var html_text = tag + text + endtag;
      return html_text
    }

  // assign "pager-active" class to the first thumb
 	$('.thumbs a:first').addClass('pager-active');
	});

