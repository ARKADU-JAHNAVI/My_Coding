def insertChar(s, c, pos):
  
    # Insert character at specified position
    return s[:pos] + c + s[pos:]

s = "Geeks"
print(insertChar(s, 'A', 3))