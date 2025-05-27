#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

// Attach an anonymous function to `incr`
myObject.incr = function () {
  this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
