# Shakespearean Insult Constructor (construction module)
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

import random

def construct_insult():
	insult_select = 0                  # Will be assigned a random number between 0 and 49 and used to select from each collection of components.
	read_insult = ""                   # Accepts each line from the insult list file and passes it to insult_list.
	insult_list = []                   # Stores one or more sub-lists, each one a collection of components from which to assemble an insult.
	built_insult = "Thou "             # The string that each component will be appended to to form a complete insult. Always begins with "Thou ".
	
	insults = open("insults", "r")     # Opens the insult list file for reading.
	
	for line in insults:
		read_insult = line.strip("\n") # Gets rid of the carriage return from each line read.
		
		# If the line read reads "[NEW]", creates a new sub_list within insult_list.
		# Otherwise just adds the newly-read string to the newest existing sub-list.
		if read_insult == "[NEW]":
			insult_list.append([])
		else:
			insult_list[-1].append(read_insult)
	
	insults.close()                    # Closes the file, to prevent the risk of the OS treating it as already open after the program has ended.
	
	for insult_column in range(len(insult_list)):
		# Generates a random number with which to select each insult component.
		insult_select = random.randint(0, len(insult_list[insult_column]) - 1)
		#print insult_column, insult_select
		
		# Appends the selected insult component to built_insult.
		built_insult = built_insult + insult_list[insult_column][insult_select]
		
		# If the current insult column is before the last one, append a space, else append an exclamation mark.
		if insult_column < 2:
			built_insult = built_insult + " "
		else:
			built_insult = built_insult + "!"
	
	return built_insult                # Send the completed insult back to the variable that called this function!
