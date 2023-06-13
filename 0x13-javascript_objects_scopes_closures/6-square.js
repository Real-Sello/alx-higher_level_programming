#!/usr/bin/node
/*
a class Square that defines a square and inherits from Square of 5-square.js:

  -Using the class notation for defining our class and extends
  -Create an instance method called charPrint(c) that prints the
    rectangle using the character c
  -If c is undefined, use the character X
*/
const Sqr = require('./5-square');

class Square extends Sqr {
  charPrint (c) {
    const Print = 'X';
    if (!c) {
      for (let i = 0; i < this.width; i++) {
        console.log(Print.repeat(this.height));
      }
    } else {
      for (let j = 0; j < this.width; j++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
