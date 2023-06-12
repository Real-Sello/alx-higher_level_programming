#!/usr/bin/node
/*
Updated this script by adding a new function incr
 that increments the integer value
*/
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

/*
MY CODE BELOW
*/

myObject.incr = function () {
  this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
