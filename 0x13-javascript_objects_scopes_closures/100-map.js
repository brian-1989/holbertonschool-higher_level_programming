#!/usr/bin/node
/* This script imports an array and computes a new array */
const array = require('./100-data').list;
let i = 0;
const map1 = array.map(a => a * i++);
console.log(array);
console.log(map1);
