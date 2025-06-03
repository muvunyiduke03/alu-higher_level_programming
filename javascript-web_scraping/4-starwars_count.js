#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const wedgeUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    const data = JSON.parse(body);
    const film = data.results || [];
    let count = 0;

    for (const film of films) {
      if (film.characters.find(url => url === wedgeUrl || url.endsWith('/18/'))) {
        count++;
      }
    }

    console.log(count);
  } catch (err) {
    console.error(err);
  }
});
