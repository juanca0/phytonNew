¿Cual es tu nombre?: deisy
>>> nombre
'deisy'
>>> nombre.upper()
'DEISY'
>>> nombre.capitalize()
'Deisy'
>>> nombre
'deisy'
>>> nombre = nombre.capitalize()
>>> nombre
'Deisy'
>>> nombre = nombre.strip()
>>> nombre
'Deisy'
>>> nombre = nombre.lowe()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'lowe'
>>> nombre = nombre.lower()
>>> nombre
'deisy'
>>> nombre.replace('d','D')
'Deisy'
>>> nombre = nombre.replace('d','D')
>>> nombre
'Deisy'
>>> nombre[0]
'D'
>>> nombre[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> nombre[2]
'i'
>>> lent(nombre)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'lent' is not defined
>>> len(nombre)
5
>>> len('Hola! Este es el curso de pyton')
31