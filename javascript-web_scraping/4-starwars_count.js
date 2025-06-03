#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const wedgeUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const data = JSON.parse(body);
  let count = 0;

  for (const film of data.results) {
    if (film.characters.includes(wedgeUrl)) {
      count++;
    }
  }

  console.log(count);
});