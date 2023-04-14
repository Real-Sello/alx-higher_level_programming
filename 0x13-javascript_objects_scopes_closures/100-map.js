#!/usr/bin/node
const importedList = require('./100-data');

const listValue = importedList.list;
const newList = listValue.map((value, index) => value * index);

console.log(listValue);
console.log(newList);
