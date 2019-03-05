import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn import svm
style.use('ggplot')

x = [1, 5, 1.5, 9, 0.6, 9]
y = [2, 4, 1.8, 8, 1, 11]

plt.scatter(x,y)

prediction = ['small', 'large', 'small', 'large', 'small', 'large']
array = [[0,0] for i in xrange(len(x))]

for i in range(len(x)):
    element = [x[i], y[i]]
    array[i] = element

array = np.array(array)
#array = array.flatten()
print array
print len(array)
print len(prediction)

clf = svm.SVC(kernel = 'linear', C = 1.0)
clf.fit(array, prediction)
print clf.predict([[20, 40]])
plt.show()




