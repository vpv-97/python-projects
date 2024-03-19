from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
import mysql.connector as mysql
from datetime import date

root = Tk()

root.title('Dessert Club Cafe')
root.geometry('1100x800')
root.config(bg='#e8d8c4')
root.resizable(False,False)

font1=('Arial',25,'bold')
font2=('Arial',15,'bold')
font3=('Arial',12,'bold')

bill_frame = Frame(root, width='300', height='300', bg='#fff',relief='solid', bd=1)
bill_frame.place(x=750,y=75)

menu_label = Label(root,text='Dessert Club',fg='#6d2932',bg='#e8d8c4', font=font1)
menu_label.place(x=50,y=10)

img1 = PhotoImage(file = r"images/vanilla.png")
img2 = PhotoImage(file = r"images/pistachio.png")
img3 = PhotoImage(file = r"images/strawberry.png")
img4 = PhotoImage(file = r"images/chocolate.png")
img5 = PhotoImage(file = r"images/mango.png")
img6 = PhotoImage(file = r"images/butterscotch.png")
img7 = PhotoImage(file = r"images/cookiedough.png")
img8 = PhotoImage(file = r"images/cottoncandy.png")
img9 = PhotoImage(file = r"images/blackcurrant.png")


# positioning of curresponding images in the gui 
img1_label = Label(root,image=img1 , text = 'Vanilla\n 40/-', font = font2,width = 150, height=175, compound=TOP, anchor=N, bg='#c7b7a3', fg='#561c24')
img1_label.place(x=50, y=75)

img2_label = Label(root,image=img2, text = 'Pistachio\n 40/-', font = font2,width = 150, height=175, compound=TOP, anchor=N, bg='#c7b7a3', fg='#561c24' )
img2_label.place(x=250, y=75)

img3_label = Label(root,image=img3, text = 'Strawberry\n 40/-', font = font2,width = 150, height=175, compound=TOP, anchor=N, bg='#c7b7a3', fg='#561c24')
img3_label.place(x=450, y=75)

img4_label = Label(root,image=img4, text = 'Chocolate\n 60/-', font = font2,width = 150, height=175, compound=TOP, anchor=N, bg='#c7b7a3', fg='#561c24')
img4_label.place(x=50, y=325)

img5_label = Label(root,image=img5, text = 'Mango\n 60/-', font = font2,width = 150, height=175, compound=TOP, anchor=N, bg='#c7b7a3', fg='#561c24' )
img5_label.place(x=250, y=325)

img6_label = Label(root,image=img6, text = 'Buttter Scotch\n 60/-', font = font2,width = 150, height=175, compound=TOP, anchor=N, bg='#c7b7a3', fg='#561c24')
img6_label.place(x=450, y=325)

img7_label = Label(root,image=img7, text = 'Cookie Dough\n 90/-', font = font2,width = 150, height=175, compound=TOP, anchor=N, bg='#c7b7a3', fg='#561c24' )
img7_label.place(x=50, y=575)

img8_label = Label(root,image=img8, text = 'Cotton Candy\n 90/-', font = font2,width = 150, height=175, compound=TOP, anchor=N, bg='#c7b7a3', fg='#561c24' )
img8_label.place(x=250, y=575)

img9_label = Label(root,image=img9, text = 'Black Currant\n 90/-', font = font2,width = 150, height=175, compound=TOP, anchor=N, bg='#c7b7a3', fg='#561c24' )
img9_label.place(x=450, y=575)

count=('0','1','2','3')
qty_box1 = ttk.Combobox(root, font= font3, values=count,state='readonly',width=10)
qty_box1.place(x=72,y=226)
qty_box1.set(0)

qty_box2 = ttk.Combobox(root, font= font3, values=count,state='readonly',width=10)
qty_box2.place(x=272,y=226)
qty_box2.set(0)

qty_box3 = ttk.Combobox(root, font= font3, values=count,state='readonly',width=10)
qty_box3.place(x=472,y=226)
qty_box3.set(0)

qty_box4 = ttk.Combobox(root, font= font3, values=count,state='readonly',width=10)
qty_box4.place(x=72,y=476)
qty_box4.set(0)

qty_box5 = ttk.Combobox(root, font= font3, values=count,state='readonly',width=10)
qty_box5.place(x=272,y=476)
qty_box5.set(0)

qty_box6 = ttk.Combobox(root, font= font3, values=count,state='readonly',width=10)
qty_box6.place(x=472,y=476)
qty_box6.set(0)

qty_box7 = ttk.Combobox(root, font= font3, values=count,state='readonly',width=10)
qty_box7.place(x=72,y=726)
qty_box7.set(0)

qty_box8 = ttk.Combobox(root, font= font3, values=count,state='readonly',width=10)
qty_box8.place(x=272,y=726)
qty_box8.set(0)

qty_box9 = ttk.Combobox(root, font= font3, values=count,state='readonly',width=10)
qty_box9.place(x=472,y=726)
qty_box9.set(0)


# pricing of respective items are listed inside the list so that we can access it by the index postion
price_list = [40,60,90]
total_price = 0 


# code for doing the payment
def pay():
    global total_price
    if(order_no_entry.get() == ''):
        messagebox.showerror(title='Error',message='Enter the Oreder number.')
    else:
        # total = quantity * values insde the list "price_list"
        total_price = (int(qty_box1.get()) * price_list[0] + 
                        int(qty_box2.get()) * price_list[0] +
                        int(qty_box3.get()) * price_list[0] +
                        int(qty_box4.get()) * price_list[1] +
                        int(qty_box5.get()) * price_list[1] +
                        int(qty_box6.get()) * price_list[1] +
                        int(qty_box7.get()) * price_list[2] +
                        int(qty_box8.get()) * price_list[2] +
                        int(qty_box9.get()) * price_list[2] )

        if(total_price == 0):
            messagebox.showwarning(title="Error",message='Please select any item')
        else:
            # displaying the values inside the billing display
            order = Label(bill_frame,text=f'Order Number: {order_no_entry.get()}', fg='#000', font=font3)
            order.place(x=10, y=50)
            price = Label(bill_frame,text=f'Total Price: Rs{total_price}',fg='#000', font=font3)
            price.place(x=10, y=100)
            date_label= Label(bill_frame,text=f'Date: {date.today()}',fg='#000', font=font3)
            date_label.place(x=10, y=150)


# intializing a new payment
def new():
    order_no_entry.delete(0,END)
    qty_box1.set(0), qty_box2.set(0), qty_box3.set(0)
    qty_box4.set(0), qty_box5.set(0), qty_box6.set(0)
    qty_box7.set(0), qty_box8.set(0), qty_box9.set(0) 


# to save the values inthe bill box to database
def save():
    db_order = order_no_entry.get();
    db_price = str(total_price);
    
    if (order_no_entry.get() == '') :
        messagebox.showerror(title='Error',message='Enter the Oreder number.')
    elif (total_price == 0):
        messagebox.showwarning(title="Error",message='Please select any item')
    else:
        # database : dessert_club
        # table name : sales
        con = mysql.connect(host='localhost', user='root', passwd='1910', port='3307', database='dessert_club')
        cursor = con.cursor()
        cursor.execute("insert into sales values('"+db_order+"','"+db_price+"')")
        cursor.execute("commit")
        messagebox.showinfo(title='Saved', message='Bill has been saved.')
        con.close()
    # f=open(f'{order_no_entry.get()} Bill',"w")
    # f.write(f'Bill Number: {order_no_entry.get()}\n')
    # f.write(f'Total Price: Rs{total_price}\n')
    # f.write(f'Bill Date: {date.today()}')
    

order_no = Label(root,text='Order number',font=font2, fg='#561c24', bg='#c7b7a3',width=18)
order_no.place(x=750, y=400)

order_no_entry = Entry(root,font=font2,fg='#000',bg='#fff',bd=1,width=20)
order_no_entry.place(x=750, y=435)


pay_button = Button(root,command=pay, text="Pay", font=font2, fg="#e9d9c4", bg="#6d2932", width=24, height=2)
pay_button.place(x=750, y=500)

save_button = Button(root,command=save, text="Save", font=font2, fg="#e9d9c4", bg="#6d2932", width=24, height=2)
save_button.place(x=750, y=590)

new_button = Button(root,command=new, text="New", font=font2, fg="#e9d9c4", bg="#6d2932", width=24, height=2)
new_button.place(x=750, y=680)




root.mainloop()

