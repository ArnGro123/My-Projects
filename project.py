from tkinter import *
from tkinter import ttk, simpledialog
import random as rand


x = 0
root = Tk() #program window
root.title("Password Partner")
root.geometry("600x600")

pass_file = open("passwords.txt","r+") #file for passwords


def password_widget():

    global q_1_entry, q_2_entry, q_3_entry, q_4_entry, q_5_entry
    global listbox_pass, listbox_saved
    global tree, x

    pass_frame = Frame(root) #all widgets on password screen are put into here
    pass_frame.pack()

    tree_frame = Frame(root) #frame for saved passwords
    tree_frame.pack()

    q_1 = Label(pass_frame,text="Favorite Sports Team : ") #questions and entries
    q_1.pack()
    q_1_entry = Entry(pass_frame)
    q_1_entry.pack()

    q_2 = Label(pass_frame,text="Favorite Place : ")
    q_2.pack()
    q_2_entry = Entry(pass_frame)
    q_2_entry.pack()

    q_3 = Label(pass_frame,text="Favorite Book : ")
    q_3.pack()
    q_3_entry = Entry(pass_frame)
    q_3_entry.pack()

    q_4 = Label(pass_frame,text="Special Character : ")
    q_4.pack()
    q_4_entry = Entry(pass_frame)
    q_4_entry.pack()

    q_5 = Label(pass_frame,text="Lucky Number : ")
    q_5.pack()
    q_5_entry = Entry(pass_frame)
    q_5_entry.pack()

    listbox_pass = Listbox(pass_frame) #for password generation
    listbox_pass.pack(pady=10)
    listbox_pass.config(width=50,height=5)

    b_gen = Button(pass_frame,text="GENERATE",command=gen_password) #generate passwords
    b_gen.pack()

    b_select = Button(pass_frame, text="SELECT", command=select_pass) #add to list
    b_select.pack()

    t_scroll = Scrollbar(tree_frame)
    t_scroll.pack(side=RIGHT,fill=Y)

    tree = ttk.Treeview(tree_frame, yscrollcommand=t_scroll.set) #display for saved passwords
    tree['columns'] = ("Site","Password")

    tree.column("#0",width=0)
    tree.column("Site",anchor=W,width=120)
    tree.column("Password",anchor=CENTER,width=120)

    tree.heading("Site",text="Site")
    tree.heading("Password",text="Password")
    tree.pack(pady=10)

    saved_l = pass_file.readlines()
    pass_file.seek(0)

    for i in range(len(saved_l)): #showing preexisting passwords
        tree.insert(parent="",index="end",iid=x,values=(next(pass_file)))
        x+=1


def gen_password():

    global l

    listbox_pass.delete(0,END) #clearing past generations

    q1 = q_1_entry.get() #using phrases from questions
    q1_l = q1.split(" ")
    rand.shuffle(q1_l)

    q2 = q_2_entry.get()
    q2_l = q2.split(" ")
    rand.shuffle(q2_l)

    q3 = q_3_entry.get()
    q3_l = q3.split(" ")
    rand.shuffle(q3_l)

    q4 = q_4_entry.get()
    q4_l = q4.split(" ")
    rand.shuffle(q4_l)

    q5 = q_5_entry.get()
    q5_l = q5.split(" ")
    rand.shuffle(q5_l)

    l = []
    l.append(rand.choice(q1_l))
    l.append(rand.choice(q2_l))
    l.append(rand.choice(q3_l))
    l.append(rand.choice(q4_l))
    l.append(rand.choice(q5_l))
    

    for i in range(5): #showing user generated passwords
        generate()
        listbox_pass.insert(END,s)

    
def generate():

    global s

    rand.shuffle(l) #randomizing

    x = True

    for i in range(len(l)):

        if x==True and l[i].isalpha()==True: #further securing password
            l[i] = l[i].capitalize()
            x = False
        else:
            x = True

    s = ""
    s = s.join(l)

x = 0

def select_pass():

    global saved_l
    global pass_file
    global x
    
    pass_file.seek(0)
    saved_l = pass_file.readlines()

    var = str(listbox_pass.get(ANCHOR)+"\n") #getting user selected pass

    if var not in saved_l:
        
        get_input()
        pass_file.write(user_input+" ")
        pass_file.write(var)
        pass_file.close()
        pass_file = open("passwords.txt","r+")
        
        tree.insert(parent="",index="end",iid=x,values=(user_input,var))
        x+=1
    
    print(saved_l)

def get_input(): #site input from user
    global user_input
    user_input = simpledialog.askstring(title="Input",prompt="What Is This For : ")


def close(): #saving file
    pass_file.close()
    root.destroy()

password_widget()

root.protocol("WM_DELETE_WINDOW",close)

root.mainloop()