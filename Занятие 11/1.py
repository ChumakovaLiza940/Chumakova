from tkinter import*
import json
import requests


def but():
    with open("C:\\Users\\555\\Desktop\\11.txt","w") as file:
        user = txtField.get()
        url = f"https://api.github.com/users/{user}"
        userInfo = requests.get(url).json()
        slovar = ['company', 'created_at', 'email', 'id', 'name', 'url']
        data = userInfo.keys()
        for i in data:
            if i in slovar:
                file.write(f"{i}:{userInfo[i]}" + '\n')
    head.configure(text = "Данніе записаніе в файл")


root = Tk()
root.title('Гит введите')
root.geometry('600x300')
root["bg"] = "grey"
head = Label(root, bg = "grey", fg = "white", text = 'ГИТ АЙДИ', font = ('Times new roman', 22))
head.pack(expand=True)
txtField = Entry(root,width=40,font=('Times new roman', 18))
txtField.pack(expand=True)
button = Button(root, bg = "grey", fg = "white", text = 'Нажми на меня',command = but)
button.pack(expand=True)
root.mainloop()