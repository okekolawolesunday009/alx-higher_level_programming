#!/usr/bin/node
const { argv } = require('node:process');

const x = argv[0];
function factorial (x) {
  if (x < 0) {
    return NaN;
  } else if (isNaN(x) || (n == 0 || n == 1)) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
