import random
from PIL import Image, ImageFilter
from PIL import Image


class Basic:
    def apply_to_pixel(self, pixel):
        raise NotImplementedError()

    def apply_to_image(self, img):
        for i in range(img.width):
            for j in range(img.height):
                pixel= img.getpixel((i, j))
                new_pixel = self.apply_to_pixel(pixel)
                img.putpixel((i, j), new_pixel)
        return img


class RandomFilter(Basic):
    def apply_to_pixel(self, pixel):
        list_meth = []

        for i in range(len(pixel)):
            list_meth.append(random.randint(0, 255))
        return tuple(list_meth)


class InverseFilter(Basic):
    def apply_to_pixel(self, pixel):
        list_meth = []

        for i in range(len(pixel)):
            list_meth.append(pixel[i])
            list_meth[i] = 255 - list_meth[i]
        return tuple(list_meth)


class CMYK:
    def apply_to_image(self, img):
        img_gray = img.convert("L")
        edges = img_gray.filter(ImageFilter.FIND_EDGES)
        return edges

