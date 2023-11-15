#!/usr/bin/node

module.exports  = class Rectangle {
    constructor(h, w) {
      if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
        this.width = undefined;
        this.height = undefined;
      } else {
        this.height = h;
        this.width = w;

      }
     
    }
    print() {
      for (let i = 0; i < this.width; i++) {
        console.log('X'.repeat(this.height));
      }
    }
}
