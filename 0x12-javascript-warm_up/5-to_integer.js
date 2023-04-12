#!/usr/bin/node
const isNum = process.argv[2];
if (isNum > 0) {
  console.log(`My number:${isNum}`);
} else {
  console.log('Not a number');
}
