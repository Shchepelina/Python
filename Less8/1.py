#Дополнить телефонный справочник возможностью изменения и удаления данных.
#Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def append_contact(contacts_file):
    contact = input('Введите контакт в формате Ф И О Телефон: ')
    with open(contacts_file, 'a', encoding="utf-8") as f:
        f.write(f'\n{contact}')
    print ('Контакт добавлен')

def read_file(contacts_file):
    with open(contacts_file, 'r', encoding="utf-8") as f:
        print (f.read())

def search_contact(contacts_file):
    search_by = input("Введите информацию для поиска (фамилия, имя или отчество): ")
    with open(contacts_file, 'r', encoding="utf-8") as f:
        for line in f:
            if search_by in line:
                return str(line)

def remove_contact(contacts_file):
    print('Для удаления контакта: ')
    card = search_contact(contacts_file) 
    del_cont = (input(f'Вы хотите удалить контакт \n {card} \n 1 - ДА \n 2 - НЕТ\n'))
    if del_cont == '1':
        with open(contacts_file, 'r', encoding="utf-8") as f: 
                all = f.readlines() 
        for i in range(len(all)-1): 
            if  card == all[i]: 
                all.pop(i) 
        cont_2 = ''.join(all) 
        with open(contacts_file, 'w', encoding="utf-8") as f: 
            f.write(f'{cont_2}')
            print ('Контакт удалён')

def change_contact(contacts_file):
    print('Для изменения контакта: ')
    card = search_contact(contacts_file) 
    del_cont = (input(f'Вы хотите изменить контакт \n {card} \n 1 - ДА \n 2 - НЕТ\n')) 
    if del_cont == '1':
        with open(contacts_file, 'r', encoding="utf-8") as f: 
                all = f.readlines() 
        for i in range(len(all)-1): 
             if  card == all[i]:
                new_contact = (str(input("Введите новые данные контакта: ")+'\n'))
                all[i] = new_contact
        cont_2 = ''.join(all) 
        with open(contacts_file, 'w', encoding="utf-8") as f:
            f.write(f'{cont_2}')
            print ('Контакт изменён')

def user_action():
    print ('Добро пожаловать! \n'
    '1) Вывести весь справочник\n'
    '2) Добавить контакт \n'
    '3) Найти контакт\n'
    '4) Найти и удалить контакт\n'
    '5) Найти и изменить контакт\n')
    while (input1:= int(input('Выберите действие со справочником (0 = выход): '))) != 0:
        if input1 == 1:
            read_file(contacts_file)
        elif input1 == 2:
            append_contact(contacts_file)
        elif input1 == 3:
            print(search_contact(contacts_file))
        elif input1 == 4:
            remove_contact(contacts_file)
        elif input1 == 5:
            change_contact(contacts_file)
        else:
            print("Некорректный ввод")
contacts_file = 'phone_number.txt'
user_action()