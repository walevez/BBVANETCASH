import functions as make

REGISTER_CODE = '2220'
ID_COMPANY = '93543'
FREE_FIRST = '  '
FREE_TWO = '    '

id_payee = make.register_insert(input('ID del beneficiario del pago: '), 18)
name_payee = make.register_append(input('Nombre del Beneficiario: '), 36)
address = make.register_append(input('Domicilio: '), 36)
address_continue= make.register_append(input('Domicilio (continuacion): '), 36)
free_three = make.register_append('', 109)


second_register_view = REGISTER_CODE + ID_COMPANY + FREE_FIRST + id_payee + FREE_TWO + name_payee + address + address_continue + free_three + '?'
print(second_register_view)