import re
pattern_create = 'CREATE \w{1,10}|a-z A-Z'
pattern_insert= 'INSERT \w{1,10} \[[0-9]*,*[0-9]*\]|a-z A-Z|$'
pattern_print_tree = 'PRINT_TREE \w{1,10}|a-z A-Z'
pattern_contains ='^CONTAINS \w{1,10} \[[0-9]*,*[0-9]*\]|a-z A-Z|$'
pattern_search= '^SEARCH \w{1,10} \[WHERE (CONTAINED_BY \[[0-9],[0-9]\]|INTERSECTS \[[0-9],[0-9]\]|RIGHT_OF [0-9])\]|a-z A-Z|$'


def delete_space_from_string (string):
    if (string[0]==' '):
        string=string[1:]
    string = re.sub(' +', ' ', string)
    string = re.sub(' +;', ';', string)
    string = re.sub(' +]', ']', string)
    string = re.sub(' +,', ',', string)
    if( bool(re.search('RIGHT_OF', command, flags = re.IGNORECASE)) == False):
       string = re.sub(' +0', '0', string)
       string = re.sub(' +1', '1', string)
       string = re.sub(' +2', '2', string)
       string = re.sub(' +3', '3', string)
       string = re.sub(' +4', '4', string)
       string = re.sub(' +5', '5', string)
       string = re.sub(' +6', '6', string)
       string = re.sub(' +7', '7', string)
       string = re.sub(' +8', '8', string)
       string = re.sub(' +9', '9', string)
    
    return string;
def is_command_correctly_written(command):
    
    if (len(command) == 0):
        print ("Please, enter command!")
        return False
    elif (re.search('-',command)):
        print ("Negative numbers are not allowed")
    elif (re.match(pattern_create,command,flags = re.IGNORECASE)):
        print ("Command create is correct")
        return True
    elif (re.match(pattern_print_tree,command,flags = re.IGNORECASE)):
        print ("Command print_tree is correct")
        return True
    elif (re.match(pattern_contains,command,flags = re.IGNORECASE)):
        print ("Command contains is correct")
        return True
    elif (re.match(pattern_search,command,flags = re.IGNORECASE)):
        print ("Command search is correct")
        return True
    elif (re.match(pattern_insert,command,flags = re.IGNORECASE)):
        print ("Command insert is correct")
        return True
    else:
        print("Check the spelling of the command", command)
        return False
def parser (command):
    
    if (is_command_correctly_written(command) == True):
        words = command.replace(';','').split(' ')
        parameters = re.findall(r'\d+', command)
        if (bool(re.search('CREATE', words[0], flags = re.IGNORECASE)) == True):
            print ('CREATE', ' ', words[1])
            print ("call create_table func")   #<------------- вызов функции create_table
        elif (bool(re.search('PRINT_TREE', words[0], flags = re.IGNORECASE)) == True):
            print ('PRINT_TREE', ' ', words[1])
            print ('call print_tree func')     #<------------- вызов функции print_tree
        elif (bool(re.search('INSERT', words[0], flags = re.IGNORECASE)) == True):
            print ('INSERT',' ',words[1],' ',parameters)
            print ('call insert_data func')    #<------------- вызов функции insert_data
        elif (bool(re.search('CONTAINS', words[0], flags = re.IGNORECASE)) == True):
            print ('CONTAINS',' ',words[1],' ',parameters)
            print ('call contains_data func')    #<------------- вызов функции contains_data
        else:
            search_type = words[3]
            print ('SEARCH',' ',words[1],' ',search_type,' ',parameters)
            print ('call search func')         #<------------- вызов функции search
        
print ("You can start with these commands: \n1) CREATE table; \n2) INSERT set_name [0,0]; \n3) PRINT_TREE set_name; \n4) CONTAINS set_name [0,0]; \n5) SEARCH set_name [WHERE ...];\n      a)RIGHT_OF 1\n      b)CONTAINED_BY [0,0]\n      c)INTERSECTS [0,0]\n")
while(1):
    command = input()
    commands = command.split(';')
    commands.pop()
    i=0
    sizeofcommands = len(commands)
    while i < sizeofcommands:
        commands[i] = delete_space_from_string(commands[i])
        parser(commands[i])
        i += 1

        

