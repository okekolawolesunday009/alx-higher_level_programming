#!/usr/bin/node
/** readme */
const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

try {
	fs.writeFileSync(filePath, content, 'utf8');
} catch (err) {
	console.error(`Error writing to file: ${err.message}`);
}

