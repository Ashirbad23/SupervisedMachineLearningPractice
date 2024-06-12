import numpy as np
import matplotlib.pyplot as plt

arr_values = np.linspace(-np.pi, np.pi, 200)
print(arr_values)

sin_values = np.sin(arr_values)
cos_values = np.cos(arr_values)
tan_values = np.tan(arr_values)

plt.subplot(1, 3, 1)
plt.plot(arr_values, sin_values)
plt.xlabel('Values')
plt.ylabel("Sin values")
plt.title('Sin curve')

plt.subplot(1, 3, 2)
plt.plot(arr_values, cos_values)
plt.xlabel('Values')
plt.ylabel("Cos values")
plt.title('Cos curve')

plt.subplot(1, 3, 3)
plt.plot(arr_values, tan_values)
plt.xlabel('Values')
plt.ylabel("Tan values")
plt.title('Tan curve')

plt.suptitle("Trigonometric Curves")
plt.tight_layout()

plt.show()
# plt.savefig("curve.png")