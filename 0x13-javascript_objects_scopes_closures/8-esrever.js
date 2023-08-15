#!/usr/bin/node
/*
a function that returns the reversed version of a list:
  -Prototype: exports.esrever = function(list)
  -Built-in method reverse not allowed
*/
exports.esrever = function (list) {
  const newList = [];
  while (list.length) {
    newList.push(list.pop());
  }
  return (newList);
};
