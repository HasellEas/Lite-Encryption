RU:
Благодарю за скачивание Lite-Encryption!
Копирование кода, материалов проекта с одобрения автора
Автор HasellEas
Контакты:
Gmail = haselleas@gmail.com
VK = vk.com/nnikolyaa
Discord = ♣nnikŌ₤ɣǺa♣#8908

Задачи файлов:
config.py - настройки
crypt.py - файл для запуска Lite-Encrypting
crypt_s.py - словари для шифрования/расшифрования
history.txt - история ваших шифрований/расшифрований на случай если вы что-то забыли

Описание проекта:
Этот код предназначен для лёгкого шифрования небольших текстов (около 1600 символов)
Метод шифрования - Замена символов на набор чисел из словаря.
Механика работы (расматривается на режиме without key):
1) При написании : "Привет", первым в ход идёт цикл, который сверяет каждую букву в строке с словарём. Если он находит символ в словаре, то он отдаёт его номер. После прохода всех букв через цикл, их итоговые номера записываюся в массив. Пример: "Привет - [n1,n2,n3,n4,n5,n6]"
2) Далее для каждого числа в массиве, рандомно создаются числа, после чего мы получаем ключ
3) После получения ключа, каждый номер массива текста и ключа слаживаются. Пример : "[text1,text2,text3](преобразованый в числа текст) + [key1,key2,key3](рандомно созданный ключ) = [text1+key1,text2+key2,text3+key3](готовый зашифрованный текст)"
Готово!
Не зная ключа подобную шифровку почти не возможно раскрыть.

Для установки своих собственных словарей:
1) В "crypt_s.py" в конце кода перед "return" скопировать и вставить следующее:

	elif choose_slova=='3':
		coder={
			'a': '177777',
		}
		uncoder={
			'177777': 'a',
		}

#coder - При нахождении символа в тексте, отдаёт его номер, uncoder - При нахождении номера отдаёт символ 

2) В 'dictionars_names' в конце поставить это:

		'3': 'my personal',

#Имя словаря под номером 3 - 'mypersonal'

2) В "choose_slova==' СЮДА ':" вести номер своего словаря (для примера стоит "3")
3) При запуске в поле выбора словаря , введите номер указаный в "choose_slova==' ЗДЕСЬ ':"
Готово!

Доступные настройки config.py:

"enable_default_dictionary" (false/true) - При запуске, вместо выбора словаря будет использоваться стандартный список, номер которого указаны в "default_dictionary"
"default_dictionary" - Номер стандартного словаря
"maximal_random_in_encrypting_withowt_key" - Максимальное число рандомного ключа в режиме without key





EN:
Thank you for downloading Lite-Encryption!
Copying code, project materials with the author's approval
Author HasellEas
Contacts:
Gmail = haselleas@gmail.com
VK = vk.com/nnikolyaa
Discord = ♣ nnikŌ₤ɣǺa ♣ #8908

File tasks: 
config.py - settings 
crypt.py - file to run Lite-Encrypting
crypt_s.py - dictionaries for encryption/decryption
history.txt - history of your encryptions / decryptions in case you forgot something

Project Description:
This code is designed for easy encryption of small texts (about 1600 characters)
The encryption method is to replace characters with a set of numbers from the dictionary.
The mechanics of the work (depicted in the mode without key):
1) When writing: "Hello", the first thing in the course is a loop that checks each letter in the line with the dictionary. If it finds a character in the dictionary, it gives its number. After passing all the letters through the loop, their final numbers are written to the array. Example: "Hello - [n1, n2, n3, n4, n5, n6]"
2) Next, for each number in the array, numbers are randomly created, after which we get the key
3) After receiving the key, each number of the text array and the key are aligned. Example: "[text1, text2, text3] (converted to numbers text) + [key1, key2, key3](randomly generated key) = [text1+key1, text2+key2, text3+key3] (ready encrypted text)"
Done!
Without knowing the key, such encryption is almost impossible to reveal.

To install your own dictionaries:
1) In "crypt_s.py "at the end of the code before" return", copy and paste the following:

	elif choose_slova=='3':
		coder={
			'a': '177777',
		}
		uncoder={
			'177777': 'a',
		}

# coder - when a character is found in the text, gives its number, uncoder - when a number is found, gives the character

2) In 'dictionars_names' at the end put this:

		'3': 'my personal',

# Dictionary name with number 3 - 'mypersonal'

2) In" choose_slova==' HERE': "keep the number of your dictionary (for example, it is "3")
3) When starting in the dictionary selection field, enter the number specified in "choose_slova==' HERE ':"
Done!

Available settings config.py:

"enable_default_dictionary" (false/true) - At startup, instead of selecting a dictionary, a standard list will be used, the number of which is specified in "default_dictionary"
"default_dictionary" - The number of the standard dictionary
"maximal_random_in_encrypting_withowt_key" - The maximum number of random keys in without key mode