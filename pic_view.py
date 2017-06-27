from PIL import Image
import matplotlib.pyplot as plt
img=Image.open('E:\D\thumbnail\tngfkortneyjohnny_1080.mp4.jpg')
plt.figure("test1")
plt.imshow(img)
plt.show()
plt.axis('off')