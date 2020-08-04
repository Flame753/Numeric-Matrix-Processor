# put your python code here
class Time:
    def __init__(self):
        self.hour = int(input())
        self.minutes = int(input())
        self.seconds = int(input())
        self.total_seconds = (self.hour * 60 * 60) + (self.minutes * 60) + self.seconds

    def difference(self, time):
        return abs(self.total_seconds - time.total_seconds)


a = Time()
b = Time()
print(a.difference(b))
