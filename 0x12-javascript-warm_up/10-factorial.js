#!/usr/bin/node
/* This script computes and prints a factorial */
function factorial (a) {
  if (isNaN(a)) {
    return 1;
  }
  if (a === 0) {
    return 1;
  }
  return a * factorial(a - 1);
}
console.log(factorial(parseInt(process.argv[2])));
