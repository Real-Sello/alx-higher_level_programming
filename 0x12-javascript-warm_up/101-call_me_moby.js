#!/usr/bin/node
exports.callMeMoby = function (x, func) {
  for (let times = 0; times < x; times++) {
    func();
  }
};
