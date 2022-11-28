import functions as make

REGISTER_CODE = '2230'
ID_COMPANY = '93543'
FREE_FIRST = '  '
FREE_TWO = '    '

id_payee = make.register_insert(input('ID del beneficiario del pago: '), 18)
location = make.register_append(input('Localidad: '), 36)
province = make.register_append(input('Provincia: '), 36)
postal_code = make.register_append(input('Codigo Postal: '), 36)
free_three = make.register_append('', 109)


third_register_view = REGISTER_CODE + ID_COMPANY + FREE_FIRST + id_payee + FREE_TWO + location + province + postal_code + free_three + '?'
print(third_register_view)