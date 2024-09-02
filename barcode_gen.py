import barcode
import random
from barcode.writer import ImageWriter
from barcode.writer import SVGWriter
from barcode import UPCA
from io import BytesIO

path_svg = './barcodes/generated.svg'
length = 5
numbers = '0123456789'

individual_number = '8'
manufacturer_number = "".join(random.choices(numbers, k=length))
product_number = "".join(random.choices(numbers, k=length))

def generate_svg():

    code_template = str(individual_number + str(manufacturer_number) + str(product_number))

    with open(path_svg, "wb") as f:
        code = UPCA(code_template, writer=SVGWriter())
        code.write(f)

    print(f'Generated code: {code}')
    print(f'The SVG code was generated in: {path_svg}')

generate_svg()