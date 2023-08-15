#!/usr/bin/node
/*
a function that converts a number from a base 10 to another
base passed as argument:
  -Prototype: exports.converter = function(base)
  -No file should be imported
  -No new variable should be declared
*/
exports.converter = function (base) {
  function convert (value) {
    return value.toString(base);
  }
  return (convert);
};
