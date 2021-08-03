#!/usr/bin/node
/* This script prints x times “C is fun” */
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const myNumber = parseInt(process.argv[2]);
  for (let i = 0; i < myNumber; i++) {
    console.log('C is fun');
  }
}
