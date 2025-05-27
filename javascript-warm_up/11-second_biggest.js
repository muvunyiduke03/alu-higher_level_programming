#!/usr/bin/node
const arguments = process.argv.slice(2).map((arguments) => parseInt(arguments, 10));

if (arguments.length < 2) {
  console.log(0);
} else {
  const max = Math.max(...arguments);
  const filtered = arguments.filter(n => n !== max);
  const secondMax = Math.max(...filtered);
  console.log(secondMax);
}
