# cv-ml-pipline based on Seldon Core, Docker, Image Processing by python and OpenCV

1. Docker on MacOS
2. Dockerfile
3. pip3 install --user -r requirements.txt
4. python class

# https://www.youtube.com/tiziran

- The Missing Package Manager for macOS (or Linux)
  - https://brew.sh
  - /usr/bin/ruby -e "\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
- brew install git
- brew cask install keycastr
- https://www.spectacleapp.com

# Python

- brew install python
- echo "alias python=/usr/local/bin/python3.7" >> ~/.zshrc
- brew install git
- Poetry: Dependency Management for Python
  - https://github.com/python-poetry/poetry
  - curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
- Simple Python Version Management: pyenv
  - brew update
  - brew install pyenv
- A framework for managing and maintaining multi-language pre-commit hooks.
  - pip3 install pre-commit

# IDE

- Visual code
  - Bracket Pair Colorizer 2
  - Prettier - Code formatter
  - indent-rainbow
  - GitHub
  - Shell

# Terminal and Code

1. Terminal
   - iTerm2
     - https://iterm2.com/downloads.html
     - themes
       - Oh My Zsh
         - sh -c "\$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
       - Prezto,
         - git clone --recursive https://github.com/sorin-ionescu/prezto.git "${ZDOTDIR:-$HOME}/.zprezto"
         - source "${ZDOTDIR:-$HOME}/.zprezto/init.zsh"
         - zstyle ':prezto:load' pmodule-dirs \$HOME/.zprezto-contrib
       - pip install --user powerline-status
       - Spaceship-prompt
         - git clone https://github.com/denysdovhan/spaceship-prompt.git "\$ZSH_CUSTOM/themes/spaceship-prompt"
         - ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"
         - prezto
           - nano ~/.zpreztorc
           - Follow prezto-contrib#usage to clone prezto-contrib to the proper location.
             - zstyle ':prezto:load' pmodule-dirs \$HOME/.zprezto-contrib
             - cd \$ZPREZTODIR
             - git clone --recurse-submodules https://github.com/belak/prezto-contrib contrib
           - Enable the contrib-prompt module (before the prompt module).
           - Set zstyle ':prezto:module:prompt' theme 'spaceship' in your .zpreztorc.
       - Plugins
         - Pipeline
           - Brew install pipeline
         - Fzf: A command-line fuzzy finder
           - https://github.com/junegunn/fzf
           - brew install fzf
         - Simplified and community-driven man pages
           - brew install tldr
         - rg — recursively search current directory for lines matching a pattern
           - brew install ripgrep
           - https://github.com/BurntSushi/ripgrep
         - Bat
           - brew install bat
