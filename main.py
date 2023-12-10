from os import name


class User:
	def__init__(self, name: str, lastname: str):
		self.name = name
		self.lastname = lastname


	def input_userName(self, name, lastname):
		while True:
			print("Введите ваши данные или нажмите 'q' что-бы выйти из программы!")
			name = input("Введите ваше имя")
			if name == 'q':
				break
			lastname = input("Введите вашу фамилию")
			if lastname == 'q':
				break

	def print_userName(self):
		print(f"{self.name} {self.surname}")

#создать хэш-таблицу с присвоением каждому user номер телефона или логин
def create_hach:
    user_hach = {}
	user_hach[name]= #значение - номер телефона или спец. логин
#создать словарь. Ключ - логин или номер телефона, а значение - пароль
# правильность ввода пароля будет проверяться с использованием булевого типа
def user_online(name): #функция поиска пользователей онлайн и вывода списка этих пользователей
     online = [] #пустой список для добавления пользователей в онлайне
	 #найти пользователя
	 #проверить его в онлайн
	 if user_online True: #добавить в список
	    online += []
	return online
class Massage (self, date, time, mas):
	#переменные, характеризующие передаваемые и хранимые сообщения
	self__date: str = date #переменная, содержащая дату создания сообщения
	self__time: float = time #переменная, содержащая время создания сообщения
	self__mas: str = mas #переменная - вводимое текстовое сообщение

	def input_massage (self, mas):
		print("Введите cообщение")
		mas = input("Введите ваше имя")

# создать очередь сообщений для хранения данных
from collections import deque
queue.append(x) #добавление сообщения в очередь
#функция поиск по историии собщений: по ключевому слову в строке, для такого использовать цикл for (насколько знаю, надо использовать библиотеку re)
#отправить сообщение, добавить сообщение в очередь
#извлечь сообщение из очереди, чтобы другой пользователь мог прочесть
