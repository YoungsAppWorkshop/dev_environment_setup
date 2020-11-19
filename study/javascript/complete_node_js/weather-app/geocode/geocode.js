const request = require('request');

const API_URI = 'https://maps.googleapis.com/maps/api/geocode/json';
const API_KEY = 'AIzaSyAPd2_Fm9LDwTTC3oVcV8eZ9nIj6Nh4aVE';

const geocodeAddress = (address, callback) => {
  const encodedAddress = encodeURIComponent(address);
  request({
    url: `${API_URI}?address=${encodedAddress}&key=${API_KEY}`,
    json: true
  }, (error, response, body) => {

    // Beautify JSON response
    // console.log(JSON.stringify(body, undefined, 2));

    if ( error ) {
      callback('Unable to connect to Google servers.');
    } else if (body.status === 'ZERO_RESULTS') {
      callback('Unable to find that address.');
    } else {
      callback(undefined, {
        address: body.results[0].formatted_address,
        latitude: body.results[0].geometry.location.lat,
        longitude: body.results[0].geometry.location.lng
      });
    }
  });
};

module.exports.geocodeAddress = geocodeAddress;
