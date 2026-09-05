from tables import connect

# CREATE
def create_project(user_id):
    conn = connect()
    c = conn.cursor()

    name = input("Enter project name: ")

    c.execute(
        "INSERT INTO projects(name, user_id) VALUES(?, ?)",
        (name, user_id)
    )

    conn.commit()
    conn.close()
    print("Project created successfully!")

# READ
def view_projects(user_id):
    conn = connect()
    c = conn.cursor()

    c.execute(
        "SELECT id, name FROM projects WHERE user_id=?",
        (user_id,)
    )

    projects = c.fetchall()

    if not projects:
        print("No projects found.")
    else:
        print("\nYour Projects")
        for p in projects:
            print(f"{p[0]}. {p[1]}")

    conn.close()

# UPDATE
def edit_project(user_id):
    view_projects(user_id)

    project_id = input("Project ID: ")
    new_name = input("New project name: ")

    conn = connect()
    c = conn.cursor()

    c.execute(
        "UPDATE projects SET name=? WHERE id=? AND user_id=?",
        (new_name, project_id, user_id)
    )

    conn.commit()
    conn.close()
    print("Project updated!")

# DELETE
def delete_project(user_id):
    view_projects(user_id)

    project_id = input("Project ID to delete: ")

    conn = connect()
    c = conn.cursor()

    c.execute(
        "DELETE FROM projects WHERE id=? AND user_id=?",
        (project_id, user_id)
    )

    conn.commit()
    conn.close()
    print("Project deleted!")