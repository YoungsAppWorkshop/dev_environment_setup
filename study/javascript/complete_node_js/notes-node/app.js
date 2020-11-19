const fs = require('fs');
const _ = require('lodash');
const yargs = require('yargs');

const notes = require('./notes.js');
const yargsOptions = {
  title: {
    describe: 'Title of note',
    demand: true,
    alias: 't'
  },
  body: {
    describe: 'Body of note',
    demand: true,
    alias: 'b'
  }
};

const argv = yargs
  .command('add', 'Add a new note', yargsOptions)
  .command('list', 'List all notes')
  .command('read', 'Read a note', yargsOptions)
  .command('remove', 'Remove a note', {
    title: yargsOptions.title
  })
  .help()
  .argv;

const command = argv._[0];
console.log('Command:', command);
// console.log('Process:', process.argv);
console.log('Yargs:', argv);
console.log();

switch(command) {
  case 'add':
    const newNote = notes.addNote(argv.title, argv.body);
    console.log(newNote ? `Note titled ${newNote.title} is added.` : `Title is duplicated.`);
    break;

  case 'list':
    console.log(notes.getAll());
    break;

  case 'read':
    debugger;
    console.log(notes.getNote(argv.title));
    break;

  case 'remove':
    const isNoteRemoved = notes.removeNote(argv.title);
    console.log(isNoteRemoved ? 'Note was removed' : 'Note Not Found');
    break;

  default:
    console.log('Command not recognized.');
}
