__author__ = 'Шакиров Дамир Харисович'

# Все задачи текущего блока решите с помощью генераторов списков!

def newlist(): # Функция для генерации списка, заполненного произвольными целыми числами
	import random
	l=[]
	for _ in range (10): l.append(random.randint(-10,10))
	return l

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
def main_1():

	def listsquare(l): # Функция для формирования нового списка, элементы которого будут квадратами элементов списка, переданного на вход функции
		i=0
		for element in l:
			l[i]=element**2
			i+=1
		return l

	print('\nЗадание №1')
	l1=newlist()
	print(l1)
	print(listsquare(l1))


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
def main_2():
	print('\nЗадание №2')
	def list_fruits_1(): # Формирование первого списка фруктов
		l=['Апельсин','Яблоко','Груша','Киви','Банан']
		return l

	def list_fruits_2(): # Формирование второго списка фруктов
		l=['Яблоко','Ананас','Киви','Папая']
		return l

	l1=list_fruits_1()
	l2=list_fruits_2()
	print(l1,l2)
	print(list(set(l1) & set(l2)))

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
def main_3():
	print('\nЗадание №3')
	l1=newlist()
	print ('Исходный список:',l1)

	def new_list_3(l1):	# Функция формировования списка из элементов крайних 3
		l2=[]
		for element in l1:
			if (element % 3) == 0 : l2.append(element)
		return l2

	def new_list_plus(l1):	# Функция формировования списка из положительных элементов
		l2=[]
		for element in l1:
			if element >0 : l2.append(element)
		return l2

	def new_list_4(l1):	# Функция формировования списка из элементов не кратным 4
		l2=[]
		for element in l1:
			if (element % 4) !=0 : l2.append(element)
		return l2

	print('Элементы кратны 3:', new_list_3(l1))
	print('Положительные элементы:', new_list_plus(l1))
	print('Элементы не кратны 4:', new_list_4(l1))

main_1()
main_2()
main_3()

