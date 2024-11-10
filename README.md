# <b>Image Resizer and Compressor</b>

This script is a simple image compressor built in Python using the Pillow (PIL) library for image manipulation , Tkinter for file dialog interaction and customtkinter for GUI. The script allows users to select an image file and save it as a compressed JPEG.
## Features

File Selection: Uses Tkinter's askopenfilename to allow users to choose an image file from their system.
    Image Compression: The selected image is resized to its original dimensions using high-quality LANCZOS resampling to optimize compression quality. This method balances image quality and file size.
    Save as Compressed JPEG: Users can save the compressed image under a new file name. The compressed image is saved with the suffix "_compressed.JPG" in the specified location.

## Requirements

    Pillow: install it with:  pip install pillow

    Tkinter: The script uses Tkinter for file dialogs, which is included with Python’s standard library in most installations.

    customtkinter: install it with:  pip install customtkinter

    
## How to Use
To set up and run the project locally, follow these steps:
1. Clone the repository:

       git clone https://github.com/MParsa-Gh/Image-compression.git

2. Navigate to the project directory:

       cd Image-compression
    

## Note

  <h5>Resizing Strategy:</h5> The image is resized to its original dimensions, which serves primarily to apply a high-quality resampling technique for compression purposes without changing the image’s actual dimensions.
  
  
  <h5>File Format:</h5> The script saves the image as a JPEG, which is inherently a lossy compression format. This can help reduce the file size while maintaining good quality for most images.
