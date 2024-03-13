#!/usr/bin/node
// Creates a class Square that inherits from Rectangle
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  // prints the rectangle using the character c
  // If c is undefined, use the character X
  charPrint (c) {
    const character = c === undefined ? 'X' : 'C';
    for (let i = 0; i < this.width; i++) {
      let printout = '';
      for (let j = 0; j < this.height; j++) {
        printout += character;
      }
      console.log(printout);
    }
  }
}
module.exports = Square;
