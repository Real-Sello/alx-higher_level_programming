#!/usr/bin/node
/*
a script that imports an array and computes a new array:
    -list is imported from the file 100-data.js
    -Map must be used
    -A new list must be created with each value equal to the value of the
        initial list, multipled by the index in the list
    -Print both the initial list and the new list
*/
const importedList = require('./100-data');

const listValue = importedList.list;
const newList = listValue.map((value, index) => value * index);

console.log(listValue);
console.log(newList);
