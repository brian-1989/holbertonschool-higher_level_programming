#!/usr/bin/node
/* This script define an class called rectangle, create a
constructor with 2 arguments and Initialize the instance attributes
and when w and h are zero or not a positive integer, create an empty object */
class Rectangle {
  constructor (w, h) {
    if (w > 0 & h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
