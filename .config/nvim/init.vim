:set number
:set relativenumber


"vim-plug plugin manager"
call plug#begin()

Plug 'dracula/vim',{'as':'dracula'}
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

call plug#end()

:colorscheme dracula
:AirlineTheme dracula
:highlight Normal ctermbg=none
:highlight NonText ctermbg=none
