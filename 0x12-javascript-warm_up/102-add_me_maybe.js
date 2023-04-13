#!/usr/bin/node
exports.addMeMaybe = function (increment, func) {
  func(++increment);
};
