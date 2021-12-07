def print_str(count_disk_user, begin, end):
    print(f"Переложить диск {count_disk_user} со стержня номер {begin} на стержень номер {end}")


def move(count_disk_user, start=1, finish=3):
    if count_disk_user == 1:
        print_str(count_disk_user, start, finish)
    else:
        middle = 6 - start - finish
        move(count_disk_user - 1, start, middle)
        print_str(count_disk_user, start, finish)
        move(count_disk_user - 1, middle, finish)


count_disk_user = int(input("Введите количество дисков: "))
move(count_disk_user)

# зачёт!
