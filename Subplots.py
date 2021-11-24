import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,2,0.1)
y1 = x
y2 = np.sqrt(x)
y3 = np.power(x,2)
y4 = np.power(x,3)

plt.subplot(2,2,1)
plt.plot(x,y1,'ro')
plt.title('x values')

plt.subplot(2,2,2)
plt.plot(x,y2,'g--')
plt.title('$y2 = \sqrt{x}')

plt.subplot(2,2,3)
plt.plot(x,y3,'b^')
plt.title('$y3 = x^s$')

plt.subplot(2,2,4)
plt.plot(x,y4,'ks')
plt.title('$y4 = x^2S')

plt.show()