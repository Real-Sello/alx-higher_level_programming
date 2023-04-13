#!/usr/bin/node
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
