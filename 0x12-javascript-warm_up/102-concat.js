#!/usr/bin/node
/* This script that concats 2 files, handing of file */
let fileOpen1 = process.argv[2];
let fileOPen2 = process.argv[3];
let fileCreate = process.argv[4];
const fs = require('fs');
fs.readFile(fileOpen1, 'utf-8', (error1, file1) => {
  fs.readFile(fileOPen2, 'utf-8', (error2, file2) => {
    fs.writeFile(fileCreate, file1 + file2, () => {});});});
