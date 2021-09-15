#!/usr/bin/node
/* This script prints the number of movies where the Wedge  is present */
const request = require('request');

const url = process.argv[2] + '1';
request(url, (error, response, body) => {
  if (error) {
    return console.error(error);
  }
  const url2 = (JSON.parse(body).characters[15]);
  request(url2, (error, response, body) => {
    if (error) {
      console.log(error);
    }
    console.log(JSON.parse(body).films.length);
  });
});
