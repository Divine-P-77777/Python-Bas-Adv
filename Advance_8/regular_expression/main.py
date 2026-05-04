import re

# =========================================
#  SAMPLE TEXT
# =========================================
text = """
Cyclone Dumazile was a strong tropical cyclone.
Another cyclone Dyclone formed nearby.
SuperCyclone and MegaCyclone are examples.
Email: test@example.com
Phone: 9876543210
Date: 04-05-2026
"""

# =========================================
#  BASIC PATTERN
# =========================================
pattern = r"[A-Z]+yclone"  
# Meaning:
# [A-Z]+ → one or more uppercase letters
# yclone → followed by 'yclone'

print("findall:", re.findall(pattern, text))
#  Finds all matches

# =========================================
#  1. re.search()
# =========================================
match = re.search(pattern, text)
if match:
    print("search:", match.group())  # first match

# =========================================
#  2. re.match()
# =========================================
match = re.match(pattern, text)
print("match:", match)  
#  Only checks at beginning of string

# =========================================
#  3. re.findall()
# =========================================
matches = re.findall(pattern, text)
print("findall:", matches)

# =========================================
#  4. re.finditer()
# =========================================
for m in re.finditer(pattern, text):
    print("finditer:", m.group(), "at", m.span())

# =========================================
#  5. re.sub()
# =========================================
new_text = re.sub(pattern, "STORM", text)
print("sub:", new_text)

# =========================================
#  6. re.split()
# =========================================
split_text = re.split(r"\s+", text)
print("split:", split_text[:5])

# =========================================
#  7. FLAGS
# =========================================
print("IGNORECASE:", re.findall(r"cyclone", text, re.IGNORECASE))

# =========================================
#  8. COMMON PATTERNS
# =========================================

# Email
emails = re.findall(r"\w+@\w+\.\w+", text)
print("emails:", emails)

# Phone number (10 digits)
phones = re.findall(r"\b\d{10}\b", text)
print("phones:", phones)

# Date (dd-mm-yyyy)
dates = re.findall(r"\b\d{2}-\d{2}-\d{4}\b", text)
print("dates:", dates)

# Words starting with capital letter
caps = re.findall(r"\b[A-Z][a-z]+\b", text)
print("capital words:", caps)

# =========================================
#  9. GROUPS
# =========================================
match = re.search(r"(\w+)@(\w+)\.(\w+)", text)
if match:
    print("groups:", match.groups())  
    # ('test', 'example', 'com')

# =========================================
#  10. COMPILE (for reuse)
# =========================================
compiled = re.compile(r"\bcyclone\b", re.IGNORECASE)
print("compiled:", compiled.findall(text))

# =========================================
#   SPECIAL SYMBOLS QUICK GUIDE
# =========================================
# .   → any character
# ^   → start of string
# $   → end of string
# *   → 0 or more
# +   → 1 or more
# ?   → optional
# {}  → exact count
# []  → character set
# \d  → digit
# \w  → word character
# \s  → whitespace

# =========================================
#  DEBUG TIP
# =========================================
print("DEBUG:", re.findall(r"[A-Z][a-z]+yclone", text))