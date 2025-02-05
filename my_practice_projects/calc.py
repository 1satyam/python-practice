from tkinter import *
import ast

root=Tk()

i=0
def get_num(num):
    global i
    display.insert(i,num)
    i+=1

def get_operator(operator):
    global i
    length=len(operator)
    display.insert(i,operator)
    i+=length

def clear_all():
    display.delete(0,END)
#for final calculation of the input and error detection
def calculate():
    entire_string=display.get()
    try:
       node=ast.parse(entire_string,mode='eval')
       result=eval(compile(node,'<string>','eval'))
       clear_all()
       display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,'error')
# to delete a single element from the display
def undo():
    entire_string=display.get()
    if entire_string:
        new_string=entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        display.insert(0,"")


display=Entry(root)
display.grid(row=0,columnspan=6)
counter=1
for x in range(3):
    for y in range(3):
        button=Button(root,text=counter,width=2,height=2,command=lambda text=counter: get_num(text))
        button.grid(row=x+1,column=y)
        counter+=1
button=Button(root,text='0', width=2,height=2,command=lambda :get_num(0))
button.grid(row=4,column=1)
operators=['+','-','*','/','%','**','(',')','**2','*3.14']
count=0
for x in range(4):
    for y in range(3):
        if count<len(operators):
            button=Button(root,text=operators[count],width=2,height=2,command=lambda text=operators[count]: get_operator(text))
            count+=1
            button.grid(row=x+1,column=y+3)

Button(root,text='AC',width=2,height=2,command=clear_all).grid(row=4,column=0)
Button(root,text='=',width=2,height=2,command=calculate).grid(row=4,column=2)
Button(root,text='<-',width=2,height=2,command=undo).grid(row=4,column=4)

root.mainloop()
