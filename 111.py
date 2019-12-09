import numpy as np
import random
import multi

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[5,6,9],[3,5,11],[22,3,2]])
s = random.randint(1,50)
c = np.zeros((3,5))
d = np.eye(5)
print(a.dot(b))
print(s)
print(np.argmax(b))
print(c)
print(d)