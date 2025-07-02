from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
import requests

def send():
    def send_msg():
        message=textarea.get(1.0,END)
        number=numberfield.get()
        auth="zg75YVCZE8DakWfX4RtJl3yFqerwTndoSspHQjx0bGKN6IBPL2duMKUxN2l3r5Q8oETsZH7LYfAgXSmF"
        url='https://www.fast2sms.com/dev/bulk'
        params={
            'authorization':auth,
            'message':message,
            'number':number,
            'sender-id':'FSTSMS',
            'route':'p',
            'language':'english'
        }
        response=requests.get(url,params=params)
        dic=response.json()
        result=dic.get('return')
        if result==True:
            messagebox.showinfo('send successfully','Message sent sucessfully')
        else:
            messagebox.showinfo('Error','something went wrong')
        
    root2=Toplevel()
    root2.title("Send BILL")
    root2.config(bg='aqua')
    root2.geometry('485x620+50+50')
    
    logoImage=PhotoImage(file='chat.png')
    label=Label(root2,image=logoImage,bg='aqua')
    label.pack(pady=5)
    
    numberLabel=Label(root2,text='Mobile Number',font=('arial',18,'underline'),bg='aqua',fg='black')
    numberLabel.pack(pady=5)
    numberfield=Entry(root2,font=('helvetica',22,'bold'),bd=3,width=24)
    numberfield.pack(pady=5)
    
    billLabel=Label(root2,text='Bill Detail',font=('arial',18,'underline'),bg='aqua',fg='black')
    billLabel.pack(pady=5)
    textarea=Text(root2,font=('areal',12,'bold'),width=42,height=14)
    textarea.pack(pady=5)
    textarea.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
    
    
    if costoffoodvar.get()!='0 Rs':
        textarea.insert(END,f'Cost of food\t\t\t{priceofFood}Rs\n')
    if costofdrinksvar.get()!='0 Rs':
        textarea.insert(END,f'Cost of Drink\t\t\t{priceofDrinks}Rs\n')
    if costofcakesvar.get()!='0 Rs':    
        textarea.insert(END,f'Cost of Cakes\t\t\t{priceofCake}Rs\n')
        
    textarea.insert(END,f'Sub Total\t\t\t{subtotalofItems}Rs\n')
    textarea.insert(END,f'Service tax\t\t\t{50}Rs\n')
    textarea.insert(END,f'Sub Total\t\t\t{subtotalofItems+50}Rs\n')
    
    sendbutton=Button(root2,text='SEND',font=('arial',19,'bold'),bg='white',bd=7,relief=GROOVE,command=send_msg)
    sendbutton.pack()
    
    root2.mainloop()

def save():
    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    
    bill_data=textReceipt.get(1.0,END)
    url.write(bill_data)
    url.close()
    messagebox.showinfo('Information','Your Bill is succesfully saved')

def receipt():
    global billnumber,date
    textReceipt.delete(1.0,END)
    x=random.randint(100,10000)
    billnumber='Bill'+str(x)
    date=time.strftime('%d/%m/%Y')
    textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
    textReceipt.insert(END,'***************************************************************\n')
    textReceipt.insert(END,'Items:\t\t Cost of Items(Rs)\n')
    textReceipt.insert(END,'***************************************************************\n')
    if e_roti.get()!='0':
        textReceipt.insert(END,f'Roti\t\t{int(e_roti.get())*10}\n\n')

    if e_daal.get()!='0':
        textReceipt.insert(END,f'Daal\t\t{int(e_roti.get())*60}\n\n')

    if e_sabji.get()!='0':
        textReceipt.insert(END,f'Sabji\t\t{int(e_sabji.get())*50}\n\n')

    if e_fish.get()!='0':
        textReceipt.insert(END,f'Fish\t\t{int(e_fish.get())*100}\n\n')

    if e_chicken.get()!='0':
        textReceipt.insert(END,f'Chicken\t\t{int(e_chicken.get())*120}\n\n')
    
    if e_paneer.get()!='0':
        textReceipt.insert(END,f'Paneer\t\t{int(e_paneer.get())*80}\n\n')

    if e_mutton.get()!='0':
        textReceipt.insert(END,f'Mutton\t\t{int(e_mutton.get())*110}\n\n')

    if e_rice.get()!='0':
        textReceipt.insert(END,f'Rice\t\t{int(e_rice.get())*30}\n\n')

    if e_egg.get()!='0':
        textReceipt.insert(END,f'Egg\t\t{int(e_egg.get())*40}\n\n')
    
    if e_lassi.get()!='0':
        textReceipt.insert(END,f'Lassi\t\t{int(e_lassi.get())*50}\n\n')
    
    if e_coffee.get()!='0':
        textReceipt.insert(END,f'Coffee\t\t{int(e_coffee.get())*40}\n\n')

    if e_faluda.get()!='0':
        textReceipt.insert(END,f'Fluda\t\t{int(e_faluda.get())*60}\n\n')

    if e_sikanji.get()!='0':
        textReceipt.insert(END,f'Sikanji\t\t{int(e_sikanji.get())*20}\n\n')

    if e_roohafaza.get()!='0':
        textReceipt.insert(END,f'Roohafaza\t\t{int(e_roohafaza.get())*15}\n\n')

    if e_badammilk.get()!='0':
        textReceipt.insert(END,f'Badammilk\t\t{int(e_badammilk.get())*60}\n\n')

    if e_tea.get()!='0':
        textReceipt.insert(END,f'Tea\t\t{int(e_tea.get())*20}\n\n')

    if e_jaljeera.get()!='0':
        textReceipt.insert(END,f'aljeera\t\t{int(e_jaljeera.get())*20}\n\n')

    if e_colddrink.get()!='0':
        textReceipt.insert(END,f'Colddrink\t\t{int(e_colddrink.get())*40}\n\n')

    if e_oreo.get()!='0':
        textReceipt.insert(END,f'Oreo cake\t\t{int(e_oreo.get())*400}\n\n')

    if e_butterscotch.get()!='0':
        textReceipt.insert(END,f'Butterscotch cake\t\t{int(e_butterscotch.get())*350}\n\n')

    if e_caramel.get()!='0':
        textReceipt.insert(END,f'Caramel cake\t\t{int(e_caramel.get())*450}\n\n')

    if e_vanilla.get()!='0':
        textReceipt.insert(END,f'vanilla cake\t\t{int(e_vanilla.get())*600}\n\n')


    if e_chocklet.get()!='0':
        textReceipt.insert(END,f'Chocklet cake\t\t{int(e_chocklet.get())*450}\n\n')   
    
    if e_pineapple.get()!='0':
        textReceipt.insert(END,f'Pineapple cake\t\t{int(e_pineapple.get())*300}\n\n') 

    if e_blackforest.get()!='0':
        textReceipt.insert(END,f'Blackforest cake\t\t{int(e_blackforest.get())*700}\n\n')   

    if e_brownie.get()!='0':
        textReceipt.insert(END,f'Brownie cake\t\t{int(e_brownie.get())*400}\n\n')  

    if e_redvelvet.get()!='0':
        textReceipt.insert(END,f'Redvelvet cake\t\t{int(e_redvelvet.get())*700}\n\n')  

    textReceipt.insert(END,'***************************************************************\n')

        
    if costoffoodvar.get()!='0 Rs':
        textReceipt.insert(END,f'Cost of food\t\t\t{priceofFood}Rs\n\n')
    if costofdrinksvar.get()!='0 Rs':
        textReceipt.insert(END,f'Cost of Drink\t\t\t{priceofDrinks}Rs\n\n')
    if costofcakesvar.get()!='0 Rs':    
        textReceipt.insert(END,f'Cost of Cakes\t\t\t{priceofCake}Rs\n\n')
        
    textReceipt.insert(END,f'Sub Total\t\t\t{subtotalofItems}Rs\n\n')
    textReceipt.insert(END,f'Service tax\t\t\t{50}Rs\n\n')
    textReceipt.insert(END,f'Sub Total\t\t\t{subtotalofItems+50}Rs\n\n')
    textReceipt.insert(END,'***************************************************************\n')
    


def totalcost():
    global priceofFood,priceofDrinks,priceofCake,subtotalofItems
    item1=int(e_roti.get())                  
    item2=int(e_daal.get())
    item3=int(e_sabji.get())
    item4=int(e_fish.get())
    item5=int(e_chicken.get())
    item6=int(e_paneer.get())
    item7=int(e_mutton.get())
    item8=int(e_rice.get())
    item9=int(e_egg.get())

    item10=int(e_lassi.get())
    item11=int(e_coffee.get())
    item12=int(e_faluda.get())
    item13=int(e_sikanji.get())
    item14=int(e_roohafaza.get())
    item15=int(e_badammilk.get())
    item16=int(e_tea.get())
    item17=int(e_jaljeera.get())
    item18=int(e_colddrink.get())

    item19=int(e_oreo.get())
    item20=int(e_butterscotch.get())
    item21=int(e_caramel.get())
    item22=int(e_vanilla.get())
    item23=int(e_chocklet.get())
    item24=int(e_pineapple.get())
    item25=int(e_blackforest.get())
    item26=int(e_brownie.get())
    item27=int(e_redvelvet.get())

    priceofFood=(item1*10)+(item2*60)+(item3*50)+(item4*100)+(item5*120)+(item6*80)+(item7*110)+(item8*30)+(item9*40)

    priceofDrinks=(item10*50)+(item11*40)+(item12*60)+(item13*20)+(item14*15)+(item15*60)+(item16*20)+(item17*20)+(item18*40)

    priceofCake=(item19*400)+(item20*350)+(item21*450)+(item22*600)+(item23*450)+(item24*300)+(item25*700)+(item26*400)+(item27*700)

    costoffoodvar.set(str(priceofFood)+ 'Rs')
    costofdrinksvar.set(str(priceofDrinks)+ 'Rs')
    costofcakesvar.set(str(priceofCake)+ 'Rs')

    subtotalofItems=priceofFood+priceofDrinks+priceofCake
    subtotalvar.set(str(subtotalofItems)+'Rs')

    servicetaxvar.set('50 Rs')

    totalcost=subtotalofItems+50
    totalcostvar.set(str(totalcost)+'Rs')


def roti():
    if var1.get()==1:
        textroti.config(state=NORMAL)
        textroti.delete(0,END )
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')

def daal():
    if var2.get()==1:
        textdaal.config(state=NORMAL)
        textdaal.delete(0,END )
        textdaal.focus()
    else:
        textdaal.config(state=DISABLED)
        e_daal.set('0')

def sabji():
    if var3.get()==1:
        textsabji.config(state=NORMAL)
        textsabji.delete(0,END )
        textsabji.focus()
    else:
        textsabji.config(state=DISABLED)
        e_sabji.set('0')

def fish():
    if var4.get()==1:
        textfish.config(state=NORMAL)
        textfish.delete(0,END )
        textfish.focus()
    else:
        textfish.config(state=DISABLED)
        e_fish.set('0')

def chicken():
    if var5.get()==1:
        textchicken.config(state=NORMAL)
        textchicken.delete(0,END )
        textchicken.focus()
    else:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')

def paneer():
    if var6.get()==1:
        textpaneer.config(state=NORMAL)
        textpaneer.delete(0,END )
        textpaneer.focus()
    else:
        textpaneer.config(state=DISABLED)
        e_paneer.set('0')

def mutton():
    if var7.get()==1:
        textmutton.config(state=NORMAL)
        textmutton.delete(0,END )
        textmutton.focus()
    else:
        textmutton.config(state=DISABLED)
        e_mutton.set('0')

def rice():
    if var8.get()==1:
        textrice.config(state=NORMAL)
        textrice.delete(0,END )
        textrice.focus()
    else:
        textrice.config(state=DISABLED)
        e_rice.set('0')

def egg():
    if var9.get()==1:
        textegg.config(state=NORMAL)
        textegg.delete(0,END )
        textegg.focus()
    else:
        textegg.config(state=DISABLED)
        e_egg.set('0')


def lassi():
    if var10.get()==1:
        textlassi.config(state=NORMAL)
        textlassi.delete(0,END )
        textlassi.focus()
    else:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')

def coffee():
    if var11.get()==1:
        textcoffee.config(state=NORMAL)
        textcoffee.delete(0,END )
        textcoffee.focus()
    else:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')

def faluda():
    if var12.get()==1:
        textfaluda.config(state=NORMAL)
        textfaluda.delete(0,END )
        textfaluda.focus()
    else:
        textfaluda.config(state=DISABLED)
        e_faluda.set('0')

def sikanji():
    if var13.get()==1:
        textsikanji.config(state=NORMAL)
        textsikanji.delete(0,END )
        textsikanji.focus()
    else:
        textsikanji.config(state=DISABLED)
        e_sikanji.set('0')

def roohafaza():
    if var14.get()==1:
        textroohafaza.config(state=NORMAL)
        textroohafaza.delete(0,END )
        textroohafaza.focus()
    else:
        textroohafaza.config(state=DISABLED)
        e_roohafaza.set('0')

def badammilk():
    if var15.get()==1:
        textbadammilk.config(state=NORMAL)
        textbadammilk.delete(0,END )
        textbadammilk.focus()
    else:
        textbadammilk.config(state=DISABLED)
        e_badammilk.set('0')

def tea():
    if var16.get()==1:
        texttea.config(state=NORMAL)
        texttea.delete(0,END )
        texttea.focus()
    else:
        texttea.config(state=DISABLED)
        e_tea.set('0')

def jaljeera():
    if var17.get()==1:
        textjaljeera.config(state=NORMAL)
        textjaljeera.delete(0,END )
        textjaljeera.focus()
    else:
        textjaljeera.config(state=DISABLED)
        e_jaljeera.set('0')

def colddrink():
    if var18.get()==1:
        textcolddrink.config(state=NORMAL)
        textcolddrink.delete(0,END )
        textcolddrink.focus()
    else:
        textcolddrink.config(state=DISABLED)
        e_colddrink.set('0')

def oreo():
    if var19.get()==1:
        textoreo.config(state=NORMAL)
        textoreo.delete(0,END )
        textoreo.focus()
    else:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')

def butterscotch():
    if var20.get()==1:
        textbutterscotch.config(state=NORMAL)
        textbutterscotch.delete(0,END )
        textbutterscotch.focus()
    else:
        textbutterscotch.config(state=DISABLED)
        e_butterscotch.set('0')

def caramel():
    if var21.get()==1:
        textcaramel.config(state=NORMAL)
        textcaramel.delete(0,END )
        textcaramel.focus()
    else:
        textcaramel.config(state=DISABLED)
        e_caramel.set('0')

def vanilla():
    if var22.get()==1:
        textvanilla.config(state=NORMAL)
        textvanilla.delete(0,END )
        textvanilla.focus()
    else:
        textvanilla.config(state=DISABLED)
        e_vanilla.set('0')

def chocklet():
    if var23.get()==1:
        textchocklet.config(state=NORMAL)
        textchocklet.delete(0,END )
        textchocklet.focus()
    else:
        textchocklet.config(state=DISABLED)
        e_chocklet.set('0')

def pineapple():
    if var24.get()==1:
        textpineapple.config(state=NORMAL)
        textpineapple.delete(0,END )
        textpineapple.focus()
    else:
        textpineapple.config(state=DISABLED)
        e_pineapple.set('0')

def blackforest():
    if var25.get()==1:
        textblackforest.config(state=NORMAL)
        textblackforest.delete(0,END )
        textblackforest.focus()
    else:
        textblackforest.config(state=DISABLED)
        e_blackforest.set('0')

def brownie():
    if var26.get()==1:
        textbrownie.config(state=NORMAL)
        textbrownie.delete(0,END )
        textbrownie.focus()
    else:
        textbrownie.config(state=DISABLED)
        e_brownie.set('0')

def redvelvet():
    if var27.get()==1:
        textredvelvet.config(state=NORMAL)
        textredvelvet.delete(0,END )
        textredvelvet.focus()
    else:
        textredvelvet.config(state=DISABLED)
        e_redvelvet.set('0')


root=Tk()
root.geometry('1285x690')
root.resizable(0,0)
root.title('Restaurant Management System created by Nishant Kumar')
root.config(bg='aqua')

topFrame=Frame(root,bd=10,relief=RIDGE,bg='green')
topFrame.pack(side=TOP)

lableTitle=Label(topFrame,text='Restaurant Managment System',font=('areal',30,'bold'),fg='yellow',bg='red',bd=9,width=51)
lableTitle.grid(row=0,column=0)

#frames

menuFrame=Frame(root,bd=10,relief=RIDGE,bg='aqua')
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,pady=10,bg='aqua')
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame,text='Food',font=('areal',19,'bold'),bd=10,relief=RIDGE,fg='green')
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame,text='Drinks',font=('areal',19,'bold'),bd=10,relief=RIDGE,fg='green')
drinksFrame.pack(side=LEFT)

cakesFrame=LabelFrame(menuFrame,text='Cakes',font=('areal',19,'bold'),bd=10,relief=RIDGE,fg='green')
cakesFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE,bg='aqua')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='aqua')
calculatorFrame.pack()

recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='aqua')
recieptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='aqua')
buttonFrame.pack()

#Variable
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()

e_roti=StringVar()
e_daal=StringVar()
e_sabji=StringVar()
e_fish=StringVar()
e_chicken=StringVar()
e_paneer=StringVar()
e_mutton=StringVar()
e_rice=StringVar()
e_egg=StringVar()

e_lassi=StringVar()
e_coffee=StringVar()
e_faluda=StringVar()
e_sikanji=StringVar()
e_roohafaza=StringVar()
e_badammilk=StringVar()
e_tea=StringVar()
e_jaljeera=StringVar()
e_colddrink=StringVar()

e_oreo=StringVar()
e_butterscotch=StringVar()
e_caramel=StringVar()
e_vanilla=StringVar()
e_chocklet=StringVar()
e_pineapple=StringVar()
e_blackforest=StringVar()
e_brownie=StringVar()
e_redvelvet=StringVar()

costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()

e_roti.set('0')
e_daal.set('0')
e_sabji.set('0')
e_fish.set('0')
e_chicken.set('0')
e_paneer.set('0')
e_mutton.set('0')
e_rice.set('0')
e_egg.set('0')

e_lassi.set('0')
e_coffee.set('0')
e_faluda.set('0')
e_sikanji.set('0')
e_roohafaza.set('0')
e_badammilk.set('0')
e_tea.set('0')
e_jaljeera.set('0')
e_colddrink.set('0')

e_oreo.set('0')
e_butterscotch.set('0')
e_caramel.set('0')
e_vanilla.set('0')
e_chocklet.set('0')
e_pineapple.set('0')
e_blackforest.set('0')
e_brownie.set('0')
e_redvelvet.set('0')

##FOOD

roti=Checkbutton(foodFrame,text='Roti',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1,command=roti)
roti.grid(row=0,column=0,sticky=W)

daal=Checkbutton(foodFrame,text='Daal',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2,command=daal)
daal.grid(row=1,column=0,sticky=W)

sabji=Checkbutton(foodFrame,text='Sabji',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3,command=sabji)
sabji.grid(row=2,column=0,sticky=W)

fish=Checkbutton(foodFrame,text='Fish',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4,command=fish)
fish.grid(row=3,column=0,sticky=W)

chicken=Checkbutton(foodFrame,text='Chicken',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5,command=chicken)
chicken.grid(row=4,column=0,sticky=W)

paneer=Checkbutton(foodFrame,text='Paneer',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6,command=paneer)
paneer.grid(row=5,column=0,sticky=W)

mutton=Checkbutton(foodFrame,text='Mutton',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7,command=mutton)
mutton.grid(row=6,column=0,sticky=W)

rice=Checkbutton(foodFrame,text='Rice',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8,command=rice)
rice.grid(row=7,column=0,sticky=W)

egg=Checkbutton(foodFrame,text='Eggs',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var9,command=egg)
egg.grid(row=8,column=0,sticky=W)

#Entryfirld for foods

textroti=Entry(foodFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_roti)
textroti.grid(row=0,column=1)

textdaal=Entry(foodFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_daal)
textdaal.grid(row=1,column=1)

textsabji=Entry(foodFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_sabji)
textsabji.grid(row=2,column=1)

textfish=Entry(foodFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_fish)
textfish.grid(row=3,column=1)

textchicken=Entry(foodFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_chicken)
textchicken.grid(row=4,column=1)

textpaneer=Entry(foodFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_paneer)
textpaneer.grid(row=5,column=1)

textmutton=Entry(foodFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_mutton)
textmutton.grid(row=6,column=1)

textrice=Entry(foodFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_rice)
textrice.grid(row=7,column=1)

textegg=Entry(foodFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_egg)
textegg.grid(row=8,column=1)


##Drinks

lassi=Checkbutton(drinksFrame,text='Lassi',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10,command=lassi)
lassi.grid(row=0,column=0,sticky=W)

coffee=Checkbutton(drinksFrame,text='Coffee',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11,command=coffee)
coffee.grid(row=1,column=0,sticky=W)

faluda=Checkbutton(drinksFrame,text='Faluda',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12,command=faluda)
faluda.grid(row=2,column=0,sticky=W)

sikanji=Checkbutton(drinksFrame,text='Sikanji',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13,command=sikanji)
sikanji.grid(row=3,column=0,sticky=W)

roohafaza=Checkbutton(drinksFrame,text='Roohafaza',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14,command=roohafaza)
roohafaza.grid(row=4,column=0,sticky=W)

badammilk=Checkbutton(drinksFrame,text='Badammilk',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15,command=badammilk)
badammilk.grid(row=5,column=0,sticky=W)

tea=Checkbutton(drinksFrame,text='Tea',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16,command=tea)
tea.grid(row=6,column=0,sticky=W)

jaljeera=Checkbutton(drinksFrame,text='Jaljeera',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17,command=jaljeera)
jaljeera.grid(row=7,column=0,sticky=W)

colddrink=Checkbutton(drinksFrame,text='Colddrink',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var18,command=colddrink)
colddrink.grid(row=8,column=0,sticky=W)


#Entryfielf for drink items

textlassi=Entry(drinksFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_lassi)
textlassi.grid(row=0,column=1)

textcoffee=Entry(drinksFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_coffee)
textcoffee.grid(row=1,column=1)

textfaluda=Entry(drinksFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_faluda)
textfaluda.grid(row=2,column=1)

textsikanji=Entry(drinksFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_sikanji)
textsikanji.grid(row=3,column=1)

textroohafaza=Entry(drinksFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_roohafaza)
textroohafaza.grid(row=4,column=1)

textbadammilk=Entry(drinksFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_badammilk)
textbadammilk.grid(row=5,column=1)

texttea=Entry(drinksFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_tea)
texttea.grid(row=6,column=1)

textjaljeera=Entry(drinksFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_jaljeera)
textjaljeera.grid(row=7,column=1)

textcolddrink=Entry(drinksFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_colddrink)
textcolddrink.grid(row=8,column=1)


#Cakes

oreocake=Checkbutton(cakesFrame,text='Oreo',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var19,command=oreo)
oreocake.grid(row=0,column=0,sticky=W)

butterscotchcake=Checkbutton(cakesFrame,text=' Butterscotch',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var20,command=butterscotch)
butterscotchcake.grid(row=1,column=0,sticky=W)

caramelcake=Checkbutton(cakesFrame,text='Caramel',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var21,command=caramel)
caramelcake.grid(row=2,column=0,sticky=W)

vanillacake=Checkbutton(cakesFrame,text='Vanilla',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var22,command=vanilla)
vanillacake.grid(row=3,column=0,sticky=W)

chockletcake=Checkbutton(cakesFrame,text='Chocklet',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var23,command=chocklet)
chockletcake.grid(row=4,column=0,sticky=W)

pineapplecake=Checkbutton(cakesFrame,text='Pineapple',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var24,command=pineapple)
pineapplecake.grid(row=5,column=0,sticky=W)

blackforestcake=Checkbutton(cakesFrame,text='blackforest',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var25,command=blackforest)
blackforestcake.grid(row=6,column=0,sticky=W)

browniecake=Checkbutton(cakesFrame,text='Brownie',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var26,command=brownie)
browniecake.grid(row=7,column=0,sticky=W)

redvelvetcake=Checkbutton(cakesFrame,text='Red Velvet',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var27,command=redvelvet)
redvelvetcake.grid(row=8,column=0,sticky=W)



#Entryfield for cakes

textoreo=Entry(cakesFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_oreo)
textoreo.grid(row=0,column=1)

textbutterscotch=Entry(cakesFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_butterscotch)
textbutterscotch.grid(row=1,column=1)

textcaramel=Entry(cakesFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_caramel)
textcaramel.grid(row=2,column=1)

textvanilla=Entry(cakesFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_vanilla)
textvanilla.grid(row=3,column=1)

textchocklet=Entry(cakesFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_chocklet)
textchocklet.grid(row=4,column=1)

textpineapple=Entry(cakesFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_pineapple)
textpineapple.grid(row=5,column=1)

textblackforest=Entry(cakesFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_blackforest)
textblackforest.grid(row=6,column=1)

textbrownie=Entry(cakesFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_brownie)
textbrownie.grid(row=7,column=1)

textredvelvet=Entry(cakesFrame,font=('areal',18,'bold'),bd=7,width=7,state=DISABLED,textvariable=e_redvelvet)
textredvelvet.grid(row=8,column=1)

#Costlabel and enteyfield

labelcostoffood=Label(costFrame,text='Cost of food',font=('arial',14,'bold'),fg='green',bg='aqua')
labelcostoffood.grid(row=0,column=0)

textcostoffood=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textcostoffood.grid(row=0,column=1,padx=41)

labelcostofdrink=Label(costFrame,text='Cost of drink',font=('arial',14,'bold'),fg='green',bg='aqua')
labelcostofdrink.grid(row=1,column=0)

textcostofdrink=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinksvar)
textcostofdrink.grid(row=1,column=1,padx=41)

labelcostofcakes=Label(costFrame,text='Cost of cakes',font=('arial',14,'bold'),fg='green',bg='aqua')
labelcostofcakes.grid(row=2,column=0)

textcostofcakes=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofcakesvar)
textcostofcakes.grid(row=2,column=1,padx=41)

labelsubTotle=Label(costFrame,text='Total',font=('arial',14,'bold'),fg='green',bg='aqua')
labelsubTotle.grid(row=0,column=2)

textsubTotle=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textsubTotle.grid(row=0,column=3,padx=41)

labelserviceTax=Label(costFrame,text='service Tax',font=('arial',14,'bold'),fg='green',bg='aqua')
labelserviceTax.grid(row=1,column=2)

textserviceTax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textserviceTax.grid(row=1,column=3,padx=41)

labeltotalcost=Label(costFrame,text='Total cost',font=('arial',14,'bold'),fg='green',bg='aqua')
labeltotalcost.grid(row=2,column=2)

texttotalcost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
texttotalcost.grid(row=2,column=3,padx=41)

#Button

buttonTotal=Button(buttonFrame,text='Total',font=('areal',14,'bold'),fg='green',bg='aqua',bd=3,command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('areal',14,'bold'),fg='green',bg='aqua',bd=3,command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('areal',14,'bold'),fg='green',bg='aqua',bd=3,command=save)
buttonSave.grid(row=0,column=2)

buttonsend=Button(buttonFrame,text='Send',font=('areal',14,'bold'),fg='green',bg='aqua',bd=3,command=send)
buttonsend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('areal',14,'bold'),fg='green',bg='aqua',bd=3)
buttonReset.grid(row=0,column=4)

#Text area for receipt

textReceipt=Text(recieptFrame,font=('areal',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)

#Calculator

operator=''
def buttonClick(numbers):
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''

calculatorField=Entry(calculatorFrame,font=('areal',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('areal',16,'bold'),fg='green',bg='aqua',bd=6,width=6,command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('areal',16,'bold'),fg='green',bg='aqua',bd=6,width=6,command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('areal',16,'bold'),fg='green',bg='aqua',bd=6,width=6,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame,text='+',font=('areal',16,'bold'),fg='green',bg='aqua',bd=6,width=6,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('areal',16,'bold'),fg='green',bg='aqua',bd=6,width=6,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('areal',16,'bold'),fg='white',bg='red',bd=6,width=6,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('areal',16,'bold'),fg='white',bg='red',bd=6,width=6,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,text='-',font=('areal',16,'bold'),fg='green',bg='aqua',bd=6,width=6,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('areal',16,'bold'),fg='green',bg='aqua',bd=6,width=6,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('areal',16,'bold'),fg='white',bg='red',bd=6,width=6,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('areal',16,'bold'),fg='white',bg='red',bd=6,width=6,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMul=Button(calculatorFrame,text='*',font=('areal',16,'bold'),fg='green',bg='aqua',bd=6,width=6,command=lambda:buttonClick('*'))
buttonMul.grid(row=3,column=3)

buttonAns=Button(calculatorFrame,text='Ans',font=('areal',16,'bold'),fg='green',bg='aqua',bd=6,width=6,command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text='Clear',font=('areal',16,'bold'),fg='green',bg='aqua',bd=6,width=6,command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('areal',16,'bold'),fg='green',bg='aqua',bd=6,width=6,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame,text='/',font=('areal',16,'bold'),fg='green',bg='aqua',bd=6,width=6,command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)


root.mainloop()
 