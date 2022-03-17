" Line numbers and relative numbers
set number
set relativenumber
" Enable mouse on terminal emulators
set mouse=a
"Highlight search
set hlsearch
" Backspace as in other text editors
set backspace=2
" Ignore case when searching
set ignorecase
filetype plugin indent on
set tabstop=4
set shiftwidth=4
set expandtab
" Use utf-8
set encoding=utf-8
"Enable true color
set t_Co=256

let g:airline_theme='dracula'
let g:airline_powerline_fonts = 1
let g:airline#extensions#languageclient#enabled = 1

"vim-plug plugin manager"
call plug#begin()

" Dracula theme
Plug 'dracula/vim',{'as':'dracula'}
" Surround with braces, quotes, etc...
Plug 'tpope/vim-surround'
" Airline bottom bar
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'autozimu/LanguageClient-neovim'
" Telescope fuzzy finder
Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim'
" Toggle comments
Plug 'terrortylor/nvim-comment'
" LSP
Plug 'neovim/nvim-lspconfig'
Plug 'glepnir/lspsaga.nvim'
Plug 'glepnir/dashboard-nvim'
Plug 'ryanoasis/vim-devicons'

call plug#end()

:colorscheme dracula
:highlight Normal ctermbg=none
:highlight NonText ctermbg=none

:lua require('nvim_comment').setup()
