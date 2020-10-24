from PIL import Image as PILImage
import matplotlib.pyplot as plt

image_file1 = "C:\\Work\\Vernell\\image_reader\\images\\181019-cardi-b_b21e6ed262ac99a6a193ef650a9225d5.jpg"
image_file2 = "C:\\Work\\Vernell\\image_reader\\images\\5d97a1004e140f1b3b22a9b6.jpg"
image1 = PILImage.open(image_file1)
image2 = PILImage.open(image_file2)
image1 = image1.resize((500,500))
image2 = image2.resize((500,500))
image_blend = PILImage.blend(image1, image2, 0.5)
plt.imshow(image_blend)
plt.show()