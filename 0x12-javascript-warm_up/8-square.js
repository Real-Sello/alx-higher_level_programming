#!/usr/bin/node
/*
script that prints a square

  -The first argument is the size of the square
  -If the first argument can’t be converted to an integer,
  print “Missing size”
  -You must use the character X to print the square
*/
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
