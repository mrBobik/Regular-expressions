import re
import csv


# читаем адресную книгу в формате CSV в список contacts_list
def read_file():
    with open('phonebook_raw.csv', encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=',')
        contacts_list = list(rows)
    contacts_list[4].pop(-1)
    return contacts_list


# TODO 1: выполните пункты 1-3 ДЗ
def fio(contacts_list):
    pattern = r'^([\w]+)(\s*)(\,*)([\w]+)(\s*)(\,?)([\w]*)(\,?)(\,?)(\,?)([\w]*)(\,?)'
    new_pattern = r'\1\3\10\4\6\9\7\8\11\12'
    newlist = list()
    for i in contacts_list:
        i_str = ','.join(i)
        # print(i_str)
        new_line = re.sub(pattern, new_pattern, i_str)
        before_format_list = new_line.split(',')
        newlist.append(before_format_list)
    # print(newlist)
    return newlist


def phone(contacts_list):
    pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    new_pattern = r'+7(\4)\8-\11-\14\15\17\18\20'
    newlist_1 = list()
    for i in contacts_list:
        i_str = ','.join(i)
        # print(i_str)
        new_line = re.sub(pattern, new_pattern, i_str)
        before_format_list = new_line.split(',')
        newlist_1.append(before_format_list)
    # print(newlist_1)
    return newlist_1


def remove_duplicates(contacts_list):
    for i in contacts_list:
        for j in contacts_list:
            if i[0] == j[0] and i[1] == j[1] and i is not j:
                if i[2] == '':
                    i[2] = j[2]
                if i[3] == '':
                    i[3] = j[3]
                if i[4] == '':
                    i[4] = j[4]
                if i[5] == '':
                    i[5] = j[5]
                if i[6] == '':
                    i[6] = j[6]
    newlist_2 = list()
    for i in contacts_list:
        if i not in newlist_2:
            newlist_2.append(i)
    return newlist_2


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
def write_file(contacts_list):
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(contacts_list)
    return contacts_list


if __name__ == '__main__':
    contacts = read_file()
    contacts = phone(contacts)
    contacts = fio(contacts)
    contacts = remove_duplicates(contacts)
    contacts = write_file(contacts)
