#!/usr/bin/node

const square = parseInt(process.argv[2]);

if (isNaN(square)) {
  console.log('Missing size');
} else if (square > 0) {
  const row = 'X'.repeat(square);

  for (let i = 0; i < square; i++) {
    console.log(row);
  }
}
