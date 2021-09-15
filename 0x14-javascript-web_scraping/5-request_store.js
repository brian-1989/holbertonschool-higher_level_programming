#!/usr/bin/node
/* This script that gets the contents of a webpage and stores it in a file. */
const request = require('request');
const fs = require('fs');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
    if (err) {
      return console.log(err);
    }
  });
});
