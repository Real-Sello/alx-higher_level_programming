#!/usr/bin/node
const argCount = process.argv;
if (argCount.length - 2 === 0) {
  console.log('No argument');
} else {
  console.log(argCount[2]);
}
