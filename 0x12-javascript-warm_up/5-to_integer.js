#!/usr/bin/node
const argv = process.argv.slice(2);

if (isNaN(argv[0]) || argv[0] === undefined) {
     console.log('Not a number');
} else {
     console.log(`My number: ${argv[0]}`); 
}
