#!/usr/bin/node
/*
script that searches the second biggest integer in the list of arguments.

  -It can be assumed all arguments can be converted to integer
  -If no argument passed, print 0
  -If the number of arguments is 1, print 0
*/
const arg = process.argv;
const secondBig = [];
arg.forEach((val, index) => {
  secondBig[index] = `${val}`;
});
if (secondBig.length <= 3) {
  console.log('0');
} else {
  secondBig.sort(function (a, b) { return a - b; });
  console.log(secondBig[secondBig.length - 2]);
}
