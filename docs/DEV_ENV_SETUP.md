# Development Environment Setup


### MacOS Setup Guide
1. Follow the Instruction:
  * Link: [MacOS Setup Guide](https://sourabhbajaj.com/mac-setup/)

2. Check List:
  * **DO NOT REMOVE** workspace auto-switching (System Preferences > Dock)
  * Export PATH for Homebrew: `export PATH="/usr/local/bin:$PATH"`


### iTerm2 Setup
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


### Zsh Setup

1. Install Zsh
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


### Change Keybinding for toggling Korean/English Keyboard
1. Install [Karabiner](https://pqrs.org/osx/karabiner/)
```
brew cask install karabiner-elements
```

2. 응용 프로그램에서 Karabiner Elements를 실행한 후, Simple Modifications를 선택합니다. 아래쪽에 Add item 버튼을 클릭한 후 From key는 right_command를 선택, To key는 f18을 선택합니다. 이렇게 설정되면 오른쪽 command키를 눌렀을 때 f18키를 누른 것과 동일합니다.

3. 시스템 환경설정 > 키보드 > 단축키탭에서 입력소스를 선택한 다음, 이전 입력 소스 선택의 단축키를 오른쪽 command로 변경합니다. (오른쪽 command키를 누르면 F18키가 할당됩니다.)

4. 참고자료: [블로그 포스트](https://godoftyping.wordpress.com/2018/04/09/mac-%EB%A7%A5%EC%97%90%EC%84%9C-%ED%95%9C%EC%98%81%EC%A0%84%ED%99%98%ED%95%98%EB%8A%94-%EB%8B%A4%EC%96%91%ED%95%9C-%EB%B0%A9%EB%B2%95%EB%93%A4/)
