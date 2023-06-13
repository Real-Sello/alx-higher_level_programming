#!/usr/bin/node
/*
a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:

  -Using the class notation for defining our class and extends
  -The constructor takes 1 argument: size
  -The constructor of Rectangle is called (by using super())
*/
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
