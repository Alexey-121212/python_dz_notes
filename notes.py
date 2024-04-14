# Задание 1. Приложение заметки (Python)

from typing import List
import re
from datetime import datetime
# 2, date, time, timedelta

file_name = 'notes.csv'

def get_last_id(file):
    lines = load_notes(file_name)
    if lines != -1:
        m = re.search('(.+?);', lines[len(lines)-1])
        id = int(m.group(1)) +1
        return id
    return 1
        
def save_note(file):

    id = get_last_id(file_name)    
    title = input('Введите заголовок заметки: ')
    body = input('Введите тело заметки: ')
    created = datetime.now()
    edited = None
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{id};{title};{body};{created};{edited}\n')
        print('\nЗаметка сохранена \n')

def load_notes(file):
     try:
        with open(file, 'r', encoding='utf-8') as f:
             lines = f.readlines()
        return lines
     except FileNotFoundError:
        open(file, 'w', encoding='utf-8')
        return -1
def delete_node(file):
    id = input('Введите ID заметки для удаления')
    
    
    
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
            save_note(file_name)
        elif answer == '2':
            lines = load_notes(file_name)
            m=0
            if lines != -1:
                for i in lines:
                    m+=1
                    print(i)
                if m==0:
                    input('Файл с заметками пуст\n')
            else:
                input('Файл с заметками отсутствует, создал пустой\n')
        elif answer == '3':
           edit_note(file_name)
        elif answer == '4':
           delete_note(file_name)
    
if __name__ == '__main__':
    main()