#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      this.height = undefined;
      this.width = undefined;
    } else {
      this.height = h;
      this.width = w;
    }
  }
};
