#!/usr/bin/node
/* This script writes a string in a file */
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
  if (err) {
    return console.error(err);
  }
});
