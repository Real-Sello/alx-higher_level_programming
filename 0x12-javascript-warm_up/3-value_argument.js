#!/usr/bin/node
/*
script that prints the first argument passed to it:

    -If no arguments are passed to the script, print “No argument”
*/
const [argCount] = process.argv.slice(2);
if (!argCount) {
  console.log('No argument');
} else {
  console.log(argCount);
}
