#!/usr/bin/env node

const argument = Process.argv.length;

if (argument <= 2) {
    console.log('No argument');
}
else if (argument === 3) {
    console.log('Argument found');
}
else {
    console.log('Arguments found');
}
