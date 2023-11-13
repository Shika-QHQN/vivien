
def intro():
    txt1 = 'Welcome to'
    new_str = txt1.center(20, '*')                                            
    a = ''' 
             )       )                                    
            /      _/                                     
           /    _/~O.     ,   O  ____     ,____           
          /  _/~ /' |    /  /' /'    )   /'    )          
         /_/~  /'   |  /' /' /(___,/'  /'    /'           
        /~    (__  _|/(__(__(________/'    /(__           '''
                                              
    print(new_str)
    print(a)
    print(' \n')
    print('This is a text editor ')
    print('Type "end now~~" to exit \nUse "display mode" to review your text\nType "save this **** file" to store it\nIf you want to read file, please type"read this **** file" and then "display mode"')

   
intro()
#  .|'''|                    .|'''|,   ||    '||            ''|, .''',  ''|, ,'''|, 
#  ||                        ||   ||   ||     ||           '  || |   | '  ||     || 
#  `|'''|, .|''|, '||''|,    `|...|| ''||''   ||''|,         .|' |   |   .|'  '''|| 
#   .   || ||..||  ||  ||         ''   ||     ||  ||        //   |   |  //       || 
#   |...|' `|...   ||..|'        ''    `|..' .||  || ,,    ((... `,,,' ((... '...|' 
#                  ||           ''                    ,                             
#                 .||                                                               
i = input('~:')
line = 0
textdata = []

while i != 'end now~~':
    if i == 'save this **** file':
        save_path = input('We do you want to store?:')
        save_name = input('Type an awesome name:')
        save_list_to_file(textdata, save_name, save_path) 
        break
    
    if i == 'read this **** file':
        read_path = input('Name the path:')
        lst_from_file = read_file(read_path)
        textdata.extend(lst_from_file)
    
    space_counter = 0
    for chch in i:
        if chch == ' ':
            space_counter += 1
        if space_counter >= 2:
            rows = i.strip().split('\n')
            for row in rows:
                textdata.append(row.strip())
           
    if i == 'display mode' and line > 0:
        for lines in range(line):
            print(lines + 1 ,' ',textdata[lines])
    else:
        textdata.append(i)
    i = input('~:')
    
    line += 1
