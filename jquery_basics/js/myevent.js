/*$('h1').click(function () {
    // console.log("There was a click!");
    $(this).text("I was changed!");
});*/
/*$('h1').dblclick(function () {
    $(this).toggleClass("turnBlue");
});*/

$('h1').on('mouseenter',function () {
    $(this).toggleClass("turnBlue");
});


$('li').click(function () {
    console.log('any li was clicked!');
});

/*$("input").eq(0).keypress(function (event) {
    // console.log(event);
    if(event.which === 13){
        $('h3').toggleClass('turnBlue');
    }
});*/

$('input').eq(1).on('click',function () {
  // $(".container").fadeOut(3000);
  $(".container").slideUp(3000);
});
