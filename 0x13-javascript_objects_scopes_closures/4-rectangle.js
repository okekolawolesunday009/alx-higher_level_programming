#!/usr/bin/node

module.exports = class Rectangle {
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

    rotate() {
        for (let i = 0; i < this.height; i++) {
            console.log('X'.repeat(this.width));
          }

    }
    double() {
        for (let i = 0; i < this.width * 2; i++) {
            console.log('X'.repeat(this.heigth * 2));
          }

    }
}
