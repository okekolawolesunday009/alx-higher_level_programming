#!/usr/bin/node
const  argv  =  process.argv.slice(2);

if (argv[0] === undefined) {
     console.log("No argument");
} else if (argv.length === 1) {
     console.log("Argument found");
} else if (argv.length > 1) {
	console.log("Arguments found");
}
