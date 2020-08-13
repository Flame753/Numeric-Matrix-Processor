# My attempt
phrase = str(input()).split('_')
words = ''
for word in phrase:
    words = words + word.capitalize()
print(words)

# Another way to do the same task
phrase = input().split('_')
for word in phrase:
    print(word.capitalize(), end='')
