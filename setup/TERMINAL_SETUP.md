# Terminal Setup Process for Mac

### Install & Configure iTerm2

1. Install iTerm2
```
brew cask install iterm2
```

2. Colors Presets

* Not necessary for Solarized Light/Dark presets
* Download one of [iTerm2 color schemes](https://github.com/mbadolato/iTerm2-Color-Schemes/tree/master/schemes) and then set these to your default profile colors
```
git clone https://github.com/mbadolato/iTerm2-Color-Schemes
```

3. Font Settings
* Change the font to 14pt Source Code Pro Lite. Source Code Pro can be downloaded using Homebrew
```
brew tap caskroom/fonts && brew cask install font-source-code-pro
```

4. Others
* https://sourabhbajaj.com/mac-setup/iTerm/



### Install & Configure Zsh

1. Install Zsh
* Install
```
brew install zsh
```


2. Install [Oh My Zsh](https://github.com/robbyrussell/oh-my-zsh)
```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

3. Plugins
```
plugins=(git colored-man colorize pip python brew osx zsh-syntax-highlighting)
```

4. Themes
* Install [Powerline fonts](https://github.com/powerline/fonts)
```
# clone
git clone https://github.com/powerline/fonts.git --depth=1
# install
cd fonts
./install.sh
# clean-up a bit
cd ..
rm -rf fonts
```

* Custom Theme: Powerlevel9k
```
git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k
```

* Select Theme
```
ZSH_THEME="agnoster" # or ZSH_THEME="powerlevel9k/powerlevel9k"
```
