__author__ = 'Шакиров Дамир Харисович'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
def currentdir(): # Возвращает текущий каталог
	path=os.getcwd()
	return path

print ('Текущий рабочий каталог: %s' %currentdir())

def createdir(name): # Создает каталог в текущем каталоге
	os.mkdir(currentdir()+'/'+name)

i=1
while i<=9: # Создание каталогов
	createdir('dir_'+str(i))
	i+=1
input('Нажмите любую кнопку для удаления созданных каталогов')

def deldir(name): # Удаляет каталог в текущем каталоге
	os.rmdir(currentdir()+'/'+name)
i=1
while i<=9: # Удаление каталогов
	deldir('dir_'+str(i))
#	os.rmdir(currentdir()+'/dir_'+str(i))
	i+=1


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def listdir():
	files=os.listdir(currentdir())
	return files
print('Содержимое текущего каталога:\n',listdir())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import inspect,shutil
currentfile=inspect.getfile(inspect.currentframe())
shutil.copyfile(currentfile,'copy_'+currentfile)