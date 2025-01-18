from PIL import Image

image = Image.open( "images/docker2.png" )
image = image.resize( ( 100, 100 ) )

image.save( "images/resized_images/docker.png" )
