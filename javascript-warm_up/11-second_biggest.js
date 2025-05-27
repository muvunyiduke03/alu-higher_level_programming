#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  const nums = [];
  for (let i = 0; i < args.length; i++) {
    nums.push(parseInt(args[i], 10));
  }

  const max = Math.max(...nums);
  const filtered = nums.filter((n) => n !== max);
  const secondMax = Math.max(...filtered);
  console.log(secondMax);
}
