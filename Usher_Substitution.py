anyString = input("Enter a string: ")
empty = ''
def normalVowels(anyString, empty):
  for i in (anyString):
    x = ord(i)
    if x in (65, 69, 73, 79, 85, 97, 101, 105, 111, 117):
      x = x + 1900
      x = chr(x)
      empty = empty + x
    else:
      x = chr(x)
      empty = empty + x
  return empty

def convertVowels(anyString, empty):
  for i in (anyString):
    x = ord(i)
    x = x - 1900
    if x in (65, 69, 73, 79, 85, 97, 101, 105, 111, 117):
      x = chr(x)
      empty = empty + x
    else:
      x = x + 1900
      x = chr(x)
      empty = empty + x
  return empty

print(normalVowels(anyString, empty))
print(convertVowels(anyString, empty))
