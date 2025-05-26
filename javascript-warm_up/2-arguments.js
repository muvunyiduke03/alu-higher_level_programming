#!/usr/bin/node

const args = process.argv.length;

if (args < 1) {
    console.log('No argument');
}
else if (args === 1) {
    console.log('Argument found');
}
else {
    console.log('Argumnts found');
}