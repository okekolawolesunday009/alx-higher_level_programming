#!/usr/bin/node
const argv = process.argv.slice(2);

const x = argv[0];
if (isNaN(x)) {
  console.log('Mising size');
} else {
  for (let i = 0; i < x; i++) {
	     console.log('X');
    for (let j = 0; i < i; i++) {
      console.log('\n');
    }
  }
}
