import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

images = datasets.load_digits()

clf = svm.SVC(C = 100, gamma = )



img = images.data[:-1]\
plt.imshow(img, cmap = )
plt.show(img)
