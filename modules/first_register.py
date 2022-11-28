import functions as make

REGISTER_CODE = '2210'
ID_COMPANY = '93543'
FREE_ONE = '  '
FREE_TWO = '    '
WAY_TO_PAY = '1'
FREE_THREE = '0000000000'
CODE_STATUS_RETURN = ' '


id_payee = make.register_insert(input('ID del beneficiario del pago: '), 18)
cbu_payee = make.register_append(input('CBU del Beneficiario: '), 22)
payment_amount = make.register_insert(input('Importe de pago: '), 13)
decimal_payment = make.register_append(input('Pago decimal: '), 2)
return_code = make.register_append('', 6)
pay_date = make.register_append(input('Fecha de pago: '), 8)
cuil_payee = make.register_insert(input('CUIL del beneficiario: '), 15)
free_four = make.egister_append('', 23)
description_return = make.register_append('', 40)
free_five = make.register_append('', 76)


first_register_view = REGISTER_CODE + ID_COMPANY + FREE_ONE + id_payee + FREE_TWO + WAY_TO_PAY + cbu_payee + FREE_THREE + payment_amount + decimal_payment + return_code + pay_date + cuil_payee + free_four + CODE_STATUS_RETURN + description_return + free_five + '?'
print(first_register_view)