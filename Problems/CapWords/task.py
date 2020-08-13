phrase = str(input()).split('_')
words = ''
for word in phrase:
    words = words + word.capitalize()
print(words)
