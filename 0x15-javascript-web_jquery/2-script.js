/* This script updates the text in the header tag when
the user clicks on the tag DIV#red_header */
$('DIV#red_header').click(function () {
  $('header').css('color', '#FF0000');
});
