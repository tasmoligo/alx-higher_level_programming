#!/usr/bin/node
// creates a Rectangle class
class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0) {
      new Rectangle;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
