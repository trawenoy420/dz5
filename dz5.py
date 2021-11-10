import os
os.getcwd()
path = 'C:\\Users\\Asus\\Desktop'
os.chdir(path)

------------------------1--------------------------

mlist = []
while True:
    a = input('some words: ')
    if a == '':
        print(mlist)
    else:
        b = a + '\n'
        mlist.append(b)
    
    
    with open("test_12222.txt", "w") as file_obj:
        file_obj.writelines(mlist)

-------------------------2-----------------------

my_file = open('qqqq.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('qqqq.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('qqqq.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} строки - {len(content[i])}')
my_file = open('qqqq.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()


-------------------------3------------------------


with open('sotr.txt', 'r') as my_file:
    sal = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')


--------------------------4-----------------------

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('wwww.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('wwww_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)


---------------------------5-----------------------



def summary():
    try:
        with open('file_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода')
summary()


----------------------------6----------------------------


subj = {}
with open('eeeee.txt', 'r') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')




