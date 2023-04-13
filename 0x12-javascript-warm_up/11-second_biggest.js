#!/usr/bin/node
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
