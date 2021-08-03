#!/usr/bin/node
/* This script create an class called square and inherits
from the rectangle class */
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
