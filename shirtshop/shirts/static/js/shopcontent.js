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


   // assign a click event to the external thumbnails
    $('.thumbs a').click(function(){
      // jequery element to change description and pattern name
    
      console.log("yo");
      // jquery for thumbnail click
      var thumbIndex = $('.thumbs a').index(this);
      change_shirt_info(thumbIndex);
      var pic = $('.main_picture');
      console.log(pic);
    });

      // change description, pattern based on shirt clicked
   



      

    function change_shirt_info(idx)
    {
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
 

