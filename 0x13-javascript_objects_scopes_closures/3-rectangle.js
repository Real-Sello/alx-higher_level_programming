#!/usr/bin/node
/*
a class Rectangle that defines a rectangle:

  -Using the class notation for defining our class
  -The constructor takes 2 arguments: w and h
  -Initialize the instance attribute width with the value of w
  -Initialize the instance attribute height with the value of h
  -If w or h is equal to 0 or not a positive integer, create an empty object
  -Create an instance method called print() that prints the rectangle using the character X
*/
class Rectangle {
  constructor (w, h) {
    if (!w || !h) {
      return;
    }
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const print = 'X';
    for (let rect = 0; rect < this.height; rect++) {
      console.log(print.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
