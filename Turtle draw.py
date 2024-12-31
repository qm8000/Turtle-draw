import turtle
import requests
from PIL import Image
from io import BytesIO

def download_image(url):
    """
    Downloads an image from a URL and returns it as a PIL Image object.
    """
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    return Image.open(BytesIO(response.content))

def process_image(image, width=100, height=100):
    """
    Resizes the image and converts it to RGB format for turtle drawing.
    """
    image = image.resize((width, height))
    image = image.convert("RGB")  # Ensure image is in RGB format
    return image

def draw_image_with_turtle(image):
    """
    Draws the image on the screen using the turtle module.
    """
    screen = turtle.Screen()
    screen.setup(width=250, height=250)
    screen.tracer(0)  # Turn off screen updates for faster drawing

    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    # Get the image size
    width, height = image.size

    # Start drawing from the top-left corner
    start_x = -width // 5
    start_y = height // 5

    pixels = image.load()  # Get pixel data

    for y in range(height):
        for x in range(width):
            # Get the pixel color
            r, g, b = pixels[x, y]
            t.goto(start_x + x, start_y - y)
            t.dot(5, (r / 255, g / 255, b / 255))  # Normalize RGB to 0-1 for turtle

    screen.update()
    turtle.done()

def main():
    # URL of the image to draw
    url = input("Enter the image URL: ")

    # Step 1: Download the image
    print("Downloading image...")
    image = download_image(url)

    # Step 2: Process the image
    print("Processing image...")
    processed_image = process_image(image)

    # Step 3: Draw the image with turtle
    print("Drawing image...")
    draw_image_with_turtle(processed_image)
    print("Done!")

if __name__ == "__main__":
    main()