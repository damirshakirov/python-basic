__author__ = 'Шакиров Дамир Харисович'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
path=os.getcwd()
print ('Текущий рабочий каталог: %s' %path)
i=1
while i<=9: # Создание каталогов
	os.mkdir(path+'/dir_'+str(i))
	i+=1
input('Нажмите любую кнопку для удаления созданных каталогов')

i=1
while i<=9: # Удаление каталогов
	os.rmdir(path+'/dir_'+str(i))
	i+=1


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
files=os.listdir(path)
print('Содержимое текущего каталога:\n',files)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import inspect,shutil
currentfile=inspect.getfile(inspect.currentframe())
shutil.copyfile(currentfile,'copy_'+currentfile)