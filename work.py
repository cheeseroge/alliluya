import random
print('Насколько они большие?')
N = int(input())
i = 0
j = 0
x = 0
y = 0
s = 0
n = 0
r = 0
print('Введи 1 для ручного заполнения матрицы или 2 если хочешь заполнить их автоматически')
c1 = int(input())
if c1 == 1:
	R = N
	C = N
	matrix1 = []
	print('Введи элементы первой матрицы')
	for i in range(R):
		a = []
		for j in range(C):
			a.append(int(input()))
		matrix1.append(a)
	for i in range(R):
		for j in range(C):
			print(matrix1[i][j], end=" ")
		print()
	R = N
	C = N
	matrix2 = []
	print('Введи элементы второй матрицы')
	for i in range(R):
		b = []
		for j in range(C):
			b.append(int(input()))
		matrix2.append(b)
	for i in range(R):
		for j in range(C):
			print(matrix2[i][j], end=" ")
		print()
if c1 == 2:
	R = N
	C = N
	matrix1 = []
	print('Введи элементы первой матрицы')
	for i in range(R):
		a = []
		for j in range(C):
			a.append(random.randint(0, 100))
		matrix1.append(a)
	for i in range(R):
		for j in range(C):
			print(matrix1[i][j], end=" ")
		print()
	R = N
	C = N
	matrix2 = []
	print('Введи элементы второй матрицы')
	for i in range(R):
		b = []
		for j in range(C):
			b.append(random.randint(0, 100))
		matrix2.append(b)
	for i in range(R):
		for j in range(C):
			print(matrix2[i][j], end=" ")
		print()
print('Так, и шо с этим делать? + там - или *?')
s=input()
if (s=="+"):
		for i in range(len(matrix1)):
			for j in range(len(matrix1[0])):
				print(matrix1[i][j] + matrix2[i][j], end=" ")
			print()
if (s=="-"):
		for i in range(len(matrix1)):
			for j in range(len(matrix1[0])):
				print(matrix1[i][j] - matrix2[i][j], end=" ")
			print()
if (s=="*"):
		for i in range(len(matrix1)):
			for j in range(len(matrix1[0])):
				print(matrix1[i][j] * matrix2[i][j], end=" ")
			print()

