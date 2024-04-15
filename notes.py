# Задание 1. Приложение заметки (Python)

from typing import List
from datetime import datetime


file_name = 'notes.csv'

def get_new_id():
    lines = load_notes()
    if lines != None and len(lines)!=0 :
        return int(lines[len(lines)-1].split(';')[0]) + 1
    return 1

def print_note(line):
    note = line.split(';')
    print(f'ID: {note[0]}  Title: {note[1]}  Body: {note[2]} CreatedDate: {note[3]} EditedDate: {note[4]}')
        
def save_note():
    id = get_new_id()    
    title = input('Введите заголовок заметки: ')
    body = input('Введите тело заметки: ')
    dt = datetime.now()
    created = str(dt.day) + '-' + str(dt.month) + '-' + str(dt.year)
    edited = None
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(f'{id};{title};{body};{created};{edited}\n')
        print('\nЗаметка сохранена \n')

def load_notes():
     try:
        with open(file_name, 'r', encoding='utf-8') as f:
             lines = f.readlines()
        return lines
     except FileNotFoundError:
        open(file_name, 'w', encoding='utf-8')
        return None

def show_notes():
    
    lines = load_notes()
    if lines == None:
            input('Файл с заметками отсутствует, создал пустой\n')    
    else:
        if len(lines) == 0:
            input('Файл с заметками пуст\n')
        else:
            sw = False
            while not sw :
                filter_date = input('\nВведите дату создания заметки в формате DD-MM-YYYY,\nдля отображения всех заметок нажмите Enter:\n')
                try :
                    sw = bool(datetime.strptime(filter_date, '%d-%m-%Y'))
                except ValueError:
                    if len(filter_date) == 0:
                        sw = True
                    else:
                        sw = False
            for line in lines:
                if  len(filter_date) == 0 or datetime.strptime(filter_date, '%d-%m-%Y')  == datetime.strptime(line.split(';')[3], '%d-%m-%Y'):
                    print_note(line)

def delete_note():
    id = input('Введите ID заметки для удаления: ')
    lines = load_notes()
    with open(file_name, "w") as f:
        for line in lines:
            if line.split(';')[0] != id:
                f.write(line)    

def edit_note():
    id = input('Введите ID заметки для редактирования: ')
    lines = load_notes()
    for line in lines:
        p = line.split(';')
        if p[0] == id:
            print('Текущее значение заметки:\n')
            print_note(line)
    new_note_body = input('Введите новое значение тела заметки:')
    with open(file_name, "w") as f:
        for line in lines:
            p = line.split(';')
            if p[0] == id:
                with open(file_name, 'a', encoding='utf-8') as f:
                    dt=datetime.now()
                    edited = str(dt.day) + '-' + str(dt.month) + '-' + str(dt.year)
                    f.write(f'{p[0]};{p[1]};{new_note_body};{p[3]};{edited}\n')
            else:
                with open(file_name, 'a', encoding='utf-8') as f:
                    f.write(line)
            
    print('\nЗаметка сохранена \n')
    
def main():
    flag = True
    while flag:
        print('0 - выход')
        print('1 - создать и сохранить заметку')
        print('2 - посмотреть список заметок')
        print('3 - редактировать заметку')
        print('4 - удалить заметку')        
        answer = input('Выберите действие: ')
        if answer == '0':
            flag = False
        elif answer == '1':
            save_note()
        elif answer == '2':
            show_notes()
        elif answer == '3':
            edit_note()
        elif answer == '4':
            delete_note()
    
if __name__ == '__main__':
    main()