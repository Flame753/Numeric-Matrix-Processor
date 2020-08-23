words = str(input()).split()
words_wth_s = [w + '_' for w in words if w.endswith('s')]
print(''.join(words_wth_s)[:-1])
