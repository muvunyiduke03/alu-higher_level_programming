#!/usr/bin/node

const arguments = Process.argv.length;

if (arguments === 0) {
    console.log('No Argument');
}
else if (arguments === 1) {
    console.log('Argument found');
}
else {
    console.log('Arguments found');
}