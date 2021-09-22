/* This script adds a li element to a list when
the user clicks on the tag add_item*/
$('DIV#add_item').click(function () {
	$('ul').append("<li>Item</li>");
});
