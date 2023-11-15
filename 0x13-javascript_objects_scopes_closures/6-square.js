#!/usr/bin/node

const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
};
