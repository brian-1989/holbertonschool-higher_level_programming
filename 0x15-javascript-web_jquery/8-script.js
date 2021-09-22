/* This script fetches and lists the title for all movies by using this URL */
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (value) {
    $('UL#list_movies').append('<li>' + data.results[value].title + '</li>');
  });
});
