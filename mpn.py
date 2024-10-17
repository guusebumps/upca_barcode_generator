import random
import barcode
from barcode.writer import ImageWriter
from barcode.writer import SVGWriter

path_svg = './barcodes/mpn.svg'

def generate_mpn():
    # prefix = "TTC"
    prefix = "776"
    number = ''.join([str(random.randint(0, 9)) for _ in range(8)])  # 8 random digits
    mpn = f"{prefix}-{number}"
    return mpn

def generate_barcode_svg(mpn, file_name):
    code128 = barcode.get('code128', mpn, writer=SVGWriter())
    
    svg_file = f"./barcodes/{file_name}"
    code128.save(svg_file)
    print(f"Barcode saved as: {svg_file}")

    print(f'The SVG code was generated in: {svg_file}')    

def main():
    mpn = generate_mpn()
    mpn2 = mpn.replace("-", "")
    print(f"Generated MPN: {mpn}")
    print(f"Generated MPN2: {mpn2}")
    
    generate_barcode_svg(mpn, 'mpn_barcode')

if __name__ == "__main__":
    main()
