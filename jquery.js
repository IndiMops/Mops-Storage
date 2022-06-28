$(document).ready(function(){
  $("#hider").click(function(){
    $("#alert").slideToggle("slow");
    $(this).toggleClass("active");
    $(".page-container-home").css("min-height", "90%");
  });

  $(".deteils-titlet").click(function(){
    $(".deteils-desc").slideToggle("slow");
    $(this).toggleClass("active");
  });

  //$(".one").hover(function() {
    //if ($(this).attr("src") == "assets/gallery-cover/red-dead-redemption-2.jpg") {
      //$(this).attr("src", "assets/gallery-cover/2.jpg");
    //} else {
      //$(this).attr('src', "assets/gallery-cover/red-dead-redemption-2.jpg");
    //}
  //});
});
