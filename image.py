# WORKING WITH IMAGES
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO


# if image in jpeg form
#fname=r'bird.jpg'  - png
#image = Image.open(fname).convert('L')


url = 'https://th.bing.com/th/id/OIP.rUkvOs8sbgzneV-NxXD57gHaHa?pid=ImgDet&w=190&h=190&c=7&dpr=1.4'
# Downloading image
response = requests.get(url)
image = Image.open(BytesIO(response.content)).convert('L')

# MApping image to gry scale
plt.imshow(image , cmap='gray') # we can change color as rainbow or something else
plt.grid()
plt.show()
