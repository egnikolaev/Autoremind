import sqlite3
runadd = "да"
userid = input("Введите id: ")

HELP = """
help - справка
add - добавление задачи
show - показать список задач
random -добавить случайную задачу
delete - удалить задачу
info -дополнительная информация
"""

INFO = """
TELEGRAM REMINDER BOT v0.1
Связь с разработчиком
nikolaev.eg-a@yandex.ru
@eg_nikolaev
"""

print(HELP)

run = True
while run:
    command = input("Введите команду: ")
    if command.lower() == "help":
        print(HELP)

    elif command.lower() == "info":
        print(INFO)

    elif command.lower() == "add":
        while runadd == "да":
            tasklist = []
            taskname = input("Введите задачу: ")
            taskdate = input("Введите дату: ")
            tasktime = input("Введите время: ")


            class TaskMaster:
                """Создание класса для подробного описания задачи"""

                def __init__(self, name, date, time):
                    """свойства задачи"""
                    self.name = taskname
                    self.date = taskdate
                    self.time = tasktime

            tasklist.append(TaskMaster(taskname, taskdate, tasktime))

            con = sqlite3.connect(f"tasktabletest{userid}.db")
            cur = con.cursor()
            cur.execute(f"""CREATE TABLE IF NOT EXISTS tasktabletest{userid}(
               taskname TEXT,
               taskdate TEXT,
               tasktime TEXT);
            """)

            con.commit()

            query = f"""INSERT INTO tasktabletest{userid}(taskname, taskdate, tasktime) VALUES (?, ?, ?)"""
            data = (
                (tasklist[0].name),
                (tasklist[0].date),
                (tasklist[0].time)
            )
            with con:
                con.execute(query, data)
            tasklist.clear()

            runadd = input("Добавить еще?(да/нет): ")
            if runadd.lower == "нет":
                break
            print("Все добавили")

    elif command.lower() == "show":
        def showfunc():
            con = sqlite3.connect(f"tasktabletest{userid}.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM tasktabletest{userid}")

            with con:
                rows = cur.fetchall()
                i = 1
                for row in rows:
                    print(i, "Задача", row[0], "запланированна на", row[1], "в", row[2], ".")
                    i = i + 1
        showfunc()

    elif command.lower() == "delete":
        showfunc()

        delltask = input("Введите название задачи на удаление: ")

        cur.execute(f"DELETE FROM tasktabletest{userid} WHERE taskname=?", (delltask,))
        con.commit()
        print(f"Задача {delltask} удалено")







