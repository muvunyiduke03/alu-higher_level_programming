#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    const data = JSON.parse(body);
    let count = 0;

    data.results.forEach(film => {
      if (
        film.characters.some(characterUrl => characterUrl.endsWith('/18/'))
      ) {
        count++;
      }
    });

    console.log(count);
  } catch (err) {
    console.error(err);
  }
});
