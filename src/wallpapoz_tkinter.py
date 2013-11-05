#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=============================================================================
#
#   wallpapoz.py - Wallpapoz
#   Copyright (C) 2013 Vajrasky Kok <sky.kok@speaklikeaking.com>
#
#=============================================================================
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#=============================================================================
from tkinter import Tk
from os.path import expanduser
from os.path import sep

from wallpapoz_gui.wallpapoz_menu import makemenu
from wallpapoz_gui.wallpapoz_main_window import makemainwindow


if __name__ == '__main__':
    root = Tk()
    root.title("Wallpapoz")
    makemenu(root)
    # Get the wallpapoz configuration file
    home = expanduser('~')
    wallpapoz_setting_dir = home + sep + '.wallpapoz'
    wallpapoz_setting_file = wallpapoz_setting_dir + sep + 'wallpapoz.xml'

    # parse it
    workspaces = {
        'workspace1': ['haha', 'hihi'],
        'workspace2': ['haha', 'hihi'],
    }
    makemainwindow(root, workspaces)
    root.mainloop()
