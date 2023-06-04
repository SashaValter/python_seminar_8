# 1. открыть файл
# 2. сохранить файл
# 3. показать все контакты
# 4. добавить контакт
# 5.найти контакт
# 6.изменить контакт
# 7.удалить контакт
# 8.выход

# функция открытия файла
def open_file_read(path):
    with open(path,'r') as file:
        main_list = file.readlines()
        main_list_1 = [x.rstrip().split() for x in main_list]
    return main_list_1
# print(open_file_read('phones.txt'))

def open_file_write(path, list_file):
    with open(path,'w') as file:
        file.writelines([''.join(x)+'\n' for x in list_file])
# list_file = [['meladze valerii', 'meladze konstantin'], ['kirkorov philip']]
# open_file_write('phones1.txt',list_file)
# list_for_look = [['valter', 'sasha', '123456'], ['smirnova', 'alina', '098765'], ['kosa', 'maksim', '765432'], ['kizaru', 'oleg', '987524']]

# функция для вывода контактов в консоль
def show_list(list_for_show):
    print ([' '.join(x) for x in list_for_show])
# show_list(list_for_look)

# функция для добавления нового пользователя в справочник
def add_new_user(path,list_file):
    with open(path,'a') as file:
        file.writelines([''.join(x) for x in list_file])
# new_user = 'nechporenko oleg 123785'
# add_new_user('phones1.txt', new_user)


# функция поиска контакта 
word = 'alina'
def find_user(path, word):
    with open(path,'r') as file:
      n=0
      for line in file:
        n += 1
        if word in line:
          print(word, 'id данного пользователя - ', n)
        else:
           print('данного пользователя нет в телефонной книге')
find_user('phones.txt', word)
