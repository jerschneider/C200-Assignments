import matplotlib.pyplot as plt
import numpy as np

# Create the vectors X and Y
x = np.array(range(100))
y = x ** 2


# Create the plot
plt.axis([-10,10,-1,100])
plt.plot(x,y, color='g')
plt.plot(-x, y, color='g')
plt.plot([-5, 5], [60,60], "bo")

# Show the plot
plt.show()
