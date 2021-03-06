import random
from crypt_s import slovari
from config import conf

def settings():
	print("Settings: \nDefault dictionary enabled - "+str(parametr1)+"\nDefault dictionary - "+str(parametr2)+"\nMaximal random in encrypting without key - "+str(parametr3)+"\nAutosave all actions - "+str(parametr4)+"\n")

def pre_start():
	global parametrs, parametr1, parametr2, parametr3, parametr4
	parametrs={}
	parametrs=conf()
	parametr1=parametrs["enable_default_dictionary"]
	parametr2=parametrs["default_dictionary"]
	parametr3=parametrs["maximal_random_in_encrypting_withowt_key"]
	parametr4=parametrs["save_all_actions"]

def logging(loged_text):
	with open('history.txt','a', encoding='utf-8') as l:
		l.write(loged_text)

#Функция преобразования строки в массив для key
def massivate_key(test):
	i=point=target=0
	word_t=num_m=''
	len_t=0
	len_t=test.count(',')+2
	massive=[0]*len_t
	while i<len(test):
		word_t=str(test[i])
		if word_t == ',':
			point=0
			massive[target] = int(num_m)
			num_m=''
			target+=1
		if point == 1:
			if word_t == ']':
				massive[target] = int(num_m)
				num_m=''
				break
			else:
				num_m += word_t
		if word_t == '[':
			point = 1
		if point == 0:
			point=1
		i+=1
		print("\n\nKey\nCycle "+str(i)+"\nNow scanning: "+str(word_t)+"\nPoint writing in massive: "+str(point)+"\nNumber massive position: "+str(target)+"\nReading to write in massive: "+str(num_m)+"\n\n")
	return massive

#Функция преобразования строки в массив для text
def massivate_text(test):
	i=point=target=0
	word_t=num_m=''
	len_t=0
	len_t=test.count(',')+2
	massive=[0]*len_t
	while i<len(test):
		word_t=str(test[i])
		if word_t == ',':
			point=0
			massive[target] = int(num_m)
			num_m=''
			target+=1
		if point == 1:
			if word_t == ']':
				massive[target] = int(num_m)
				num_m=''
				break
			else:
				num_m += word_t
		if word_t == '[':
			point = 1
		if point == 0:
			point=1
		i+=1
		print("\n\nText:\nCycle "+str(i)+"\nNow scanning: "+str(word_t)+"\nPoint writing in massive: "+str(point)+"\nNumber massive position: "+str(target)+"\nReading to write in massive: "+str(num_m)+"\n\n")
	return massive

#Функция шифрования с рандомным ключом
def cripting_without_key():
	text=input('Enter text: ')
	text=text.lower()
	i=0
	ready_cript=uncripy_key='['
	while i<len(text):
		word=text[i]
		keyr=random.randint(1, parametr3)
		key_num=int(coder[word])
		i+=1
		if i!=len(text):
			uncripy_key+=str(keyr)+","
			ready_cript+=str(key_num+keyr)+","
		else:
			uncripy_key+=str(keyr)+"]"
			ready_cript+=str(key_num+keyr)+"]"
		print(word+" "+coder[word]+" "+str(keyr))
	if str(parametr4) == 'true':
		itog="MODE: encryption without key\nUsed dictionary: "+str(dict_name)+"\nUsed text: "+str(text)+"\nReady encrypted text: "+str(ready_cript)+"\nYour key to decryption: "+str(uncripy_key)+'\n\n'
		logging(itog)
	print("\n\nMODE: encryption without key\nUsed dictionary: "+str(dict_name)+"\nReady encrypted text: "+str(ready_cript)+"\nYour key to decryption: "+str(uncripy_key)+'\n\n')

#Функция шифрования с полным ключом
def cripting_with_full_key():
	text=input('Enter text: ')
	text=text.lower()
	keyr_str=input("Enter key: ")
	keyr=massivate_key(keyr_str)
	if len(keyr)-1==len(text):
		i=lenght_if=0
		lenght_if=len(text)-1
		ready_cript=uncripy_key='['
		while i<len(text):
			word=text[i]
			key_num=int(coder[word])
			if i!=lenght_if:
				uncripy_key+=str(keyr[i])+","
				ready_cript+=str(key_num+keyr[i])+","
			else:
				uncripy_key+=str(keyr[i])+"]"
				ready_cript+=str(key_num+keyr[i])+"]"
			print(word+" "+coder[word]+" "+str(keyr[i]))
			i+=1
		if str(parametr4) == 'true':
			itog="MODE: encryption with full key\nUsed dictionary: "+str(dict_name)+"\nUsed text: "+str(text)+"\nUsed key: "+str(keyr)+"\nReady encryption text: "+str(ready_cript)+"\nYour key to decryption: "+str(uncripy_key)+'\n\n'
			logging(itog)
		print("\n\nMODE: encryption with full key\nUsed dictionary: "+str(dict_name)+"\nReady encryption text: "+str(ready_cript)+"\nYour key to decryption: "+str(uncripy_key)+'\n\n')
	else:
		print("The length of the keys in the array is not equal to the length of the text! Stop encryption ...")	

#Функция шифрования с одним постоянным ключом (Хуета не безопастная!)
def cripting_with_key():
	text=input('Enter text: ')
	text=text.lower()
	keyr=int(input("Enter alltime one key: "))
	i=0
	ready_cript=uncripy_key='['
	while i<len(text):
		word=text[i]
		key_num=int(coder[word])
		i+=1
		if i!=len(text):
			uncripy_key+=str(keyr)+","
			ready_cript+=str(key_num+keyr)+","
		else:
			uncripy_key+=str(keyr)+"]"
			ready_cript+=str(key_num+keyr)+"]"
		print(word+" "+coder[word]+" "+str(keyr))
	if str(parametr4) == 'true':
		itog="MODE: encryption with key\nUsed dictionary: "+str(dict_name)+"\nUsed text: "+str(text)+"\nUsed key: "+str(keyr)+"\nReady encryption text: "+str(ready_cript)+"\nYour key to decryption: "+str(uncripy_key)+'\n\n'
		logging(itog)
	print("\n\nMODE: encryption with key\nUsed dictionary: "+str(dict_name)+"\nReady encryption text: "+str(ready_cript)+"\nYour key to decryption: "+str(uncripy_key)+'\n\n')

#Функция расшифровки
def uncripting():
	text=input('Enter encryption text: ')
	text=text.lower()
	keyw=input('Enter your key: ')
	i=0
	uncripted_text=''
	lenght=text.count(',')+2
	massive_text_crypt=massive_key_crypt=[0]*lenght
	massive_text_crypt=massivate_text(text)
	massive_key_crypt=massivate_key(keyw)
	print(str(massive_text_crypt)+" "+str(massive_key_crypt))
	stopw=0
	while i<len(text) and stopw==0:
		massive_minus=str(int(massive_text_crypt[i] - massive_key_crypt[i]))
		print(str(massive_minus)+" = "+str(massive_text_crypt[i])+" - "+str(massive_key_crypt[i]))
		if massive_minus=='0' or massive_text_crypt[i]==0:
			stopw=1
		else:
			try:
				uncripted_text+=uncoder[massive_minus]
			except:
				uncripted_text+=" WRONG_KEY "
		print("Cycle "+str(i)+"\nMassive massive_minus= "+str(massive_minus)+"\nText= "+str(uncripted_text)+"\n\n")
		i+=1
	if str(parametr4) == 'true':
		itog="MODE: decryption with full key\nUsed dictionary: "+str(dict_name)+"\nUsed text: "+str(text)+"\nUsed key: "+str(keyw)+"\nReady decrypted text: "+str(uncripted_text)+'\n\n'
		logging(itog)
	print("\n\nMODE: decryption with full key\nUsed dictionary: "+str(dict_name)+"\nReady decrypted text: "+str(uncripted_text)+'\n\n')

def uncripting_with_alltime_key():
	text=input('Enter encryption text: ')
	text=text.lower()
	keyw=input('Enter your key: ')
	i=massive_key_crypt=0
	uncripted_text=''
	lenght=text.count(',')+2
	massive_key_crypt=[0]*lenght
	massive_text_crypt=massivate_text(text)
	massive_key_crypt=int(keyw)
	print(str(massive_text_crypt)+" "+str(massive_key_crypt))
	stopw=0
	while i<len(text) and stopw==0:
		massive_minus=str(int(massive_text_crypt[i] - massive_key_crypt))
		print(str(massive_minus)+" = "+str(massive_text_crypt[i])+" - "+str(massive_key_crypt))
		if massive_minus=='0' or massive_text_crypt[i]==0:
			stopw=1
		else:
			try:
				uncripted_text+=uncoder[massive_minus]
			except:
				uncripted_text+=" WRONG_KEY "
		print("Cycle "+str(i)+"\nMassive massive_minus= "+str(massive_minus)+"\nText= "+str(uncripted_text)+"\n\n")
		i+=1
	if str(parametr4) == 'true':
		itog="MODE: decryption with one alltime key\nUsed dictionary: "+str(dict_name)+"\nUsed text: "+str(text)+"\nUsed key: "+str(keyw)+"\n\nReady decryption text: "+str(uncripted_text)+'\n\n'
		logging(itog)
	print("\n\nMODE: decryption with one alltime key\nUsed dictionary: "+str(dict_name)+"\n\nReady decryption text: "+str(uncripted_text)+'\n\n')

def main():
	type_wrk=input("Select: \n\n1 - Encryption with random key (more safe).\n2 - Encryption with key (easy to hack).\n3 - Encryption with full key ([n1,n2,n3],[k1,k2,k3] - OK | [n1,n2,n3],[k1,k2] - BAD).\n4 - Decryption with full key ([n1,n2,n3...]). \n5 - Decryption with one alltime key (n).\n6 - Change dictionary (dictionary now: "+str(dict_name)+").\n7 - Show settings.\n\n")
	if type_wrk=='1':
		cripting_without_key()
	elif type_wrk=='2':
		cripting_with_key()
	elif type_wrk=='3':
		cripting_with_full_key()
	elif type_wrk=='4':
		uncripting()
	elif type_wrk=='5':
		uncripting_with_alltime_key()
	elif type_wrk=='6':
		change_slovar()
	elif type_wrk=='7':
		settings()

def change_slovar():
	global coder, uncoder, dict_name
	parametr1='false'
	coder,uncoder,dict_name=slovari(parametr1, parametr2)
	print("\nDictionary successfully selected: "+str(dict_name)+"\n")

hi_logotype='''
╔╗─╔══╦════╦═══╗──╔═══╦╗─╔╦══╦═══╦╗╔╦═══╦════╗
║║─╚╗╔╩═╗╔═╣╔══╝──║╔══╣╚═╝║╔═╣╔═╗║║║║╔═╗╠═╗╔═╝
║║──║║──║║─║╚══╦══╣╚══╣╔╗─║║─║╚═╝║╚╝║╚═╝║─║║
║║──║║──║║─║╔══╩══╣╔══╣║╚╗║║─║╔╗╔╩═╗║╔══╝─║║
║╚═╦╝╚╗─║║─║╚══╗──║╚══╣║─║║╚═╣║║║─╔╝║║────║║
╚══╩══╝─╚╝─╚═══╝──╚═══╩╝─╚╩══╩╝╚╝─╚═╩╝────╚╝

#       Created by HasellEas        #
#                                   #
#       VK: vk.com/nnikolyaa        #
#    Gmail: haselleas@gmail.com     #
#    Discord = ♣nnikŌ₤ɣǺa♣#8908     #

'''
print(hi_logotype)

pre_start()

if parametr1=='false':
	change_slovar()
elif parametr1=='true':
	choose_slova=str(parametr2)
	coder,uncoder,dict_name=slovari(parametr1, parametr2)

#Защита от критов, выключить для поиска ошибок
protect=1
while True:
	if protect==1:
		try:
			main()
		except:
			print("Error\nDo you want to off 'try:' ptotect? (Y/N) \n")
			que=input()
			if str(que.lower())=='y':
				protect=0
	elif protect==0:
		main()
