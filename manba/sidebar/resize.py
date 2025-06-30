from PIL import Image

image = Image.open( "images/logging.png" )
image = image.resize( ( 100, 100 ) )

image.save( "images/resized_images/logging.png" )
