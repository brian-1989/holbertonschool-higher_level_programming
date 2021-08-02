#!/usr/bin/node
/* This script convert the first argument in number */
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Not a number');
} else {
  console.log('My number: ', process.argv[2]);
}
