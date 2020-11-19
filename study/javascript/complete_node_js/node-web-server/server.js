const express = require('express');
const hbs = require('hbs');
const fs = require('fs');

let app = express();

hbs.registerPartials(__dirname + '/views/partials');
app.set('view engine', 'hbs');

app.use((req, res, next) => {
  const now = new Date().toString();
  const log = `${now}: ${req.method} ${req.url}`;
  console.log(log);
  fs.appendFile('server.log', log + '\n', err => {
    if (err) {
      console.log('Unable to append to server.log.');
    }
  })
  next();
});

// When the website is on maintenance
app.use((req, res, next) => {
  res.render('maintenance.hbs');
});

// Static middleware should be below the maintenance middleware
// to prevent resources from public folder being rendered
app.use(express.static(__dirname + '/public'));

hbs.registerHelper('getCurrentYear', () => {
  return new Date().getFullYear();
});
hbs.registerHelper('screamIt', text => {
  return text.toUpperCase();
});

app.get('/', (req, res) => {
  // res.send('<h1>Hello, Express!</h1>');
  // res.send({
  //   name: 'Young',
  //   likes: [
  //     'Biking',
  //     'Cities'
  //   ]
  // })
  res.render('home.hbs', {
    pageTitle: 'Home Page',
    welcomeMessage: 'hello, world!'
  });
});

app.get('/about', (req, res) => {
  res.render('about.hbs', {
    pageTitle: 'About Page',
  });
});


// /bad - send back json with errorMessage
app.get('/bad', (req, res) => {
  // res.send('<h1>Hello, Express!</h1>');
  res.send({errorMessage: 'Something went wrong'});
});

app.listen(3000, () => {
  console.log('Server is up on port 3000');
});
