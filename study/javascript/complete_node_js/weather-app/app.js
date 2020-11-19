const yargs = require('yargs');
const axios = require('axios');

const GEOCODE_API_URI = 'https://maps.googleapis.com/maps/api/geocode/json';
const GEOCODE_API_KEY = 'AIzaSyAPd2_Fm9LDwTTC3oVcV8eZ9nIj6Nh4aVE';

const WEATHER_API_URI = 'https://api.darksky.net/forecast';
const WEATHER_API_KEY = '6f1abfd47f4df2fec6297a543dd99098';

const argv = yargs
  .options({
    address: {
      demand: true,
      alias: 'a',
      describe: 'Address to fetch weather for',
      string: true
    }
  })
  .help()
  .alias('help', 'h')
  .argv;


const encodedAddress = encodeURIComponent(argv.address);
const geocodeUrl = `${GEOCODE_API_URI}?address=${encodedAddress}&key=${GEOCODE_API_KEY}`

axios.get(geocodeUrl).then(response => {
  if (response.data.status === 'ZERO_RESULTS') {
    throw new Error('Unable to find that address.');
  }

  const latitude = response.data.results[0].geometry.location.lat;
  const longitude = response.data.results[0].geometry.location.lng;
  const weatherUrl = `${WEATHER_API_URI}/${WEATHER_API_KEY}/${latitude},${longitude}`;
  console.log(response.data.results[0].formatted_address);

  return axios.get(weatherUrl);

}).then(response => {
  const temperature = response.data.currently.temperature;
  const apparentTemperature = response.data.currently.apparentTemperature;
  console.log(temperature, apparentTemperature);

}).catch(error => {
  if (error.code === 'ENOTFOUND') {
    console.log('Unable to connect to API Server');
  } else {
    console.log(error.message);
  }

});
