#!/usr/bin/env python3
# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from typing import Dict

from libqtile.widget.battery import BatteryState

import os
import subprocess


# Dracula theme colors
dracula_colors: Dict = {
    "background": "#282a36",
    "background_focus": "#44475a",
    "foreground": "#f8f8f2",
    "comment": "#6272a4",
    "cyan": "#8be9fd",
    "green": "#50fa7b",
    "orange": "#ffb86c",
    "pink": "#ff79c6",
    "purple": "#bd93f9",
    "red": "#ff5555",
    "yellow": "#f1fa8c",
}


@lazy.function
def backlight_up(qtile):
    subprocess.run(["xbacklight", "-inc", "10"])


@lazy.function
def backlight_down(qtile):
    subprocess.run(["xbacklight", "-dec", "10"])


mod = "mod4"
terminal = "kitty"
editor = "code"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    

    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "p", lazy.spawn("rofi -show drun -show-icons"),
        desc="Run an application using rofi"),
    Key([mod], "e", lazy.spawn("code")),

    # Default keyboard functions
    Key([], "XF86MonBrightnessUp", backlight_up(),
        desc="Increase monitor brightness"),
    Key([], "XF86MonBrightnessDown", backlight_down(),
        desc="Decrease monitor brightness"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window
            # to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"],
    # border_width=1),
    layout.Tile(add_after_last=True,
                border_focus=dracula_colors["purple"],
                border_normal=dracula_colors["background"],
                margin=7),
    layout.Max(),
    layout.Floating(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="FiraCode Nerd Font Mono",
    fontsize=12,
    padding=3,
    background=dracula_colors["background"]
)
extension_defaults = widget_defaults.copy()

# Custom widgets


class MyBacklight(widget.Backlight):
    def poll(self) -> str:
        info = self._get_info()
        if info is False:
            return '---'
        no = int(info * 100)
        char = '☼'
        #self.layout.colour = color_alert
        return '{} {}%'.format(char, no)  # chr(0x1F50B))


class MyBattery(widget.Battery):
    def poll(self) -> str:
        status = self._battery.update_status()
        
        percent = status.percent
        symbol = ""
        charging = ""

        if status.state == BatteryState.CHARGING:
            charging = "ﮣ"

        if percent >= .95:
            symbol = ""
        elif percent >= .90:
            symbol = ""
        elif percent >= .80:
            symbol = ""
        elif percent >= .70:
            symbol = ""
        elif percent >= .60:
            symbol = ""
        elif percent >= .50:
            symbol = ""
        elif percent >= .40:
            symbol = ""
        elif percent >= .30:
            symbol = ""
        elif percent >= .20:
            symbol = ""
        else:
            symbol = ""

        return "{} {:.0f}% {}".format(symbol, percent * 100, charging)


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(foreground=dracula_colors["background"]),
                widget.CurrentLayout(),
                widget.GroupBox(
                    highlight_method="line",
                    highlight_color=dracula_colors["background_focus"],
                    this_screen_border=dracula_colors['cyan'],
                    this_current_screen_border=dracula_colors['cyan'],
                    borderwidth=2),
                widget.Systray(),
                # "Center"
                widget.Spacer(),
                widget.Clock(
                    format="<b> %d/%m | %A | %H:%M %p </b>",
                    background=[dracula_colors["comment"], dracula_colors["background_focus"]],
                    padding=10),
                widget.Spacer(),
                # Right side
                widget.CPU(format=": {load_percent}%",
                           foreground=dracula_colors["orange"],
                           padding=5),
                widget.Memory(
                    format=":{MemUsed: .1f}{mm}/{MemTotal: .1f}{mm}",
                    measure_mem="G",
                    foreground=dracula_colors["green"],
                    padding=5),
                # NOTE: Check your computer backlight service on /sys/class/backlight
                MyBacklight(
                    backlight_name="intel_backlight",
                    foreground=dracula_colors['yellow'],
                    # background=[dracula_colors['yellow'], dracula_colors['background']],
                    padding=5),
                MyBattery(foreground=dracula_colors['cyan']),
                widget.QuickExit(
                    default_text="⏻",
                    fontsize=16,
                    background=dracula_colors["background"],
                    foreground=dracula_colors["red"],
                    padding = 5),
                widget.Sep(foreground=dracula_colors["background"])
            ],
            24,
            # background="#000000"
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders
            # are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X
        # client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# Autostart applications


@hook.subscribe.startup
def autostart():
    start_script = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([start_script])

wmname = "\\e[33;49mQTile"
