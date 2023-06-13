#!/usr/bin/node
/*
a script that imports a dictionary of occurrences by user id and computes
a dictionary of user ids by occurrence.

  -The script imports dict from the file 101-data.js
  -In the new dictionary:
    -A key is a number of occurrences
    -A value is the list of user ids
  -Print the new dictionary at the end
*/
const importedDict = require('./101-data');
const dictValue = importedDict.dict;

const newDict = {};
for (const userId in dictValue) {
  if (newDict[dictValue[userId]] === undefined) {
    newDict[dictValue[userId]] = [];
  }
  newDict[dictValue[userId]].push(userId);
}

console.log(newDict);
