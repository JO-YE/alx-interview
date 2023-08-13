#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

// Importing the 'request' module
const request = require('request');

/* checking if the correct number of arguments is provided */
if (process.argv.length !== 3) {
  console.error('Kindly provide your movie ID');
  process.exit(1);
}

/* Extracting the Movie ID from command line arguments */
const movieId = process.argv[2];

/* Constructing the URL for the movie's API endpoint */
const url = `https://swapi.dev/api/films/${movieId}/`;

/* Performing the request to the movie's API endpoint */
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('API Error:', body);
    return;
  }
  /* Parsing  the JSON response */
  const movieData = JSON.parse(body);

  // Fetching and displaying character names
  const characters = movieData.characters;

/* Function to fetch and display character names */
  characters.forEach((characterUrl) => {
    request(characterUrl, (characterError, characterResponse, characterBody) => {
      if (characterError) {
        console.error('Error:', characterError.message);
        return;
      }

      if (characterResponse.statusCode !== 200) {
        console.error(`API request failed with status: ${characterResponse.statusCode}`);
        return;
      }

      const characterData = JSON.parse(characterBody);
      console.log(characterData.name);
    });
  });
});
