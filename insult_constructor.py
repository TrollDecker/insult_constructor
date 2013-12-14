# Shakespearean Insult Constructor (CLI version)
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

import os
from construct_insult import construct_insult
exit_prompt = "n"

while exit_prompt != "y":
	os.system("cls" if os.name == "nt" else "clear")         # Clears the screen in both Windows and Unix-likes.
	print construct_insult()
	exit_prompt = raw_input("Art thou done? (y/n)").lower()  # Unless this is set to "y" when asked, the loop will repeat again.
