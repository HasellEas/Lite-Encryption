def conf():
	setting={
		#RU: При запуске окна выбора словаря не будет, вместо этого будет использоваться словарь введённый в "default_dictionary"
		#EN: When launching the dictionary selection window, the dictionary entered in "default_dictionary" will be used instead
	    "enable_default_dictionary": "false",
	    #RU: Номер стандартного словаря	    
		#EN: Standard dictionary number
	    "default_dictionary": "1",
	    #RU: Максимальное число рандома ключа для шифрования без ключа
	    #EN: Maximum random key for keyless encryption
	    "maximal_random_in_encrypting_withowt_key": 10000000
	}
	return setting