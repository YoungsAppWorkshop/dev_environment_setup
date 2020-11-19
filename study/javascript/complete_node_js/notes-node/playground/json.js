// let obj = {
//   name: 'Young',
// };
//
// let stringObj = JSON.stringify(obj);
// console.log(typeof stringObj);
// console.log(stringObj);

// let personString = '{"name": "Young", "age": 25}';
// let person = JSON.parse(personString);
// console.log(typeof person);
// console.log(person);

const fs = require('fs');
let originalNote = {
  title: 'Some title',
  body: 'Some body'
};
const originalNoteString = JSON.stringify(originalNote);
fs.writeFileSync('notes.json', originalNoteString);

const noteString = fs.readFileSync('notes.json');
// note
const note = JSON.parse(noteString);
console.log(note.title);
