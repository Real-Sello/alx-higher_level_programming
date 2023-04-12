#!/usr/bin/node
const isNum = process.argv[2];
if (!isNaN(parseInt(isNum))) {
  console.log(`My number:${parseInt(isNum)}`);
} else {
  console.log('Not a number');
}
