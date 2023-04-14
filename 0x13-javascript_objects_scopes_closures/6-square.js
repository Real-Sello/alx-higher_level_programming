#!/usr/bin/node
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
