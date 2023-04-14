#!/usr/bin/node
exports.converter = function (base) {
  function convert (value) {
    return value.toString(base);
  }
  return (convert);
};
