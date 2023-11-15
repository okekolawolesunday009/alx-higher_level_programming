#!/usr/bin/node
const argv = process.argv.slice(2);

const x = parseInt(argv[0]);
if (isNaN(x)) {
  console.log('Missing size');
  for (let i = 0; i < x; i++) {
	     console.log('X');
    for (let j = 0; j < i; i++) {
      console.log('\n');
    }
  }
}
