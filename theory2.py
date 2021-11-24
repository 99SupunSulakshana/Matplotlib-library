import matplotlib.pyplot as plt
import numpy as np
x = [1,2,3,4,5]
plt.plot(x,np.power(x,2),'k^-.',x,np.power(x,3),'c+:')
plt.xlabel('X axis')
plt.ylabel('y axis')
plt.title('Example')
plt.show()