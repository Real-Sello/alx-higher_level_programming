#!/usr/bin/node
const [argCount] = process.argv.slice(2);
if (!argCount) {
  console.log('No argument');
} else {
  console.log(argCount);
}
