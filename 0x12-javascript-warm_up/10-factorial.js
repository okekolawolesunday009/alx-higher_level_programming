#!/usr/bin/node
const  argv  = process.argv.slice(2);

const x = argv[0];
function factorial (x) {
  if (isNaN(x) || (x == 0 || x == 1)) {
    return console.log(1);
  } else {
    return console.log(x * factorial(x - 1));
  }
}
factorial(x)
