import barcode
import random
from barcode.writer import ImageWriter
from barcode.writer import SVGWriter
from barcode import EAN13
from barcode import UPCA
from io import BytesIO

path_svg = './barcodes/generated.svg'
length = 5
numbers = '0123456789'

individual_number = '8'
manufacturer_number = "".join(random.choices(numbers, k=length))
product_number = "".join(random.choices(numbers, k=length))
check_digit = '5'

def generate_svg():

    code_template = str(individual_number + str(manufacturer_number) + str(product_number))
    # code_template = str(individual_number + str(manufacturer_number) + str(product_number) + check_digit)

    with open(path_svg, "wb") as f:
        # UPCA(code_template, writer=SVGWriter()).write(f)
        code = UPCA(code_template, writer=SVGWriter())
        code.write(f)
        # EAN13(str(123456789102), writer=SVGWriter()).write(f)
        # EAN13(str(100000011111), writer=SVGWriter()).write(f)

    print(code)
    print(len(str(code)))
    # print(f'Generated code: {code_template}')
    print(f'The SVG code was generated in: {path_svg}')

generate_svg()