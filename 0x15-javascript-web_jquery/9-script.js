/* This script fetches the value of hello from that a URL */
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  $('DIV#hello').text(data.hello);
});
