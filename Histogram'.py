import matplotlib.pyplot as plt

marks = [12,22,11,66,78,44,33,22,33,44,55.77,88]
plt.hist(marks,bins=[0,50,75,100],rwidth=0.95,color='g')
plt.show()