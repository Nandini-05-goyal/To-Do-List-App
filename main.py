# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import tkinter  # to create a window
import pickle   # converts python object into byte stream to store in database
import tkinter.messagebox  # a message box opens as soon as we import this and connect it to root and mainloop

root = tkinter.Tk()
root.title("To-Do List App")

def add_task():
    task = entry_task.get()    # this task help us making an entry
    if task != "":
        listbox_tasks.insert(tkinter.END, task)    # inserting the task at the end means it will keep adding tasks one after another
        entry_task.delete(0, tkinter.END)  # now once one task is entered it will automatically clear the field
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Enter something, empty task cannot be added")

def delete_task():
    try:                          # so this box first tries this, if an error is there displays except block
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Select task to delete")

def load_task():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)  # it will delete everyting in d list box after saving it once so dat it doesnt load again and again
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks to load")

def save_task():      #to saved task we will use pickle module
    tasks = listbox_tasks.get(0, listbox_tasks.size())      # here we are getting the tasks all in one time saved
    pickle.dump(tasks, open("tasks.dat", "wb"))    # saving it in one data file so that later we can load it from there

# Create GUI
frame_tasks = tkinter.Frame(root)   #creates a frame so now listbox doesnt go into root it will be in frame
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=20, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)    #yscrollcommand helps in scrolling up and down through tasks
scrollbar_tasks.config(command=listbox_tasks.yview)

# to enter the data in add task
entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

# Buttons
button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task)
button_delete_task.pack()

button_load_task = tkinter.Button(root, text="Load task", width=48, command=load_task)
button_load_task.pack()

button_save_task = tkinter.Button(root, text="Save task", width=48, command=save_task)
button_save_task.pack()

root.mainloop()
