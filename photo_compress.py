# 照片压缩
# 徐浡伦

from PIL import Image
import os


def compress_image(input_path, output_path, quality=85, max_size=None):
    """
    Compress an image by reducing its quality or resizing it.

    Parameters:
        input_path (str): Path to the input image.
        output_path (str): Path to save the compressed image.
        quality (int): Quality of the output image (1-100, higher means better quality).
        max_size (tuple): Maximum width and height of the output image (optional).
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Resize the image if max_size is provided
            if max_size:
                img.thumbnail(max_size, Image.ANTIALIAS)

            # Save the image with the specified quality
            img.save(output_path, "JPEG", quality=quality)

            print(f"Image compressed and saved to {output_path}")
    except Exception as e:
        print(f"Error compressing image: {e}")


if __name__ == "__main__":
    # Example usage
    input_image_path = "1.png"  # Replace with your input image path
    output_image_path = "2.png"  # Replace with your desired output path

    # Compress with quality reduction only
    compress_image(input_image_path, output_image_path, quality=70)

    # Compress with resizing and quality reduction
    compress_image(input_image_path, output_image_path, quality=70, max_size=(800, 800))
