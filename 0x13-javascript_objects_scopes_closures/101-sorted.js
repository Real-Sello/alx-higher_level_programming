#!/usr/bin/node
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
