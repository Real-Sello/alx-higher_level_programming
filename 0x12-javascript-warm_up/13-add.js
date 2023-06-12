#!/usr/bin/node
/*
script contains a function that returns the addition of 2 integers.

  -The function is visible from outside
  -The name of the function is add
*/
exports.add = function (number1, number2) {
  const myAddition = number1 + number2;
  return (myAddition);
};
