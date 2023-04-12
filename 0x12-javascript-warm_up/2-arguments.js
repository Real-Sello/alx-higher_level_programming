#!/usr/bin/node
const argCount = process.argv;
if (argCount.length - 2 === 0) {
  console.log('No argument');
} else if (argCount.length - 2 === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
