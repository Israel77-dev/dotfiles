
# Initialization code that may require console input (password prompts, [y/n]
# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi


# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

alias xampp='sudo /opt/lampp/manager-linux-x64.run'
alias lampp='sudo /opt/lampp/lampp'
export PATH="/opt/lampp/bin:$PATH"

# allow locally installed npm binaries to be executed;
# added by `npm i -g add-local-binaries-to-path`
export PATH="$PATH:./node_modules/.bin"


# Use Dracula theme colors on tty
if [ "$TERM" = "linux" ]; then
	echo -en "\e]P021222C"
	echo -en "\e]P1FF5555"
	echo -en "\e]P250FA7B"
	echo -en "\e]P3F1FA8C"
	echo -en "\e]P4BD93F9"
	echo -en "\e]P5FF79C6"
	echo -en "\e]P68BE9FD"
	echo -en "\e]P7F8F8F2"
	echo -en "\e]P86272A4"
	echo -en "\e]P9FF6E6E"
	echo -en "\e]PA69FF94"
	echo -en "\e]PBFFFFA5"
	echo -en "\e]PCD6ACFF"
	echo -en "\e]PDFF92DF"
	echo -en "\e]PEA4FFFF"
	echo -en "\e]PFFFFFFF"
	clear
fi

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
if [ "$TERM" = "xterm-kitty" ]; then
    source ~/.p10k-bling.zsh
else
    [[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
fi

# Neofetch on launch
# neofetch
# Alternative: cache neofetch from last terminal session
#cat .nf 2> /dev/null
#setsid neofetch >| .nf
# Alternative 2: Run neofetch only on first terminal (kitty) session
KITTY_INSTS=0
for pid in $(pidof -x kitty x-terminal-emulator); do
  KITTY_INSTS=$((KITTY_INSTS+1))
  if [ $KITTY_INSTS -gt 1 ]; then
    break;
  fi
done
if [ $KITTY_INSTS -le 1 ]; then
  neofetch
fi

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion


# Add cargo to path
export PATH="$HOME/.cargo/bin/${PATH:+:${PATH}}"

source ~/powerlevel10k/powerlevel10k.zsh-theme

# My aliases
alias ls="exa -al --color=always --group-directories-first"
alias cls='clear && neofetch'
alias dotf='git --git-dir=$HOME/.dotfiles --work-tree=$HOME' # Dotfiles management via git

# Syntax-highlighting plugin must be at the end of the file
source "$HOME/.zsh_plugins/fast-syntax-highlighting/fast-syntax-highlighting.plugin.zsh"  

alias nv=nvim
