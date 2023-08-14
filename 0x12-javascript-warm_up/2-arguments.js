#!/usr/bin/node
/*
script that prints a message depending of the number of arguments passed:

    -If no arguments are passed to the script, print “No argument”
    -If only one argument is passed to the script, print “Argument found”
    -Otherwise, print “Arguments found”
*/
const argCount = process.argv;
if (argCount.length - 2 === 0) {
  console.log('No argument');
} else if (argCount.length - 2 === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
