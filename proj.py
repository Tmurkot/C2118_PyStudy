print('Lesson2, Python DDF')


class Marker:
    color: str
    thikness: int
    isAvailable: bool

    def __init__(self, color, thikness, isavailable = True):
        self.color = color
        self.isavailable = isavailable
        self.thikness = thikness


    def get_info(self):
        print("general_info")
        if self.isavailable:
            print(f'color-{self.color} | thk - {self.thikness}')
        else:
            print("this marker is absent in storage")



markerRed = Marker(red, 2)
markerRed.get_info()
markerRed.color = "black"
markerRed.get_info()
