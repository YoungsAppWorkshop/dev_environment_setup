# VIM cheetsheat

## `.vimrc`
* Create `.vimrc` file to run Vim as non Vi-compatible mode


## Basic Commands

* Move cursor
  - Basic Movement: 	h(left), j(down), k(up), l(right)
  - Word Movement:	w, b
  - Start / End line:	^ or 0(start), $(end)
  - Move to specific line:	5G(move to line 5), G(move to end of file)
  - Show current line number/row:	CTRL-G
  - Scroll Up / Down:	CTRL-U / CTRL-D

* Insert
  - Character:		i(before), a(after), A(end of line)
  - New line:		o(after),	O(before)


* Undo/Redo:	u(undo), U(undo one line), CTRL-R(redo)

* Repeat the last change: .

* Getting Out: 	ZZ,	:q!


## Editing

* Change / Replace
  - cc: 	Change entire line
  - cw, c$
  - r{char}: 	Replace a character 
  - 5r{char}:	Replace 5 characters
  - ~:		Change case

* Copy / Yank
  - y:		Copy(Yank) a whole line
  - y'{mark}:	Copy texts between cursor and the mark

* Delete 
  - x:	delete a character
  - dd: delete a line	
  - de, dw, d3w,d$

* Put / Paste
  - p:	put characters

* Mark
  - m{a-z}:	Create a marker named {a-z}
  - '{a-z}:	Move to the marker
  - List markers
    - :marks :		List all markers
    - :marks args:	List a particular marker

* Join lines: 	J

* Insert Shell commands output
  - !!{shell_commands}	ex) !!ls
  - :.!{shell_commands}	ex) !!ls


## Searching

* Search
  - On Line:	f(forward) or t(til), F(backward), T(backward til)
  - Forward:	/{regex}, n(next), N(before)
  - Backward:	?{regex}, n(next), N(before)
  - History:	/{UP or DOWN}

* Basic Regex
  - ^:		Start of a line
  - $:		End of a line
  - .:		Any single character


## Handling Multiple files

* Edit Another File
  - :vi {file}	Open another file

* Open files
  - `$ vim file1 file2 file3`

* Move to the next file
  - :next	Move to the next file
  - :wnext	Write current file and move to the next file
  - :Next 	Move to the previous file
  - :previous 	Move to the previous file
  - :rewind	Move to the first file
  - :last	Move to the last file
  - {num}CTRL-6	Move to {num}th file

## Others

* Keyboard Macros
  - Register:	q{char(a~z)}	/ q(End recording)
  - Use:	@{char(a~z)}

* Diagraphs
  - List:	:diagraphs
  - Use:	On Insert Mode, CTRL-K{diagraph code}

* Help
  - :help, :help subject
  - CTRL-]:	Jump to tag
  - CTRL-T:	Pop tag

* Command mods
  - :set (no)number		Toggle line number
  - :set (no)hlsearch		Toggle search highlighting
  - :set (no)incsearch		Toggle incremental searches
  - :set (no)autowrite		Toggle auto write(save) option
