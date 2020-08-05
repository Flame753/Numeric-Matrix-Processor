class Movies:
    def __init__(self, age):
        self.age = age

    def recommendation(self):
        if self.age <= 16:
            print("Lion King")
        elif 17 <= self.age <= 25:
            print("Trainspotting")
        elif 26 <= self.age <= 40:
            print("Matrix")
        elif 41 <= self.age <= 60:
            print("Pulp Fiction")
        else:
            print("Breakfast at Tiffany's")


if __name__ == "__main__":
    a = Movies(int(input()))
    a.recommendation()
