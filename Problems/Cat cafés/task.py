cafe_name: str = ''
amount_cats: int = 0
while True:
    cafe = str(input()).split()
    if len(cafe) == 1:
        print(cafe_name)
        break
    elif int(cafe[1]) > amount_cats:
        cafe_name = cafe[0]
        amount_cats = int(cafe[1])
