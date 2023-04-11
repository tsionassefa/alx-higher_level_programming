#!/usr/bin/node
const lil = require('./100-data.js').lil;
console.log(lil);
console.log(lil.map((item, index) => item * index))
