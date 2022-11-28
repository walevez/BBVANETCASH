
# Insert empty space to end
def register_append(input_string, length_string):
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
    print(list_compilet + '<--------------- Datos Ingresado!')
    return list_compilet

# Insert zeros from the beginning
def register_insert(input_string, length_string):
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
    print(list_compilet + '<--------------- Datos Ingresado!')
    return list_compilet