class CoordError(Exception):
    pass


class ImageXIterator:
    def __init__(self, img, y:int):
        self.__x = 0
        self.__y = y
        self.__img = img
        self.__limit = img.width

    def __iter__(self):
        return self

    def __next__(self):
        if self.__x >= self.__limit:
            raise StopIteration

        self.__x += 1
        return self.__img[self.__x - 1, self.__y]



class ImageYIterator:
    def __init__(self, img):
        self.__limit = img.height
        self.__img = img
        self.__y = 0                     # lines(rows)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__y >= self.__limit:
            raise StopIteration

        self.__y += 1
        return ImageXIterator(self.__img, self.__y - 1)

class Image:
    def __init__(self, width, height, background = '_'):
        self.__background = background
        self.__pixels = {}
        self.__width = width
        self.__height = height
        self.__color = {self.__background}

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def __checkCoord(self, coord):
        if not isinstance(coord, tuple) or len(coord) != 2:
            raise CoordError('Координаты точки должны быть двумерным кортежем')

        if not (0 <= coord[0] < self.__width) or not (0 <= coord[1] < self.__height):
            raise CoordError('Значения координаты выходит за пределы изображения')


    def __setitem__(self, coord, color):
        self.__checkCoord(coord)                # is coord correct?

        if color == self.__background:          # delete pixel
            self.__pixels.pop(coord, None)
        else:
            self.__pixels[coord] = color
            self.__color.add(color)

    def __getitem__(self, coord):               # get color coord
        self.__checkCoord(coord)
        return self.__pixels.get(coord, self.__background)

    def __iter__(self):
        return ImageYIterator(self)



class MyIter:
    def __init__(self, limit):
        self.__num = 0
        self.__limit = limit               # max num

    def __iter__(self):
        return self

    def __next__(self):
        if self.__num >= self.__limit:
            raise StopIteration            # end of iteration

        self.__num += 1
        return self.__num


it = MyIter(10)

for i in it:
    print(i)






img = Image(20, 4)
img[1, 1] = '*'
img[2, 1] = '*'
img[3, 1] = '*'

for row in img:
    for pixel in row:
        print(pixel, sep =' ', end='')
    print()

# for y in range(img.height):
#     for x in range(img.width):
#         print(img[x, y], sep =' ', end='')
#     print()











