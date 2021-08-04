#!/usr/bin/node
/* This script create an instance method called charPrint(c)
that prints the rectangle using the character c */
const Square1 = require('./5-square');
class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        for (let i = 0; i < this.width; i++) {
          process.stdout.write(c);
        }
        console.log('');
      }
    }
  }
}
module.exports = Square;
