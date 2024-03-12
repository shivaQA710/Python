"""
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One or more occurrences
{}  Indicate number of occurrences of a preceding RE 
    to match.
()  Enclose a group of REs

"""

# Define a regular expression pattern
pattern = r"expression"

# Match the pattern against a string
text = "Hello, world!"

match = re.search(pattern, text)

if match:
    print("Match found!")
else:
    print("Match not found.")