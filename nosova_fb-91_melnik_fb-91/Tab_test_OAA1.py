import re
pattern_create = 'CREATE \w{3,10};|a-z A-Z'
pattern_insert= 'INSERT \w{3,10} \[[0-9]*,*[0-9]*\];|a-z A-Z|$'
pattern_print_tree = 'PRINT_TREE \w{3,10};|a-z A-Z'
pattern_contains ='^CONTAINS \w{3,10} \[[0-9]*,*[0-9]*\];|a-z A-Z|$'
pattern_search= '^SEARCH \w{3,10} \[WHERE (CONTAINED_BY \[[0-9],[0-9]\]|INTERSECTS \[[0-9],[0-9]\]|RIGHT_OF [0-9])\];|a-z A-Z|$'

def is_command_correctly_written(command):
    if (len(command) == 0):
        print ("Please, enter command!")
        return False
    elif (re.match(pattern_create,command)):
        print ("Command create is correct")
        return True
    elif (re.match(pattern_print_tree,command)):
        print ("Command print_tree is correct")
        return True
    elif (re.match(pattern_contains,command)):
        print ("Command contains is correct")
        return True
    elif (re.match(pattern_search,command)):
        print ("Command search is correct")
        return True
    elif (re.match(pattern_insert,command)):
        print ("Command insert is correct")
        return True
    else:
        print("Check the spelling of the command")
        return False
def parser (command):
    if (is_command_correctly_written(command) == True):
        words = command.replace(';','').split(' ')
        command_name = words[0]
        name_of_table_or_set = words[1]
        parameters = re.findall(r'\d+', command)
        if (words[0]=='CREATE'):
            print (command_name, ' ', name_of_table_or_set)
            print ("call create_table func")   #<------------- вызов функции create_table
        elif (words[0]=='PRINT_TREE'):
            print (command_name, ' ', name_of_table_or_set)
            print ('call print_tree func')     #<------------- вызов функции print_tree
        elif (words[0]=='INSERT'):
            print (command_name,' ',name_of_table_or_set,' ',parameters)
            print ('call insert_data func')    #<------------- вызов функции insert_data
        elif (words[0]=='CONTAINS'):
            print (command_name,' ',name_of_table_or_set,' ',parameters)
            print ('call contains_data func')    #<------------- вызов функции contains_data
        else:
            search_type = words[3]
            print (command_name,' ',name_of_table_or_set,' ',search_type,' ',parameters)
            print ('call search func')         #<------------- вызов функции search
        
print ("You can start with these commands: \n1) CREATE table; \n2) INSERT set_name [0,0]; \n3) PRINT_TREE set_name; \n4) CONTAINS set_name [0,0]; \n5) SEARCH set_name [WHERE ...];\n      a)RIGHT_OF 1\n      b)CONTAINED_BY [0,0]\n      c)INTERSECTS [0,0]\n")
while(1):
    command = input()
    parser (command)