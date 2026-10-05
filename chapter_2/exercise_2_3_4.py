class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        average = (self._red + self._green + self._blue) // 3
        self._red = self._green = self._blue = average

    def print_pixel_info(self):
        color_name = ""
        if self._red > 50 and self._green == self._blue == 0:
            color_name = " Red"
        elif self._green > 50 and self._red == self._blue == 0:
            color_name = " Green"
        elif self._blue > 50 and self._red == self._green == 0:
            color_name = " Blue"
        print(f"X: {self._x}, Y: {self._y}, Color: ({self._red}, {self._green}, {self._blue}){color_name}")


def main():
    pixel = Pixel(5, 6, 250)
    pixel.print_pixel_info()
    pixel.set_grayscale()
    pixel.print_pixel_info()


if __name__ == "__main__":
    main()
