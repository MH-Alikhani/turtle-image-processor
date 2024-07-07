import turtle as t
from PIL import Image
from turtle import Screen
from typing import Tuple


class ImageProcessor:
    """Base class for image processing."""

    def __init__(self, image_path: str):
        self.image_path = image_path
        self.img = Image.open(self.image_path)
        self.rgb_img = self.img.convert("RGB")
        self.width, self.height = self.img.size

    def process_image(self):
        raise NotImplementedError("This method should be overridden by subclasses.")


class TurtleImageProcessor(ImageProcessor):
    """Image processor that draws an image using turtle graphics."""

    def __init__(self, image_path: str):
        super().__init__(image_path)
        self.screen = Screen()
        self.screen.colormode(255)
        self.offset_x, self.offset_y = self._set_initial_turtle_position()
        t.shape("classic")
        t.speed(0)
        t.tracer(0, 0)  # Disable turtle animation for faster drawing

    def _set_initial_turtle_position(self) -> Tuple[float, float]:
        """Calculate the initial turtle position and set it."""
        offset_x = -(self.width / 2)
        offset_y = self.height / 2
        t.penup()
        t.setposition(offset_x, offset_y)
        t.pendown()
        return offset_x, offset_y

    def process_image(self) -> None:
        """Draw the image using the turtle graphics."""
        for y in range(self.height):
            t.penup()
            t.setposition(self.offset_x, -y + self.offset_y)
            t.pendown()
            
            row_colors = [self.rgb_img.getpixel((x, y)) for x in range(self.width)]
            t.penup()
            t.setposition(self.offset_x, -y + self.offset_y)
            t.pendown()

            for x, color in enumerate(row_colors):
                t.pencolor(color)
                t.setx(x + self.offset_x)
            t.penup()

            if y % 10 == 0:  # Update the screen every 10 lines for better performance
                t.update()
                print(f"Current line: {y + 1} of {self.height}")

        t.update()  # Final screen update
        print("Drawing finished")
        t.done()  # Finish the turtle graphics


class ImageProcessorFactory:
    """Factory class to create image processors."""

    @staticmethod
    def create_image_processor(processor_type: str, image_path: str) -> ImageProcessor:
        if processor_type == 'turtle':
            return TurtleImageProcessor(image_path)
        else:
            raise ValueError(f"Unknown processor type: {processor_type}")


def main() -> None:
    """Main function to execute the image processing."""
    image_path = input("Please provide the image path: ")
    processor_type = 'turtle'  # Can be extended to support different types
    processor = ImageProcessorFactory.create_image_processor(processor_type, image_path)
    processor.process_image()


if __name__ == "__main__":
    main()
