const request = require('request');

const API_URI = 'https://api.darksky.net/forecast';
const API_KEY = '6f1abfd47f4df2fec6297a543dd99098';

const getWeather = (latitude, longitude, callback) => {
  request({
    url: `${API_URI}/${API_KEY}/${latitude},${longitude}`,
    json: true
  }, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      callback(undefined, {
        temperature: body.currently.temperature,
        apparentTemperature: body.currently.apparentTemperature
      });
    } else {
      callback('Unable to fetch weather from Dark Sky API server.');
    }
  });
};

module.exports.getWeather = getWeather;
