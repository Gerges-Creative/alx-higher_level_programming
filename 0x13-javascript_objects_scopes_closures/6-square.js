#!/usr/bin/node

const Square0 = require('./5-square');

class Square extends Square0 {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let rec = '';
        for (let j = 0; j < this.width; j++) {
          rec += c;
        }
        console.log(rec);
      }
    }
  }
}

module.exports = Square;
