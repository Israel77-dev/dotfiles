# Dotfiles

Repository containing my config files for linux distros. These, along with the programs and commands listed on this Readme are used to setup my particular workflow, but feel free to use them however you want.

## Stuff that I use

### Programs
These are the software that I use on a daily basis, some of them are configured through the dotfiles in this repo:

|         Purpose         |                                             Software                                              |
| :---------------------: | :-----------------------------------------------------------------------------------------------: |
|      Distribution       |                               [Linux Mint](https://linuxmint.com/)                                |
|     Window manager      |                                  [QTile](http://www.qtile.org/)*                                  |
|       Compositor        |                             [Picom](https://github.com/yshui/picom)*                              |
|          Shell          |                                   [Zsh](https://www.zsh.org/)*                                    |
|    Terminal emulator    |                            [kitty](https://sw.kovidgoyal.net/kitty/)*                             |
|     Source control      |                                   [Git](https://git-scm.com/)*                                    |
|       Text Editor       |                                    [Vim](https://www.vim.org/)                                    |
|           IDE           |             [VSCode](https://code.visualstudio.com/), [NeoVim](https://www.neovim.io)             |
|       Web Browser       |           [Firefox Developer Edition](https://www.mozilla.org/pt-BR/firefox/developer)            |
|        Launcher         |                            [Rofi](https://github.com/davatorium/rofi)*                            |
|      File manager       | [Nemo](https://github.com/linuxmint/nemo) (GUI), [ranger](https://github.com/ranger/ranger) (TUI) |
|       Fancy info        |                        [neofetch](https://github.com/dylanaraps/neofetch)*                        |
|      Media player       |                   [VLC](https://www.videolan.org/vlc/), [mpv](https://mpv.io/)                    |
|         Torrent         |                               [Deluge](https://deluge-torrent.org/)                               |
| Bluetooth configuration |                        [Blueberry](https://github.com/linuxmint/blueberry)                        |
|    Background setter    |                           [Nitrogen](https://github.com/l3ib/nitrogen)*                           |
|   GTK+ Theme selector   |                       [LXAppearance](https://github.com/lxde/lxappearance)                        |
|      Office Suite       |                            [LibreOffice](https://www.libreoffice.org/)                            |
|  Visual Git Management  |                              [GitKraken](https://www.gitkraken.com/)                              |
|     Screenshot tool     |                                [Flameshot](https://flameshot.org/)                                |
|     Process viewer      |                                     [htop](https://htop.dev/)                                     |
|     ls replacement      |                               [exa](https://github.com/ogham/exa)*                                |
|  Retrieve system info   |                           [psutil](https://pypi.org/project/psutil/)**                            |

\* Some dotfiles reference these programs to configure other apps (e.g. The zsh prompt will be different if kitty is not used)
\*\* Required for my qtile bar

### Themes, plugins, add-ons, etc...

These are meant to be used as complements to some of the programs listed above. When it comes to theming, most things are based on the [Dracula theme](draculatheme.com/).

#### Zsh Plugins

Expected to be cloned into $HOME/.zsh_plugins (except for powerlevel10k, which basically just needs the ~/.p10k.zsh file):

* [PowerLevel10k](https://github.com/romkatv/powerlevel10k): Highly configurable and versatile zsh prompt 
* [Fast Syntax Highlighting](https://github.com/zdharma-continuum/fast-syntax-highlighting): Syntax highlighting on the shell 
* [Zsh Autosuggestions](https://github.com/zsh-users/zsh-autosuggestions): Suggestions based on command usage history

#### VSCode Themes and Extensions

* [Vim](https://marketplace.visualstudio.com/items?itemName=vscodevim.vim): Vim keybindings emulation for VSCode.
* [Extension profiler](https://marketplace.visualstudio.com/items?itemName=cyberbiont.vscode-profiles): Manage extensions for different types of projects
* [Dracula Theme](https://marketplace.visualstudio.com/items?itemName=dracula-theme.theme-dracula): Official Dracula theme
* [Dracula at Night](https://marketplace.visualstudio.com/items?itemName=bceskavich.theme-dracula-at-night) and [Dark Material Dracula](https://marketplace.visualstudio.com/items?itemName=carloshenrique.dark-material-dracula): Some variations on the dracula theme, that I sometimes find easier to read.
* [Material Icons](https://marketplace.visualstudio.com/items?itemName=pkief.material-icon-theme): Icon theme
* [Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments): Highlight TODOs, Notes, etc...
* [Todo tree](https://marketplace.visualstudio.com/items?itemName=gruntfuggly.todo-tree): Show TODOs, FixMes, etc, throughout the project
* [Code Spell](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker): Spell checker.
* [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint): ESLint integration
* [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode): Prettier formatter integration
* [Vite](https://marketplace.visualstudio.com/items?itemName=antfu.vite): Vite integration
* [Hocus Pocus](https://marketplace.visualstudio.com/items?itemName=nicoespeon.hocus-pocus): Some neat stuff for TypeScript

#### Other:

* GTK+ Theme: [Dracula Theme](https://www.pling.com/p/1687249).
* GTK+ Icon Theme: [Papirus-dark](https://www.pling.com/p/1166289/)
* Cursor Theme: [Dracula cursors](https://www.pling.com/p/1669262/)
