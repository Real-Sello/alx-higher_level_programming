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

  rotate () {
    const swap = this.width;
    this.width = this.height;
    this.height = swap;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
