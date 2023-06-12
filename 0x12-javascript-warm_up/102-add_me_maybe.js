#!/usr/bin/node
/*
script containing a function that increments and calls a function.

  -The function is visible from outside
  -Prototype: function (number, theFunction)
*/
exports.addMeMaybe = function (increment, func) {
  func(++increment);
};
