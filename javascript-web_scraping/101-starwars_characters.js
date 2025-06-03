#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./101-starwars_characters.js <movie_id>');
  process.exit(1);
}

const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(filmUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  try {
    const film = JSON.parse(body);
    const characters = film.characters;

    const fetchCharacter = (index) => {
      if (index >= characters.length) return;
      request(characters[index], (error, response, charBody) => {
        if (error) {
          console.error(error);
          return;
        }
        try {
          const character = JSON.parse(charBody);
          console.log(character.name);
          fetchCharacter(index + 1);
        } catch (e) {
          console.error(e);
        }
      });
    };

    fetchCharacter(0);
  } catch (parseError) {
    console.error(parseError);
  }
});
