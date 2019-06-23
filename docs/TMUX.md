# TMUX Commands


### Useful Commands
* Show Keyboard Shortcuts : `Prefix -> ?` and Search `CTRL + s`
* List Commands : `tmux list-commands` `tmux lscm`
* List Key Bindings : `tmux list-keys`
  - Key bindings for vi Copy mode : `tmux list-keys -t vi-copy`
* Show Messages : `Prefix -> ~`


### Session Related Commands
* List Sessions : `tmux list-sessions` `tmux ls`
* Create a new Session : `tmux new-session` `tmux new`
* Create a new Session with name `tmux new-session -s NAME`
* Rename Session : `tmux rename-session NAME`
* Attach Session : `tmux attach-session -t NAME`
* Detach Session : `Prefix -> d`

* Choose Session Interface : `Prefix -> s`
* Move to Next Session : `Prefix -> )`
* Move to Previous Session : `Prefix ->(`


### Window Related Commands
* Create a new Window : `Prefix -> c`
* Rename the current Window : `Prefix -> ,`
* Kill the current Window : `Prefix -> &`

* Choose Window Interface : `Prefix -> w`
* Move to Previous Window : `Prefix -> p`
* Move to Next Window : `Prefix -> n`
* Move to Last window : `Prefix -> l`
* Move to Window using number : `Prefix -> NUMBER` 

* Find Window Prompt : `Prefix -> f`


### Pane Related Commands
* Split the window Vertically : `Prefix -> \`
* Split the window Horizontally : `Prefix -> -`
* Change Panes Layout : `Prefix -> SPACE BAR`
* Resize Pane : `Prefix -> Meta + Arrow keys`
* Swap Panes Location : `Prefix -> { or }`

* Show Pane index number : `Prefix -> q` -> Press Number to move to the pane
* Move to Other Panes : `Prefix -> o`

* Kill the current Pane : `Prefix -> x`
* Zoom in/out the Pane : `Prefix -> z`


### Show Options
* View Global Options : `tmux show-options -g`
* View Window Options : `tmux show-options -w`
* View Server Options : `tmux show-options -s`


### TMUX Configurations
* Set Option : `tmux set-option OPTION PARAMS` `Prefix -> :set-option OPTION PARAMS`
* Configuration file : `~/.tmux.conf`
* Reload Configuration file : `tmux source-file ~/.tmux.conf`


### Window History
* Clear Window History : `tmux clear-history`


### Various TMUX Mode
* Default Mode : Similar to vi's insert mode
* Copy Mode : `Prefix -> [` 
  - Similar to vi's normal mode
* Command Mode : `Prefix -> :` -> Enter TMUX Commands

#### Copy Mode
* Switch to Copy Mode : `Prefix -> [`
  - Back to Default Mode : `q`
* Paste Buffer : `Prefix -> ]`
* Show Buffer List : `Prefix -> =`

##### Copy Mode Cursor Movements
* Moving Cursor(vi style) : Same as vi
  - Page Up : `CTRL + b`
  - Page Down : `CTRL + f`
  - To the Top : `g`
  - To the Bottom : `G`
* Search Up / Down : `?` / `/`
* Move to a Specific Line : `: -> LINE NUMBER`
* Select Text
  - Start Selection : `SPACE BAR`
  - End Selection : `ENTER`
  - Toggle Rectangular Selection: `v`
