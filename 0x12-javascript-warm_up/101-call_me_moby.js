#!/usr/bin/node
/*
script containing a function that executes x times a function.

  -The function is visible from outside
  -Prototype: function (x, theFunction)
*/
exports.callMeMoby = function (x, func) {
  for (let times = 0; times < x; times++) {
    func();
  }
};
