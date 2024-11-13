from tkinter import*
from tkinter.ttk import*
root = Tk()
root.title("Table Generator")
root.geometry("500x500")

#label text for title
title = Label(root, text="Mathematical Table")
caption = Label(root, text="Number and range:")
caption.place(x=100, y =100)
title.place(x=200, y=10)

# combo box
theNum = StringVar()
numbers = Combobox(root, textvariable=theNum, width= 2)
numbers.place(x=250, y=100)
numbers["values"] = tuple(range(28))# adding combo box dropp down list#

#Radio Buttons
endVal = IntVar()
r10 = Radiobutton(root, text="10", variable= endVal, value=10)
r20 = Radiobutton(root, text="20", variable = endVal, value=20)
r30 = Radiobutton(root, text="20", variable = endVal, value=30)
# set the default value as 10
endVal.set(10)

r10.place(x=300, y=100)
r20.place(x=300, y=150)
r30.place(x=300, y=200)

# Button
def generateMulTable():
    tables=" "
    for i in range(1, endVal.get()+1):
        tables+=str(theNum.get()) + "  X  " + str(i) + "  =  " + str(theNum.get()*i) + "\n"
    table.configure(text=tables)


generate_btn = Button(root, text="Generate", command=generateMulTable)
generate_btn.place(x = 200, y= 300)

table = Label(root, anchor = 'center')
table.place(x=200, y=350)
root.mainloop()