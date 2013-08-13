// INSÈRE UN CARACTÈRE UNICODE APRÈS <DD>
(function($) {
    $.fn.postDD=function()
    {
        return this.each(function(){
            $(this).after("<span>⁀</span>");
        });
    };
})(jQuery);

function checkImageResolution(){
    // CHECK IMAGE RESOLUTION
    $("img.noir").each(function(){
        if ($(this).attr("id") != "cale-page"){
            height = $(this).height();
            naturalHeight = this.naturalHeight;
            ratio = naturalHeight/height;
            console.log(this);
            console.log(ratio);
            if (ratio < 5.5){
                $(this).parent().css("outline", "5px solid red");
                //$(this).css({"opacity": ".5", "background-color": "red"});
            }
        }
    });
}

$(window).load(function(){             
        // FAKE PAGES
        //doc_height = $("body").height();
        //page_height = $("#fakepage").height(); 
        //page_height = 22; 
        //nb_page = Math.ceil(doc_height/page_height) -2;
        //gutter = parseInt($("#fakepage").css("top"));  // = 1cm
        
        //for (i = 0; i <= nb_page; i++){
        //    $("#fakepage").clone().css({'outline-offset': '-1cm', 'display': 'block'}).attr("id","fakepage-p"+i).insertBefore($("#fakepage"));
        //}

        // AJOUTE UN UNICODE APRÈS <DD>
        $("dd").postDD();
        
        
        
        // PRÉPARATION À L'EXPORT, ON PASSE TOUT EN NOIR
        // IMAGES
        $("section#body.export img.preview").css("display", "none");
        $("section#body.export img.noir").css("display", "block");
        
        // VECTEURS
        $("section#body.export *").css({"color": "black", "border-color": "black", "outline-color": "black"});
        $(".folio p").css({"color": "black",});

        //checkImageResolution();

});
