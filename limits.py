import matplotlib.pyplot as plt
import numpy as np

plt.plot([2,4,6,8],[2,4,6,8])
left,right = plt.xlim(left=2,right=8)
print(left)
print(right)
plt.show()