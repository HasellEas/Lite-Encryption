def slovari(parametr1, parametr2):
	dictionars_names={
		'1': 'Global',
	}
	i=max_len=0
	i_text=dictionars_list=choose_slova=''
	max_len=int(len(dictionars_names))
	while i!=max_len:
		i+=1
		i_text=str(i)
		dictionars_list+=i_text+") "+dictionars_names[i_text]+"\n"
	if parametr1=='true':
		choose_slova=parametr2
	else:
		choose_slova=input("Choose dictionary to encryption:\n\n"+str(dictionars_list)+"\n")
	try:
		dict_active_name=dictionars_names[choose_slova]
	except:
		dict_active_name='Unknown'
	if choose_slova=='1':
		#Словарь для шифрования
		coder={
			'a': '177777',
			'b': '277777',
			'c': '377777',
			'd': '477777',
			'e': '577777',
			'f': '677777',
			'g': '777777',
			'h': '877777',
			'i': '977777',
			'j': '1077777',
			'k': '1177777',
			'l': '1277777',
			'm': '1377777',
			'n': '1477777',
			'o': '1577777',
			'p': '1677777',
			'q': '1777777',
			'r': '1877777',
			's': '1977777',
			't': '2077777',
			'u': '2177777',
			'v': '2277777',
			'w': '2377777',
			'x': '2477777',
			'y': '2577777',
			'z': '2677777',
			' ': '2777777',
			'а': '2877777',
			'б': '2977777',
			'в': '3077777',
			'г': '3177777',
			'д': '3277777',
			'е': '3377777',
			'ё': '3477777',
			'ж': '3577777',
			'з': '3677777',
			'и': '3777777',
			'й': '3877777',
			'к': '3977777',
			'л': '4077777',
			'м': '4177777',
			'н': '4277777',
			'о': '4377777',
			'п': '4477777',
			'р': '4577777',
			'с': '4677777',
			'т': '4777777',
			'у': '4877777',
			'ф': '4977777',
			'х': '5077777',
			'ц': '5177777',
			'ч': '5277777',
			'ш': '5377777',
			'щ': '5477777',
			'ъ': '5577777',
			'ы': '5677777',
			'ь': '5777777',
			'э': '5877777',
			'ю': '5977777',
			'я': '6077777',
			',': '6177777',
			'!': '6277777',
			'.': '6377777',
			'/': '6477777',
			'-': '6577777',
			'*': '6677777',
			'=': '6777777',
			'@': '6877777',
		}
		#Словарь для расшифровки
		uncoder={
			'177777': 'a',
			'277777': 'b',
			'377777': 'c',
			'477777': 'd',
			'577777': 'e',
			'677777': 'f',
			'777777': 'g',
			'877777': 'h',
			'977777': 'i',
			'1077777': 'j',
			'1177777': 'k',
			'1277777': 'l',
			'1377777': 'm',
			'1477777': 'n',
			'1577777': 'o',
			'1677777': 'p',
			'1777777': 'q',
			'1877777': 'r',
			'1977777': 's',
			'2077777': 't',
			'2177777': 'u',
			'2277777': 'v',
			'2377777': 'w',
			'2477777': 'x',
			'2577777': 'y',
			'2677777': 'z',
			'2777777': ' ',
			'2877777': 'а',
			'2977777': 'б',
			'3077777': 'в',
			'3177777': 'г',
			'3277777': 'д',
			'3377777': 'е',
			'3477777': 'ё',
			'3577777': 'ж',
			'3677777': 'з',
			'3777777': 'и',
			'3877777': 'й',
			'3977777': 'к',
			'4077777': 'л',
			'4177777': 'м',
			'4277777': 'н',
			'4377777': 'о',
			'4477777': 'п',
			'4577777': 'р',
			'4677777': 'с',
			'4777777': 'т',
			'4877777': 'у',
			'4977777': 'ф',
			'5077777': 'х',
			'5177777': 'ц',
			'5277777': 'ч',
			'5377777': 'ш',
			'5477777': 'щ',
			'5577777': 'ъ',
			'5677777': 'ы',
			'5777777': 'ь',
			'5877777': 'э',
			'5977777': 'ю',
			'6077777': 'я',
			'6177777': ',',
			'6277777': '!',
			'6377777': '.',
			'6477777': '/',
			'6577777': '-',
			'6677777': '*',
			'6777777': '=',
			'6877777': '@',
		}
	return coder, uncoder, dict_active_name
'''
Example for personal dictionary
	elif choose_slova=='personal':
		coder={
			'a': '177777',
		}
		uncoder={
			'177777': 'a',
		}
'''