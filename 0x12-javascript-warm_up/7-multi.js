#!/usr/bin/node
const  argv  = process.argv.slice(2);

var x = argv[1];

if (x === undefined) {
     return "Missing number of occurrences";
} else  {
     for (let i = 0; i < x; i++) {
         console.log("C is fun");
        }
}

