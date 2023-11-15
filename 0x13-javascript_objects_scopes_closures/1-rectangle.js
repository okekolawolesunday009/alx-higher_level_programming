#!/usr/bin/node

module.exports  = class Rectangle {
    constructor(h, w) {
      if (w <= 0 || h <= 0 || !isNaN(w) || isNaN(h)) {
        this.width = null;
        this.height = null;
      } else {
        this.height = h;
        this.width = w;

      }
    }
  }
