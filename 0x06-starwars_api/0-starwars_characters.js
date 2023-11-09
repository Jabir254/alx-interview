#!/usr/local/bin/node

const request = require("request");

function getMovieCharacters(movieId) {
	const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

	request(filmUrl, (error, response, body) => {
		if (!error && response.statusCode === 200) {
			const filmData = JSON.parse(body);
			const charactersUrls = filmData.characters;

			charactersUrls.forEach((characterUrl) => {
				request(characterUrl, (error, response, body) => {
					if (!error && response.statusCode === 200) {
						const characterData = JSON.parse(body);
						console.log(characterData.name);
					} else {
						console.error(
							`Failed to fetch character data for ${characterUrl}`
						);
					}
				});
			});
		} else {
			console.error(`Failed to fetch movie data for ID: ${movieId}`);
		}
	});
}

// Usage: Pass the movie ID as an argument
const movieId = process.argv[2];
if (!movieId) {
	console.log("Please provide the Movie ID as a command-line argument.");
} else {
	getMovieCharacters(movieId);
}
