#!/usr/bin/bash
const dict = require('./101-data');

const newDict = {};
for (const userId in dict) {
  const occurrence = dict[userId];
  if (newDict[occurrence] === undefined) {
    newDict[occurrence] = [userId];
  } else {
    newDict[occurrence].push(userId);
  }
}

console.log(newDict);
