#!/usr/bin/node
/*
script that prints x times “C is fun”

  -Where x is the first argument of the script
  -If the first argument can’t be converted to
  an integer, print “Missing number of occurrences”
*/
let x;
const arg = [];
process.argv.forEach((val, index) => {
  arg[index] = `${val}`;
});
const times = Number(`${arg[2]}`);
if (isNaN(times)) {
  console.log('Missing number of occurrences');
} else {
  for (x = 0; x < times; x++) {
    console.log('C is fun');
  }
}
