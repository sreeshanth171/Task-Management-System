from tables import connect

# CREATE
def add_task(user_id):
    conn = connect()
    c = conn.cursor()

    c.execute(
        "SELECT id, name FROM projects WHERE user_id=?",
        (user_id,)
    )

    projects = c.fetchall()

    if not projects:
        print("Create a project first!")
        conn.close()
        return

    print("\nProjects")
    for p in projects:
        print(f"{p[0]}. {p[1]}")

    project_id = input("Project ID: ")

    title = input("Task title: ")
    description = input("Description: ")
    due_date = input("Due date (DD-MM-YYYY): ")
    priority = input("Priority (High/Medium/Low): ")

    c.execute("""
        INSERT INTO tasks
        (title, description, due_date, priority, project_id)
        VALUES(?,?,?,?,?)
    """, (title, description, due_date, priority, project_id))

    conn.commit()
    conn.close()
    print("Task added!")

# READ
def view_tasks(user_id):
    conn = connect()
    c = conn.cursor()

    c.execute("""
        SELECT
        tasks.id,
        tasks.title,
        projects.name,
        tasks.status,
        tasks.priority,
        tasks.due_date
        FROM tasks
        JOIN projects
        ON tasks.project_id = projects.id
        WHERE projects.user_id=?
    """, (user_id,))

    rows = c.fetchall()

    if not rows:
        print("No tasks.")
    else:
        print("\nYour Tasks\n")
        for r in rows:
            print(f"""
ID       : {r[0]}
Title    : {r[1]}
Project  : {r[2]}
Status   : {r[3]}
Priority : {r[4]}
Due Date : {r[5]}
-------------------------
""")

    conn.close()

# UPDATE STATUS
def update_task(user_id):
    view_tasks(user_id)

    task_id = input("Task ID: ")
    status = input("Status (Pending/In Progress/Completed): ")

    conn = connect()
    c = conn.cursor()

    c.execute("""
        UPDATE tasks
        SET status=?
        WHERE id IN (
            SELECT tasks.id
            FROM tasks
            JOIN projects
            ON tasks.project_id=projects.id
            WHERE projects.user_id=?
        )
        AND id=?
    """, (status, user_id, task_id))

    conn.commit()
    conn.close()
    print("Status updated!")

# EDIT DETAILS
def edit_task(user_id):
    view_tasks(user_id)

    task_id = input("Task ID: ")

    title = input("New title: ")
    description = input("New description: ")
    due = input("New due date: ")
    priority = input("Priority: ")

    conn = connect()
    c = conn.cursor()

    c.execute("""
        UPDATE tasks
        SET title=?, description=?, due_date=?, priority=?
        WHERE id=?
    """, (title, description, due, priority, task_id))

    conn.commit()
    conn.close()
    print("Task edited!")

# DELETE
def delete_task(user_id):
    view_tasks(user_id)

    task_id = input("Task ID: ")

    conn = connect()
    c = conn.cursor()

    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))

    conn.commit()
    conn.close()
    print("Task deleted!")