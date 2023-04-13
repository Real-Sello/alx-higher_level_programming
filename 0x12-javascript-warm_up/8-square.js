#!/usr/bin/node
const arg = [];
const { argv } = require('process');
const square = 'X';
let xSquare;
argv.forEach((val, index) => {
  arg[index] = `${val}`;
});
const times = Number(`${arg[2]}`);
if (isNaN(times)) {
  console.log('Missing size');
} else {
  for (xSquare = 0; xSquare < times; xSquare++) {
    console.log(square.repeat(times));
  }
}
