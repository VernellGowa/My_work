from PIL import Image as PILImage
import matplotlib.pyplot as plt

image_file = "C:\\Work\\Vernell\\image_reader\\images\\20200926_145824.jpg"
image = PILImage.open(image_file)
#image = image.rotate(250)
#image = image.resize((1000, 1000))
image = image.convert('1')
plt.imshow(image)
plt.show()
