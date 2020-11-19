const fs = require('fs');

const fetchNotes = () => {
  try {
    return JSON.parse(fs.readFileSync('notes-data.json'));
  } catch (e) {
    return [];
  }
};

const saveNotes = notes => {
  fs.writeFileSync('notes-data.json', JSON.stringify(notes));
};

const addNote = (title, body) => {
  let notes = fetchNotes();
  let note = {
    title,
    body
  };
  const isTitleDuplicated = notes.filter(note => note.title === title).length > 0;

  if ( !isTitleDuplicated ) {
    notes.push(note);
    saveNotes(notes);
    return note;
  }
};

const getAll = () => fetchNotes();

const getNote = title => {
  const notes = fetchNotes();
  return notes.filter(note => note.title === title);
};

const removeNote = title => {
  const notes = fetchNotes();
  const filteredNotes = notes.filter(note => note.title !== title);

  saveNotes(filteredNotes);
  return notes.length !== filteredNotes.length
};

module.exports = {
  addNote,
  getAll,
  getNote,
  removeNote
};
