def print_book_info(title, author=None, year=None):
    t = f'"{title}"'
    s = ' was written'
    a = f' by {author}'
    y = f' in {year}'

    if author and year:
        print(t + s + a + y)
    elif author and not year:
        print(t + s + a)
    elif year and not author:
        print(t + s + y)
    else:
        print(t)
