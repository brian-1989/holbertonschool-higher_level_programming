#!/usr/bin/node
/* This script prints a square */
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const myNumber = process.argv[2];
  for (let i = 0; i < myNumber; i++) {
    for (let i = 0; i < myNumber; i++) {
      /* Function to remove line jumps */
      process.stdout.write('X');
    }
    console.log('');
  }
}
