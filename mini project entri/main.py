from tables import create_tables
from auth import register, login

from Project import (
    create_project,
    view_projects,
    edit_project,
    delete_project
)

from task import (
    add_task,
    view_tasks,
    update_task,
    edit_task,
    delete_task
)

create_tables()

while True:

    print("\n===== TASK MANAGER =====")
    print("1.Register")
    print("2.Login")
    print("3.Exit")

    choice = input("Choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        user_id = login()

        if user_id:

            while True:

                print("""
====== DASHBOARD ======

1.Create Project
2.View Projects
3.Edit Project
4.Delete Project

5.Add Task
6.View Tasks
7.Update Task Status
8.Edit Task
9.Delete Task

0.Logout
""")

                op = input("Choose: ")

                if op == "1":
                    create_project(user_id)

                elif op == "2":
                    view_projects(user_id)

                elif op == "3":
                    edit_project(user_id)

                elif op == "4":
                    delete_project(user_id)

                elif op == "5":
                    add_task(user_id)

                elif op == "6":
                    view_tasks(user_id)

                elif op == "7":
                    update_task(user_id)

                elif op == "8":
                    edit_task(user_id)

                elif op == "9":
                    delete_task(user_id)

                elif op == "0":
                    break

                else:
                    print("Invalid")

    elif choice == "3":
        print("Goodbye!")
        break