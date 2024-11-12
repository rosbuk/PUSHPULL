print('')
print('')
import os
import shutil
import sys 

while True:
    print(
        'MANAGER MENU\n \
        1. Make a folder\n \
        2. Remove a file or a folder\n \
        3. Copy a file or a folder\n \
        4. View the content of the work directory\n \
        5. View folders only\n \
        6. View files only\n \
        7. View the OS information\n \
        8. About the author\n \
        9. Play the Victory game\n \
        10. My bank account\n \
        11. Change the work directory\n \
        12. Exit\n'
    )

    menu = input('Print the number of the menue item you want to use: ')
    w_dir = os.getcwd()

    if menu == '1' :
        folder_name = input('Print the name of the folder to make: ')
        if not os.path.exists(folder_name):        
            os.mkdir(folder_name)
        else: 
            print('The folder name is used already')

    if menu == '2' :
        name = input('Print the name of the folder or the full name of the file to remove: ')
        path = os.path.join(w_dir, name)

        if os.path.isfile(path):
            os.remove(path)
            print(f'The file {name} is removed')
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print(f'The folder {name} is removed')
        else:
            print('The folder  or the file is not found')

    if menu == '3' :
        name = input('Print the name of the folder or the full name of the file to copy: ')
        path = os.path.join(w_dir, name)

        if os.path.isfile(path):
            name.split('.') 
            shutil.copy(name, name.split('.')[0]+'_copy.' + name.split('.')[1])
            print(f'The file {name} is copied')
        elif os.path.isdir(path):
            shutil.copytree(path, path+'_copy')
            print(f'The folder {name} is copied')
        else:
            print('The folder  or the file is not found')

    if menu == '4' :
        contents = os.listdir(w_dir)
        print('')       
        print('The contents of the work directory is:')
        for cont in contents:
            print('    '+cont)       
        print('')


    if menu == '5' :
        folders = [item for item in os.listdir(w_dir) if os.path.isfile(os.path.join(w_dir, item))]
        print('')       
        print('The folders in the work directory are:')
        for f in folders:
            print('    '+f)       
        print('')

    if menu == '6' :
        files = [item for item in os.listdir(w_dir) if os.path.isdir(os.path.join(w_dir, item))]
        print('')       
        print('The files in the work directory are:')
        for f in files:
            print('    '+f)       
        print('')

    if menu == '7' :
        print('')
        print('Current operation system is: ')
        print(sys.platform)

    if menu == '8' :
        print('')        
        with open('author.txt', 'r', encoding='utf-8') as file:   
            author = file.read()
        print('The programm was made by')    
        print(author)
        
    if menu == '9' : 
        import victory       

    if menu == '10' : 
        import account 

    if menu == '11' : 
        new_directory = input('Print the new work directory path:  ')
        os.chdir(new_directory)
        print('The new work directory is ', os.getcwd()) 

    if menu == '12' :
        break







