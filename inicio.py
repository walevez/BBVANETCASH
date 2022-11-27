# CONSTANTES UNIVERSALES



# CONSTANTES DE REGISTRO DE CABECERA
REGISTER_CODE = '2210'
ID_COMPANY = '93543'
BANK_ISSUING = '0017'
BRANCH_OFFICE = '0215'
CD_ACCOUNT = '51'
NUMBER_ACCOUNT = '0100638193'
COIN_CODE = 'ARS'
RETURN_INDICATOR = '0'
CBU_TYPE_ACCOUNT = '20'

# CONSTANTES DE PRIMER REGISTRO
ID_COMPANY = '93543'
FREE_ONE = '  '
FREE_TWO = '    '
WAY_TO_PAY = '1'
FREE_THREE = '0000000000'


# def registro_cabecera(input_string, length_string):
#     words = input_string
#     list_compilet = []
    
#     for i in range(len(words)):
#         character = words[i]
#         list_compilet.append(character)
    
#     if len(list_compilet) < length_string:
#         for i in range(int(length_string)-len(list_compilet)):
#             empty_space = " "
#             list_compilet.append(empty_space)
            
#     list_compilet = "".join(list_compilet)
#     print(list_compilet + ' <--------------- Dato Ingresado!')
#     return list_compilet


# create_date = registro_cabecera(input('Fecha de creacion: ') ,8)
# process_date = registro_cabecera(input('Fecha de deseada de proceso: ') ,8)
# service_code = registro_cabecera(input('Codigo de Servicio: ') ,10)
# file_name = registro_cabecera(input('Nombre del archivo: ') ,12)
# ordering_name = registro_cabecera(input('Nombre ordenante: ') ,36)
# free = registro_cabecera(input('Libre: '), 140)

# registro_cabecera_view = REGISTER_CODE + ID_COMPANY + create_date + process_date + BANK_ISSUING + BRANCH_OFFICE + CD_ACCOUNT + NUMBER_ACCOUNT + service_code + COIN_CODE + RETURN_INDICATOR + file_name + ordering_name + CBU_TYPE_ACCOUNT + free + '?'
# print(registro_cabecera_view)


def first_register_append(input_string, length_string):
    words = input_string
    list_compilet = []
    
    for i in range(len(words)):
        character = words[i]
        list_compilet.append(character)
    
    if len(list_compilet) < length_string:
        for i in range(int(length_string)-len(list_compilet)):
            empty_space = " "
            list_compilet.append(empty_space)
            
    list_compilet = "".join(list_compilet)
    print(list_compilet + '<--------------- Dato Ingresado!')
    return list_compilet

def first_register_insert(input_string, length_string):
    words = input_string
    list_compilet = []
    
    for i in range(len(words)):
        character = words[i]
        list_compilet.append(character)
    
    if len(list_compilet) < length_string:
        for i in range(int(length_string)-len(list_compilet)):
            empty_space = "0"
            list_compilet.insert(0, empty_space)
            
    list_compilet = "".join(list_compilet)
    print(list_compilet + ' <--------------- Dato Ingresado!')
    return list_compilet

id_payee = first_register_insert(input('ID del beneficiario del pago: '), 18)
cbu_payee = first_register_append(input('CBU del Beneficiario: '), 22)
payment_amount = first_register_insert(input('Importe de pago: '), 13)
decimal_payment = first_register_append(input('Pago decimal: '), 2)
return_code = first_register_append(input('Codigo de devolucion: ') or '000000', 6)
pay_date = first_register_append(input('Fecha de pago: '), 8)
cuil_payee = first_register_insert(input('CUIL del beneficiario: '), 15)
free_four = first_register_append('', 111)


first_register_view = REGISTER_CODE + ID_COMPANY + FREE_ONE + id_payee + FREE_TWO + WAY_TO_PAY + cbu_payee + FREE_THREE + payment_amount + decimal_payment + return_code + pay_date + cuil_payee + free_four + '?'
print(first_register_view)