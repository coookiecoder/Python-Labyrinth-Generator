from PIL import Image
from lab import Labyrinth

size = 256

if size % 2 == 0:
    size = size + 1

image_lab = Image.new("L", (size, size))

white = 255
black = 0

matrix_lab = Labyrinth(size)
matrix_lab.generate_labyrinth()
matrix_lab.generate_enter()
matrix_lab.generate_exit()

tmp = matrix_lab.get_data()

for line in range(size):
    for colum in range(size):
        image_lab.putpixel((line, colum), tmp[line][colum])

image_lab.save("output.png")
