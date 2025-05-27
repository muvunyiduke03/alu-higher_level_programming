#!/usr/bin/node

const { dict } = require('./101-data');

const newDict = {};

for (const [userId, occ] of Object.entries(dict)) {
  if (!newDict[occ]) {
    newDict[occ] = [];
  }
  newDict[occ].push(userId);
}

console.log(newDict);
