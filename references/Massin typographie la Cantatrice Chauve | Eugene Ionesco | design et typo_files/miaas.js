$jq = jQuery.noConflict();
$jq(document).ready(function($jq){     
$jq('#commentform').submit(function(){
      $jq(this).append($jq('<input />').attr('name','token').attr('id','token').attr('type','hidden'));      
      $jq('#token').val(miaas);      
      });         
});


