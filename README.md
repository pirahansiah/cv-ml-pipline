# Computer Vision

Object Tracking in IoT


# Image Processing

Thresholding:
Binarization or thresholding is one problem that have to solve in pattern recognition methods and applications. Moreover, it has a very important influence on the sequent steps in computer vision applications such as, Optical Character Recognition (OCR), image segmentation, and tracking objects.

Binarization or thresholding is one problem that must be solved in pattern recognition and it has a very important influence on the sequent steps in imaging applications. Thresholding is used to separate objects from the background, and diminish the amount of data alter the computational speed. Recently, interest in multilevel thresholding has been altered. However, when the levels are altered, the computation time alters so single threshold methods are accelerated than multilevel methods. Moreover, for every new application, new methods are is acquired.

Thresholding is one of the critical steps in pattern recognition and has a significant effect on the upcoming steps of image application, the important objectives of thresholding are as follows, separating objects from background, decreasing the capacity of data consequently increases speed. Handwritten recognition is one of the important issues, which have various applications in mobile devices.

## Reference:

Using An Ant Colony Optimization Algorithm For Image Edge Detection As A Threshold Segmentation For OCR System Journal of Theoretical & Applied Information Technology, 95(21)
http://www.jatit.org/volumes/Vol95No21/1Vol95No21.pdf

GSFT-PSNR: Global Single Fuzzy Threshold Based on PSNR for OCR Systems, International Journal of Computer Science and Network Solutions 4(6)
https://www.ijcsns.com/June.2016-Volume.4-No.6/Article01.pdf

Adaptive Image Thresholding based On the Peak Signal-To-Noise Ratio, Research Journal of Applied Sciences, Engineering and Technology 8(9).
http://www.academia.edu/download/44161592/Adaptive_Image_Thresholding_Based_on_the20160328-31366-1wyb1jc.pdf

Peak Signal-To-Noise Ratio Based On Threshold Method for Image Segmentation, Journal of Theoretical & Applied Information Technology, 57(2)
http://www.jatit.org/volumes/Vol57No2/4Vol57No2.pdf

Comparison Single Thresholding Method for Image Segmentation on Handwritten Images, International Conference on Pattern Analysis and Intelligent Robotics
https://doi.org/10.1109/ICPAIR.2011.5976918

License Plate Recognition with Multi-Threshold Based on Entropy, 3rd International Conference on Electrical Engineering and Informatics (ICEEI 2011)
https://doi.org/10.1109/ICEEI.2011.6021627

Adaptive image segmentation based on Peak Signal to Noise Ratio for a license plate Recognition system, International Conference on Computer Applications and Industrial Electronics (ICCAIE 2010)
https://doi.org/10.1109/ICCAIE.2010.5735125
http://www.academia.edu/download/44161592/Adaptive_Image_Thresholding_Based_on_the20160328-31366-1wyb1jc.pdf

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
