# Terminal Commands



### History Tricks

* Sudo Previous Command: `sudo !!`


* Reverse-i-search: `CTRL + R`


* Execute the last command that matches the specified characters
  - `!characters`


* Review most oft-used UNIX commands
  - `history|awk '{print $2}'|awk 'BEGIN {FS="|"} {print $1}'|sort|uniq -c|sort -r`


* Caret substitution trick: substitute the previous command
```
$ cd mydriectory
bash: cd: mydriectory: No such file or directory
$ ^ri^ir
```


* Yield the second most recent command: `!-2`


* Select arguments with the colon
```
$ mv oldfilename newfilename
$ ls
$ more !-2:2
more newfilename
```
