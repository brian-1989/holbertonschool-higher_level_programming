#!/usr/bin/node
/* This script create an instance method called charPrint(c)
that prints the rectangle using the character c */
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        for (let i = 0; i < this.width; i++) {
          process.stdout.write('C');
        }
        console.log('');
      }
    }
  }
}
module.exports = Square;
