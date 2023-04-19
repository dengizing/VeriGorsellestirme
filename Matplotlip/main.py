import matplotlib.pyplot as plt
import numpy as np

'''x=[1,2,3,4]
y=[1,4,9,16]

plt.plot(x,y)
plt.axis([0,6,0,20])

plt.title("Grafik Başlığı")
plt.xlabel("x label")
plt.ylabel("y label")'''

x=np.linspace(0,2,100)
plt.plot(x,x, label ="linear",color="red")
plt.plot(x,x**2,label="quadratic",color="yellow")
plt.plot(x,x**3, label="cubic",color="green")

plt.xlabel("x label")
plt.ylabel("y label")

plt.legend()

plt.show()