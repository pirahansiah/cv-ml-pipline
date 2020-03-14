# IDE & Terminal on Mac

- Visual code
  - Bracket Pair Colorizer 2
  - Prettier - Code formatter
  - indent-rainbow
  - GitHub
  - Shell

bpython https://bpython-interpreter.org/downloads.html
pip install bpython

Terminal
_ iTerm2
_ https://iterm2.com/downloads.html
_ themes  
 _ Oh My Zsh
_ sh -c "\$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
_ Prezto,
_ git clone --recursive https://github.com/sorin-ionescu/prezto.git "${ZDOTDIR:-$HOME}/.zprezto"
_ source "${ZDOTDIR:-$HOME}/.zprezto/init.zsh"
_ zstyle ':prezto:load' pmodule-dirs \$HOME/.zprezto-contrib
_ pip install --user powerline-status
_ Spaceship-prompt
_ git clone https://github.com/denysdovhan/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt"
                * ln -s "$ZSH\*CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "\$ZSH_CUSTOM/themes/spaceship.zsh-theme"

- prezto
  _ nano ~/.zpreztorc
  _ Follow prezto-contrib#usage to clone prezto-contrib to the proper location. \* zstyle ':prezto:load' pmodule-dirs \$HOME/.zprezto-contrib

* cd \$ZPREZTODIR
  _ git clone --recurse-submodules https://github.com/belak/prezto-contrib contrib
  _ Enable the contrib-prompt module (before the prompt module).
  _ Set zstyle ':prezto:module:prompt' theme 'spaceship' in your .zpreztorc.
  _ Plugins
  _ Pipeline
  Brew install pipeline
  Fzf: A command-line fuzzy finder
  _ https://github.com/junegunn/fzf
  _ brew install fzf
  _ Simplified and community-driven man pages
  _ brew install tldr
  _ rg — recursively search current directory for lines matching a pattern
  _ brew install ripgrep
  _ https://github.com/BurntSushi/ripgrep
  \_ Bat \* brew install bat

# Tools

## Pyenv

### Install

```
brew install pyenv
```

vim ~/.zshrc  
eval "\$(pyenv init -)"

### commands

## poetry

### Install

https://blog.jayway.com/2019/12/28/pyenv-poetry-saviours-in-the-python-chaos/

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

poetry config virtualenvs.in-project true

source $HOME/.poetry/env

poetry init
poetry new poetry_projcet
poetry run python test.py

```

### commands

```
poetry new "name of projces"
poetry install
poetry run which python
poetry add `cat requirements.txt`

```

https://python-poetry.org/

##

### Install

```

```

### commands

```

```

##

### Install

```

```

### commands

```

```

# cv-ml-pipline

# Computer Vision with Machine Learning Pipline: Docker, AWS, Kubernetes, TensorFlow, Seldon, Kubeflow, ...

Command + Shift + P
Shell Command : Install code in PATH
code .

Config GitHub: https://github.com 1. ssh-keygen -t rsa -b 4096 -C "your_email@example.com" 2. pbcopy < ~/.ssh/id_rsa.pub 3. GitHub->Personal Setting->SSH and GPG keys->Add new : past 4. ssh-add ~/.ssh/id_rsa_work_user1 5. ~/.ssh/config

1: install docker : https://docs.docker.com/docker-for-mac/install/
docker run
Docker file: -> Docker image: package, template, planet
Docker container:

3: install the requirements.txt

# cv-ml-pipline Feb 2020 develop

Computer Vision with Machine Learning Pipline: Docker, AWS, Kubernetes, TensorFlow, Seldon, Kubeflow, ...

Command + Shift + P
Shell Command : Install code in PATH
code .
