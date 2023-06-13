#!/usr/bin/node
/*
a script that concats 2 files.

    -The first argument is the file path of the first source file
    -The second argument is the file path of the second source file
    -The third argument is the file path of the destination
*/
const getFile = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destFile = process.argv[4];

const data1 = getFile.readFileSync(sourceFile1, 'utf8');
const data2 = getFile.readFileSync(sourceFile2, 'utf8');
const combinedData = data1 + data2;

getFile.writeFileSync(destFile, combinedData);
