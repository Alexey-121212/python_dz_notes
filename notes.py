# Задание 1. Приложение заметки (Python)

from typing import List
from datetime import datetime

file_name = 'notes.csv'

def get_new_id():
    lines = load_notes()
    if lines != -1:
        return int(lines[len(lines)-1].split(';')[0]) + 1
    return 1

def print_note(line):
    note = line.split(';')
    print(f'ID: {note[0]}  Title: {note[1]}  Body: {note[2]} CreatedDate: {note[3]} EditedDate: {note[4]}')
        
def save_note():
    id = get_new_id()    
    title = input('Введите заголовок заметки: ')
    body = input('Введите тело заметки: ')
    created = datetime.now()
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
        return -1

def delete_note():
    id = input('Введите ID заметки для удаления: ')
    with open(file_name, "r") as f:
        lines = f.readlines()
    with open(file_name, "w") as f:
        for line in lines:
            if line.split(';')[0] != id:
                f.write(line)    

def edit_note():
    id = input('Введите ID заметки для редактирования: ')
    with open(file_name, "r") as f:
        lines = f.readlines()
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
                    f.write(f'{p[0]};{p[1]};{new_note_body};{p[3]};{datetime.now()}\n')
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
            lines = load_notes()
            m=0
            if lines != -1:
                for i in lines:
                    m+=1
                    print_note(i)
                if m==0:
                    input('Файл с заметками пуст\n')
            else:
                input('Файл с заметками отсутствует, создал пустой\n')
        elif answer == '3':
           edit_note()
        elif answer == '4':
           delete_note()
    
if __name__ == '__main__':
    main()