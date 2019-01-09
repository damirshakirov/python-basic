__author__ = 'Шакиров Дамир Харисович'

import os
def currentdir(): # Возвращает текущий каталог
	path=os.getcwd()
	return path

def createdir(name): # Создает каталог в текущем каталоге
	os.mkdir(currentdir()+'/'+name)

def deldir(name): # Удаляет каталог в текущем каталоге
	os.rmdir(currentdir()+'/'+name)

def listdir(): # Просмотр содержимого текущего каталога
	files=os.listdir(currentdir())
	return files