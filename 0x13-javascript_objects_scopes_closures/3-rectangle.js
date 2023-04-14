#!/usr/bin/node
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
