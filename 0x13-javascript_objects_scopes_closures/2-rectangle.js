#!/usr/bin/node
/*
a class Rectangle that defines a rectangle:

  -Using the class notation for defining our class
  -The constructor takes 2 arguments w and h
  -Initializes the instance attribute width with the value of w
  -Initializes the instance attribute height with the value of h
  -If w or h is equal to 0 or not a positive integer, create an empty object
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
}
module.exports = Rectangle;
