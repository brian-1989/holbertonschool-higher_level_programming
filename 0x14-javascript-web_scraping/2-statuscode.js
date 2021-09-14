#!/usr/bin/node
/* This script that display the status code of a GET request */
const request = require('request');

request.get(process.argv[2], (error, response) => {
  if (error) {
    return 'code: ' + response.statusCode;
  }
  console.log('code: ' + response.statusCode);
});
