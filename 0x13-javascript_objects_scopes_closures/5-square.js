#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    // Pass the one side of the Rectangle to create the Square
    super(size, size);
  }
}

module.exports = Square;
