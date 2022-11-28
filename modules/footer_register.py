import functions as make

REGISTER_CODE = '2910'
ID_COMPANY = '93543'
FREE_FIRST = '  '
FREE_TWO = '    '

payment_amount = make.register_insert(input('Importe Total del fichero ENTERA: '), 13)
decimal_payment = make.register_insert(input('Importe Total del fichero DECIMAL: '), 2)
number_operations = make.register_insert(input('Numero total de operaciones: '), 8)
number_regiters = make.register_insert(input('Numero total de registros: '), 10)
free_three = make.register_append('', 208)


footer_register_view = REGISTER_CODE + ID_COMPANY + payment_amount + decimal_payment + number_operations + number_regiters + free_three + '?'
print(footer_register_view)