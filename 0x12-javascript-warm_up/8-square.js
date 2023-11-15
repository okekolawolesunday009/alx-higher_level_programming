#!/usr/bin/node
const argv = process.argv.slice(2);

const x = parseInt(argv[0]);
if (isNaN(x)) {
  console.log('Missing size');
} else {
	 for(let i = 0; i <x; i++){
           console.log('x');
	for(let j = 1; j <= i; j++){
           console.log('\n');
	}
	 }
}
