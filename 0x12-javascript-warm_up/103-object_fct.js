#!/usr/bin/node
const myThing = {
  type: 'object',
  value: 12
};
console.log (myThing);

myThing.incr = function () {
  this.value++;
};

myThing.incr();
console.log(myThing);
myThing.incr();
console.log(myThing);
myThing.incr();
console.log(myThing);
