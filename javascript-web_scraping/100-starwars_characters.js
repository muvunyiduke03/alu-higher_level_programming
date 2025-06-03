#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./100-starwars_characters.js <movie_id>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  try {
    const movie = JSON.parse(body);
    const characters = movie.characters; // array of URLs

    let count = 0;
    const names = new Array(characters.length);

    characters.forEach((url, idx) => {
      request(url, (err, res, charBody) => {
        if (err) {
          console.error(err);
          return;
        }
        try {
          const character = JSON.parse(charBody);
          names[idx] = character.name;
          count++;

          if (count === characters.length) {
            names.forEach(name => console.log(name));
          }
        } catch (e) {
          console.error(e);
        }
      });
    });
  } catch (e) {
    console.error(e);
  }
});
