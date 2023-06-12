#!/usr/bin/node
/*
script that prints My number: <first argument converted in integer>
if the first argument can be converted to an integer:

    -If the argument can’t be converted to an integer, print “Not a number”
*/
const argument = process.argv[2];

const parsedNum = parseInt(argument);

if (isNaN(parsedNum)) {
  console.log('Not a number');
} else {
  console.log('My number:', parsedNum);
}
