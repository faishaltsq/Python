import tkinter as tk

def login():
    username = username_entry.get()
    password = password_entry.get()

    # check if the username and password match
    if username == "admin" and password == "password":
        label_status.config(text="Login successful", fg="green")
    else:
        label_status.config(text="Incorrect username or password", fg="red")

root = tk.Tk()
root.title("Login Page")

label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0)

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

label_status = tk.Label(root)
label_status.grid(row=3, column=0, columnspan=2)

root.mainloop()
