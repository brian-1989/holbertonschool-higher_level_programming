#!/usr/bin/node
/* This script prints the number of movies where the Wedge  is present */
const request = require('request');
const id = 18;
let count = 0;

const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    return console.error(error);
  }
  const myList = JSON.parse(body).results;
  for (const dict of myList) {
    for (const urlFilms of dict.characters) {
      if (urlFilms.includes(id)) {
        count += 1;
      }
    }
  }
  console.log(count);
});
