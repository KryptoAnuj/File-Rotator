#for a folder as an input rotate clockwise
#change -90 to 90 for anticlockwise 

import os
from PIL import Image

def rotate_images_in_folder():
    folder_path = input("Enter the path to the folder containing images: ").strip('"').strip("'")

    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')

    try:
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(valid_extensions):
              
                image_path = os.path.join(folder_path, filename)
                
                name, ext = os.path.splitext(filename)
                
                output_filename = f"{name}(rotated){ext}"
                output_path = os.path.join(folder_path, output_filename)

                with Image.open(image_path) as img:
                    rotated_img = img.rotate(-90, expand=True)
                    
                    rotated_img.save(output_path)
                    print(f"Rotated image saved as: {output_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

rotate_images_in_folder()

############################################################################
#for a single file path

'''
import os
from PIL import Image

def rotate_image_clockwise():

    image_path = input("Enter the path to the image you want to rotate: ")
    
    directory, filename = os.path.split(image_path)
    name, ext = os.path.splitext(filename)

    output_filename = f"{name}(rotated){ext}"

    output_path = os.path.join(directory, output_filename)
    
    try:
        with Image.open(image_path) as img:
            # Rotate the image 90 degrees clockwise
            rotated_img = img.rotate(-90, expand=True)
            
            rotated_img.save(output_path)
            print(f"Rotated image saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


rotate_image_clockwise()
'''
