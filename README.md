# UPC-A Barcode Generator

This project is a simple barcode generator using Python. It creates a UPC-A barcode and saves it as an SVG file. The barcode is generated using random numbers for the manufacturer and product codes.

# Prerequisites
To run this code, you need to have Python installed along with the python-barcode package. You can install the package using pip:

```bash
pip install python-barcode
```

# Code Overview
This script generates a UPC-A barcode and saves it as an SVG file. The barcode consists of an individual number, a manufacturer number, and a product number. Here is a breakdown of the code:

# Import Statements
```bash
import barcode
import random
from barcode.writer import ImageWriter
from barcode.writer import SVGWriter
from barcode import UPCA
from io import BytesIO
```

barcode: A library to generate barcodes in various formats.
random: Python’s built-in module to generate random numbers.
ImageWriter: Used for generating barcodes as images.
SVGWriter: Used for generating barcodes as SVG files.
UPCA: Represents the UPC-A barcode format.
BytesIO: Allows the code to work with byte objects in memory, though it is not used in this script.

# Global Variables
```bash
path_svg = './barcodes/generated.svg'
length = 5
numbers = '0123456789'
```

* path_svg: The path where the generated SVG file will be saved.
* length: The length of the random number sequences used for manufacturer and product numbers.
* numbers: A string containing digits from which random numbers will be selected.
* Barcode Number Components

```bash
individual_number = '8'
manufacturer_number = "".join(random.choices(numbers, k=length))
product_number = "".join(random.choices(numbers, k=length))
```

* individual_number: A fixed number used at the start of the barcode.
* manufacturer_number: A random 5-digit number representing the manufacturer.
* product_number: A random 5-digit number representing the product.
  
# Function: generate_svg()
```bash
def generate_svg():
    code_template = str(individual_number + str(manufacturer_number) + str(product_number))

    with open(path_svg, "wb") as f:
        code = UPCA(code_template, writer=SVGWriter())
        code.write(f)

    print(f'Generated code: {code}')
    print(f'The SVG code was generated in: {path_svg}')
```

* code_template: Concatenates the individual, manufacturer, and product numbers to form a 12-digit string, which is used as the content for the UPC-A barcode.
* open(path_svg, "wb"): Opens a file in binary write mode to save the SVG barcode.
* UPCA(): Creates a UPC-A barcode object using the code_template.
* code.write(f): Writes the barcode in SVG format to the specified file.
* print statements: Outputs the generated barcode information and file path to the console.

# Usage
To generate a new UPC-A barcode as an SVG file, run the script in a Python environment:

```bash
python your_script_name.py
```

This will generate a barcode and save it in the specified path (./barcodes/generated.svg).

# Customization
You can customize the generated barcode by modifying the individual_number, length, or the path_svg variable.

individual_number: Change this value to alter the starting number of the barcode.
length: Modify this to change the length of the manufacturer and product numbers.
path_svg: Change the file path to save the barcode in a different location or with a different name.
# Contributing
Feel free to fork this project and submit pull requests for any improvements or new features. Contributions are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for details.


Para rodar basta fazer um Git Clone e em seguida rodar "pip install -r requirements.txt"
