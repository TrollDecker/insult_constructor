# Shakespearean Insult Constructor (UI version)
# Code Copyright (C) 2013  Jonathan Humphreys
# Using content from the Shakespearean Insult Kit at: http://web.mit.edu/dryfoo/Funny-pages/shakespeare-insult-kit.html

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

#!/usr/bin/env python

import Tkinter
from construct_insult import construct_insult

# Creates a new Tkinter window.
main = Tkinter.Tk()
main.geometry("500x160")
main.wm_title("Shakespearean Insult Kit")

# Calls upon construct_insult to generate an insult.
def draw_insult():
	lblInsult["text"] = construct_insult()
	btnClipboard["state"] = "normal"

# Event-handler to copy the existing insult to the clipboard.
def send_to_clipboard():
	main.clipboard_clear()
	main.clipboard_append(lblInsult["text"])

# This label will display the insult created by the program.
lblInsult = Tkinter.Label(main, bg = "#999999")
lblInsult.pack()
lblInsult.place(bordermode = "outside", x = 10, y = 10, width = 480, height = 25)

# Button to click to generate an insult.
btnConstruct = Tkinter.Button(main, bg = "#AAAAAA", text = "Construct thy insult", command = draw_insult)
btnConstruct.pack()
btnConstruct.place(bordermode = "outside", x = 10, y = 40, width = 480, height = 25)

# Button to click in order to copy to clipboard. When the program first runs, this button is disabled,
# what with nothing for it to copy yet.
btnClipboard = Tkinter.Button(main, bg = "#AAAAAA", text = "Copy to thy clipboard", command = send_to_clipboard, state = "disabled")
btnClipboard.pack()
btnClipboard.place(bordermode = "outside", x = 10, y = 70, width = 480, height = 25)

# Label to give credit to the source of the insult components.
lblCredit = Tkinter.Label(main, text = "Based on the Shakespeare Insult Kit at:\nhttp://web.mit.edu/dryfoo/Funny-pages/shakespeare-insult-kit.html")
lblCredit.pack()
lblCredit.place(bordermode = "outside", x = 10, y = 100, width = 480, height = 50)

# Commences the event-loop.
main.mainloop()
