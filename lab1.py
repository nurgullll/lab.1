import numpy as np


massiv = np.arange(10)
print("Бастапқы массив:", massiv)


print("Индекстері 3 тен 6-ға дейінгі элементтер :", end=" ")
for i in range(3, 7):
    print(massiv[i], end=" ")
print()



for i in range(7, 10):
    massiv[i] = (i - 6) * 10
print("Өзгерген  массив:", massiv)




