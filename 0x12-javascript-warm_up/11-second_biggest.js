#!/usr/bin/node
/* This script that searches the second biggest integer in the list of arguments. */
const myArray = [];
let lengthMyArray = process.argv.length;
if (isNaN(parseInt(process.argv[2])) || lengthMyArray === 3) {
  console.log(0);
} else {
  for (let i = 2; process.argv[i]; i++) {
    myArray.push(process.argv[i]);
  }
  myArray.sort(function (a, b) { return a - b; });
  lengthMyArray = myArray.length;
  console.log(myArray[lengthMyArray - 2]);
}
