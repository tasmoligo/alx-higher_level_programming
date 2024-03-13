#!/usr/bin/node
// imports an array and computes a new array.
const oldList = require('./100-data').list;
const newArray = oldList.map((i, j) => i * j);
console.log(oldList);
console.log(newArray);
