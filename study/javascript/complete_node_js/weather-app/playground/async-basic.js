console.log('Starting app');

setTimeout(() => {
  console.log('First setTimeout callback 2000');
}, 2000);

setTimeout(() => {
  console.log('Second setTimeout callback 0');
}, 0);

console.log('Finishing app');
