# Turtle Image Processor

A Python-based application that uses turtle graphics to draw images. This project allows users to convert image files into turtle-drawn representations, showcasing a unique blend of image processing and graphical output.

## Features

- Converts any image into a turtle graphics drawing
- Utilizes the Python Imaging Library (PIL) for image manipulation
- Fast drawing using turtle graphics with performance optimizations

## Installation

To use this project, you need to have Python and the required libraries installed. Follow these steps to set up your environment:

1. **Clone the repository:**

   ```sh
   git clone https://github.com/MH-Alikhani/turtle-image-processor.git
   cd turtle-image-processor
   ```

2. **Install the required libraries:**

   ```sh
   pip install -r requirements.txt
   ```

   Ensure `requirements.txt` contains the following:

   ```txt
   Pillow
   ```

## Usage

1. **Prepare an image:**

   Ensure you have an image file you want to process.

2. **Run the script:**

   ```sh
   python main.py
   ```

3. **Follow the prompts:**

   Enter the path to your image file when prompted.

### Example

```sh
$ python main.py
Please provide the image path: /path/to/your/image.jpg
```

The turtle graphics window will open, and the drawing process will begin. The script updates the progress in the terminal, showing the current line being processed.

## Technical Details

### `ImageProcessor` Class

A base class for image processing that loads and prepares the image.

**Attributes:**

- `image_path`: Path to the image file.
- `img`: The original image.
- `rgb_img`: The image converted to RGB format.
- `width`, `height`: Dimensions of the image.

**Methods:**

- `process_image()`: Abstract method to be overridden by subclasses.

### `TurtleImageProcessor` Class

Inherits from `ImageProcessor` and implements the turtle graphics drawing.

**Attributes:**

- `screen`: The turtle graphics screen.
- `offset_x`, `offset_y`: Initial turtle position.

**Methods:**

- `_set_initial_turtle_position()`: Sets the initial turtle position.
- `process_image()`: Draws the image using turtle graphics.

### `ImageProcessorFactory` Class

A factory class to create different types of image processors.

**Methods:**

- `create_image_processor(processor_type, image_path)`: Creates an instance of the specified image processor type.

### Main Function

The entry point of the script that initializes and starts the image processing.

**Steps:**

1. Prompts the user for the image path.
2. Creates a `TurtleImageProcessor`.
3. Calls `process_image()` to start drawing.

## Contribution

Contributions are welcome! Please fork the repository and submit a pull request.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## Acknowledgements

- [Python Imaging Library (PIL)](https://python-pillow.org/)
- [Turtle Graphics Documentation](https://docs.python.org/3/library/turtle.html)
