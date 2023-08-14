#!/usr/bin/node
/*
script that computes and prints a factorial

  -The first argument is integer (argument can be cast as integer)
   used for computing the factorial
  -Factorial of NaN is 1
*/
const arg = [];
function factorial (n) {
  if (isNaN(n)) {
    return (1);
  } else if (n === 1) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}
process.argv.forEach((val, index) => {
  arg[index] = `${val}`;
});
const fact = factorial(arg[2]);
console.log(fact);
