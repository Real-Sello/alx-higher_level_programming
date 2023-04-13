#!/usr/bin/node
const Argv1 = process.argv[2];
const Argv2 = process.argv[3];
const firstInt = Number(Argv1);
const secondInt = Number(Argv2);

function add (a, b) {
  const addition = firstInt + secondInt;
  console.log(addition);
}

add(firstInt, secondInt);
