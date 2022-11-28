import functions as make

REGISTER_CODE = '2110'
ID_COMPANY = '93543'
BANK_ISSUING = '0017'
BRANCH_OFFICE = '0215'
CD_ACCOUNT = '51'
NUMBER_ACCOUNT = '0100638193'
COIN_CODE = 'ARS'
RETURN_INDICATOR = '0'
CBU_TYPE_ACCOUNT = '20'


create_date = make.register_append(input('Fecha de creacion: ') ,8)
process_date = make.register_append(input('Fecha de deseada de proceso: ') ,8)
service_code = make.register_append(input('Codigo de Servicio: ') ,10)
file_name = make.register_append(input('Nombre del archivo: ') ,12)
ordering_name = make.register_append(input('Nombre ordenante: ') ,36)
free = make.register_append('', 141)


registro_cabecera_view = REGISTER_CODE + ID_COMPANY + create_date + process_date + BANK_ISSUING + BRANCH_OFFICE + CD_ACCOUNT + NUMBER_ACCOUNT + service_code + COIN_CODE + RETURN_INDICATOR + file_name + ordering_name + CBU_TYPE_ACCOUNT + free + '?'
print(registro_cabecera_view)