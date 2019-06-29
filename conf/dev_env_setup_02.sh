##### Install Source Code Pro Font #####
brew tap caskroom/fonts && brew cask install font-source-code-pro

##### Install zsh & oh-my-zsh theme #####
brew install zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

##### Install Fonts #####
# Install Source Code Pro Lite font
brew tap caskroom/fonts && brew cask install font-source-code-pro

# Install Powerline fonts
git clone https://github.com/powerline/fonts.git --depth=1
cd fonts
./install.sh
cd ..
rm -rf fonts

##### Install Powerlevel9k Theme #####
git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k

##### Install Necessary Programs #####
brew install ntfs-3g nvm tmux tree yarn sass
brew cask install atom font-source-code-pro iterm2 launchcontrol vagrant virtualbox vlc dbeaver-community gimp karabiner-elements osxfuse vagrant-manager visual-studio-code
