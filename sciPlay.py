import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn import svm
from sklearn import datasets


style.use('ggplot')

x = [1, 5, 1.5, 8, 1, 9]
y = [2, 8, 1.8, 8, 0.6, 11]

X = np.array([
    [1,2],
    [5,8],
    [1.5,1.8],
    [8,8],
    [1,0.6],
    [9,11]]
)

y = ['small','large','small','large','small','large']

clf = svm.SVC(kernel = 'linear', C = 1.0)
clf.fit(X,y)

print clf.predict([[100,100]])
plt.scatter(x,y)
plt.show()


