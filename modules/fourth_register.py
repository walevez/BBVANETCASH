import functions as make

REGISTER_CODE = '2240'
ID_COMPANY = '93543'
FREE_FIRST = '  '
FREE_TWO = '    '

id_payee = make.register_insert(input('ID del beneficiario del pago: '), 18)
concept = make.register_append(input('Concepto: '), 40)
free_three = make.register_append('', 177)


fourth_register_view = REGISTER_CODE + ID_COMPANY + FREE_FIRST + id_payee + FREE_TWO + concept + free_three + '?'
print(fourth_register_view)