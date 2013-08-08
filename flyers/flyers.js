// INSÈRE UN CARACTÈRE UNICODE APRÈS <DD>
(function($) {
    $.fn.postDD=function()
    {
        return this.each(function(){
            $(this).after("<span>⁀</span>");
        });
    };
})(jQuery);

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

        // CHECK IMAGE RESOLUTION
        $("img").each(function(){
            if ($(this).attr("id") != "cale-page"){
                height = $(this).height();
                naturalHeight = this.naturalHeight;
                ratio = naturalHeight/height;
                if (ratio < 5.5){
                    console.log(this);
                    console.log(ratio);
                    $(this).parent().css("outline", "5px solid red");
                    //$(this).css({"opacity": ".5", "background-color": "red"});
                }
            }
        });
});
