#!/usr/bin/node

const arguments = Process.argv.length;

if (arguments <= 2) {
    console.log('No Argument');
}
else if (arguments === 3) {
    console.log('Argument found');
}
else {
    console.log('Arguments found');
}