#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12,
  incr: function () {
    this.value++;
  }
};

console.log({type: 'object', value: 12});
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
