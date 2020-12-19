import tkinter
from tkinter import*
from tkinter.ttk import*
###################################################variables
cad_a=0
can_anm="CANDIDATE 1"#change candidate name here
cad_b=0
can_bnm="CANDIDATE 2"#change candidate name here
nov=0
elec_name="ELECTION FOR BEST CANDIDATE"
Vlist=()
v_id=0
v_ki=0
a_id=0
a_ki=0
vtmain='{can1:'
adm_list="{'aaarc':'aaarcmade'}"
####################################################password
def vpwrdcal(y):
        k=((y*10)-1000)*10
        if(k<0):
            k*=-1
        else:
            k*=1
        return k
###################################################functions
def aftervot():
    av = tkinter.Toplevel()
    #av.iconbitmap('cpy.ico')
    av.config(bg='black')
    av.geometry('400x300+350+200')
    av.title('Completed')
    av.resizable(0, 0)
    lab1 = tkinter.Label(av, text='THANK YOU\nYour VOTE Has been Accepted\nPlease Close The Window', fg='white', bg='black',font={'Arial',40})
    lab1.pack(padx=60, pady=70)
    labm = tkinter.Label(av, text="Thanks for not wasting your vote", font={'Arial', 32}, bg='black', fg='#ccffff')
    labm.pack(padx=10, pady=10)

"""def admin1():
    global cad_b
    global cad_a
    print(cad_a,cad_b,nov)"""####this was used to check the results

def morefun():##################___________use to find default functions_____________

    morefn=tkinter.Toplevel()
    #morefn.iconbitmap('cpy.ico')
    morefn.config(bg='black')
    morefn.geometry('400x200')
    morefn.title('NO FUNCTION ASSIGNED')
    morefn.resizable(0,0)
    lab1=tkinter.Label(morefn,text='No Function assigned yet Please Close this window ',fg='white',bg='black')
    lab1.pack(padx=60,pady=70)
def votingmain():
    global nov
    global can_anm
    a1=can_anm
    global can_bnm
    b1=can_bnm
    vtmfn = tkinter.Toplevel()
    #vtmfn.iconbitmap('cpy.ico')
    vtmfn.config(bg='black')
    vtmfn.geometry('400x400+275+125')
    vtmfn.title('voting')
    vtmfn.resizable(0, 0)
    title1 = tkinter.Label(vtmfn, text=elec_name, bg='black', fg='#ccffff', font={'Arial', 22})
    title1.pack(padx=5, pady=5)
    lab1vm = tkinter.Label(vtmfn,text='Click on the candidate name to vote',fg='#66ffff',bg='black',font={'Arial', 22})
    lab1vm.pack(padx=20,pady=20)

    def vc1():
        global nov
        global cad_a
        cad_a += 1
        nov += 1
        vtmfn.destroy()
        aftervot()

    def vc2():
        global nov
        global cad_b
        cad_b += 1
        nov += 1
        vtmfn.destroy()
        aftervot()
    bc1=tkinter.Button(vtmfn,text=a1,bg='black',fg='#ff751a',relief=FLAT,command= vc1,font={'Arial',20})
    bc1.pack()
    bc2=tkinter.Button(vtmfn,text=b1,bg='black',fg='#4da6ff',relief=FLAT,command= vc2,font={'Arial',20})
    bc2.pack()




def votinglogin():
    vtfn = tkinter.Toplevel()
    #vtfn.iconbitmap('cpy.ico')
    vtfn.config(bg='black')
    vtfn.geometry('400x400+275+125')
    vtfn.title('LOGIN FOR VOTING')
    vtfn.resizable(0, 0)
    l4=tkinter.Label(vtfn,text='ENTER VOTER IDNUMBER', fg='#ccffff', bg='black',font={'Arial', 16})
    l4.pack(pady=25,padx=15)
    lab1vl = tkinter.Entry(vtfn)
    lab1vl.pack(padx=60, pady=15)
    lr = tkinter.Label(vtfn, text='ENTER KEY', fg='#ccffff', bg='black',font={'Arial', 16})
    lr.pack(pady=25, padx=15)
    lab1vk=tkinter.Entry(vtfn)
    lab1vk.pack()
    def checklogin():
        """a_id = lab1vl.get()
        a_key =lab1vk.get()
        if (a_id == 'aaarc' and a_key == 'aaarcmade'):  ###############this is a trail version in final version use dict
            adl1 = tkinter.Button(vtfn, text='Continue to voting screen', bg='black', fg='#e6b800', relief=FLAT, command=votingmain,font={'Arial', 38})
            adl1.pack()
        else:
            l8 = tkinter.Labe(vtfn, text='INVALID CREDENTIALS', fg='#ccffff', bg='black')
            l3.pack(pady=5, padx=5)"""

        v_id=int(lab1vl.get())#@must be 8 digit
        v_key=int(lab1vk.get())#must be 4digit
        #print(type(v_key),type(v_id),v_id)
        global Vlist
        Vlist=list(Vlist)
        vk_cal=vpwrdcal(v_id)###########################formula for voter key
        #print(vk_cal)
        if(v_key==vk_cal):
            if(Vlist.count(v_id)==0):
                Vlist.append(v_id)
                Vlist=tuple(Vlist)
                #print(Vlist,v_id)
                votingmain()
                vtfn.destroy()

            else:
                l3 = tkinter.Label(vtfn, text='Vote has already been cast for this Voter Id', fg='#ccffff', bg='black',font={'Arial', 15})
                l3.pack(pady=5, padx=5)
        else:
            l8 = tkinter.Label(vtfn, text='INVALID CREDENTIALS', fg='#ccffff', bg='black',font={'Arial', 15})
            l8.pack(pady=5,padx=5)

    checkbtn = tkinter.Button(vtfn, text='Check', bg='black', fg='#e6b800', relief=FLAT, command=checklogin,font={'Arial', 38})
    checkbtn.pack()
#######################################################admin_stuff
def tellres():
    global nov
    global cad_b
    global cad_a
    global can_anm
    global can_bnm
    an=can_anm
    bn=can_bnm
    a=cad_a
    b=cad_b
    reswin= tkinter.Toplevel()
    #reswin.iconbitmap('cpy.ico')
    reswin.config(bg='black')
    reswin.geometry('400x400+275+100')
    reswin.title('ADMIN LOGIN')
    reswin.resizable(0, 0)
    if a>b:
        p= (a/nov)*100
        res="Winner of election is: "+an+"\nWith "+str(p)+" percentage of all votes"

    elif b>a:
        p = (b/nov)*100
        res = "Winner of election is: " + bn + "\nWith " +str(p) + " percentage of all votes"
    else:
        res="It is draw a Re-Election time!!!"
    tl2 = tkinter.Label(reswin, text=res, fg='#ccffff', bg='black',font=48)
    tl2.pack(pady=20, padx=20)
##########################################################################functions inside settings
def changecad1():#change candidate 1 name
    chnc1 = tkinter.Toplevel()
    #chnc1.iconbitmap('cpy.ico')
    chnc1.config(bg='black')
    chnc1.geometry('400x400+300+100')
    chnc1.title('ADMIN SETTINGS')
    chnc1.resizable(0, 0)
    tl1 = tkinter.Label(chnc1, text='FOR ADMINS ONLY\n\n\n ENTER NEW NAME OF CANDIDATE 1', fg='#ccffff', bg='black',font={'Arial', 15})
    tl1.pack(pady=20, padx=20)
    nc1n = tkinter.Entry(chnc1)
    nc1n.pack(pady=2)

    def update_c1_name():
        global can_anm
        n = nc1n.get()
        can_anm = n
        tl1 = tkinter.Label(chnc1, text='NAME UPDATED', fg='#ccffff', bg='black',font={'Arial', 15})
        tl1.pack(pady=15, padx=20)

    but = tkinter.Button(chnc1, text='Change', bg='black', fg='yellow', command=update_c1_name)
    but.pack(pady=15)


def changecad2():#change candidate 2 name
    chnc2 = tkinter.Toplevel()
    #chnc2.iconbitmap('cpy.ico')
    chnc2.config(bg='black')
    chnc2.geometry('400x400+300+100')
    chnc2.title('ADMIN SETTINGS')
    chnc2.resizable(0, 0)
    tl1 = tkinter.Label(chnc2, text='FOR ADMINS ONLY\n\n\n ENTER NEW NAME OF CANDIDATE 2', fg='#ccffff', bg='black',font={'Arial', 16})
    tl1.pack(pady=20, padx=20)
    nc2n = tkinter.Entry(chnc2)
    nc2n.pack(pady=2)

    def update_c2_name():
        global can_bnm
        n= nc2n.get()
        can_bnm = n
        tl1 = tkinter.Label(chnc2, text='NAME UPDATED', fg='#ccffff', bg='black',font={'Arial', 16})
        tl1.pack(pady=15, padx=20)

    but = tkinter.Button(chnc2, text='Change', bg='black', fg='yellow', command=update_c2_name)
    but.pack(pady=15)


def c_elname():#change election name3
    chne = tkinter.Toplevel()
    #chne.iconbitmap('cpy.ico')
    chne.config(bg='black')
    chne.geometry('400x400+300+100')
    chne.title('ADMIN SETTINGS')
    chne.resizable(0, 0)
    tl1 = tkinter.Label(chne, text='FOR ADMINS ONLY\n\n\n ENTER NEW NAME OF ELECTION', fg='#ccffff', bg='black',font={'Arial', 16})
    tl1.pack(pady=20, padx=20)
    nen = tkinter.Entry(chne)
    nen.pack(pady=2)
    def update_ele_name():
        global elec_name
        n=nen.get()
        elec_name=n
        tl1 = tkinter.Label(chne, text='NAME UPDATED', fg='#ccffff', bg='black',font={'Arial', 15})
        tl1.pack(pady=15, padx=20)
    but = tkinter.Button(chne, text='Change', bg='black', fg='yellow', command=update_ele_name)
    but.pack(pady=15)
def admin_addedwindow():##########################________ok button in add admin________
    admadd1 = tkinter.Toplevel()
    #admadd1.iconbitmap('cpy.ico')
    admadd1.config(bg='black')
    admadd1.geometry('150x200+300+200')
    admadd1.title('ADMIN SETTINGS')
    admadd1.resizable(0, 0)
    tl1 = tkinter.Label(admadd1, text='NEW ADMIN \nADDED \n', fg='#ccffff', bg='black',font={'Arial', 16})
    tl1.pack(pady=15, padx=20)
    def okbutton():
        admadd1.destroy()

    but = tkinter.Button(admadd1, text='OK', bg='black', fg='yellow', command=okbutton)
    but.pack(pady=15)



def addadmin():#######################____________new admin__________________________
    admadd = tkinter.Toplevel()
    #admadd.iconbitmap('cpy.ico')
    admadd.config(bg='black')
    admadd.geometry('400x400+300+100')
    admadd.title('ADMIN SETTINGS')
    admadd.resizable(0,0)
    tl1 = tkinter.Label(admadd, text='FOR ADMINS ONLY\n ADDITION OF NEW ADMIN\n\nENTER ADMIN ID', fg='#ccffff', bg='black',font={'Arial', 22})
    tl1.pack(pady=20, padx=20)
    adi = tkinter.Entry(admadd)
    adi.pack(pady=5)
    tl2 = tkinter.Label(admadd, text='ENTER ADMIN KEY', fg='#ccffff', bg='black')
    tl2.pack(pady=20, padx=20)
    adk = tkinter.Entry(admadd)
    adk.pack(pady=5)
    def addnewadm():

        global  adm_list
        adl=eval(adm_list)
        adid=adi.get()
        adkey=adk.get()
        c=sorted(adl)
        if(c.count(adid)==0):
            adl[adid]=adkey
            admin_addedwindow()
            adm_list= str(adl)
            admadd.destroy()

        else:
            tl1 = tkinter.Label(admadd, text='ID ALREADY EXISTS', fg='#ccffff', bg='black',font={'Arial', 22})
            tl1.pack(pady=20, padx=20)

    but = tkinter.Button(admadd, text='Change', bg='black', fg='yellow', command=addnewadm)
    but.pack(pady=23)
def settingsadmin():###############################_________admin________settings main menu___________
    admset = tkinter.Toplevel()
    #admset.iconbitmap('cpy.ico')
    admset.config(bg='black')
    admset.geometry('400x400+275+100')
    admset.title('ADMIN SETTINGS')
    admset.resizable(0, 0)
    tl1 = tkinter.Label(admset, text='FOR ADMINS ONLY', fg='#ccffff', bg='black',font={'Arial', 16})
    tl1.pack(pady=20, padx=20)
    but = tkinter.Button(admset, text='Change Candidate 1 Name', bg='black', fg='yellow', command=changecad1)
    but.pack(pady=23)
    but = tkinter.Button(admset, text='Change Candidate 2 Name', bg='black', fg='yellow', command=changecad2)
    but.pack(pady=23)
    but = tkinter.Button(admset, text='Change Election Name', bg='black', fg='yellow', command=c_elname)
    but.pack(pady=23)
    but = tkinter.Button(admset, text='ADD NEW ADMIN', bg='black', fg='yellow', command=addadmin)
    but.pack(pady=23)

def admm():##################################__________admin main menu
    admain = tkinter.Toplevel()
    #admain.iconbitmap('cpy.ico')
    admain.config(bg='black')
    admain.geometry('400x400+250+100')
    admain.title('ADMIN MENU')
    admain.resizable(0, 0)
    tl1 = tkinter.Label(admain, text='FOR ADMINS ONLY', fg='#ccffff', bg='black',font={'Arial', 16})
    tl1.pack(pady=20, padx=20)
    but = tkinter.Button(admain, text='RESULTS', bg='black', fg='yellow', command=tellres)
    but.pack(pady=15)
    but1= tkinter.Button(admain, text='SETTINGS', bg='black', fg='yellow', command=settingsadmin)
    but1.pack(pady=15)



def adresche():
    adlog=tkinter.Toplevel()
    #adlog.iconbitmap('cpy.ico')
    adlog.config(bg='black')
    adlog.geometry('400x400+250+100')
    adlog.title('ADMIN LOGIN')
    adlog.resizable(0, 0)
    tl1= tkinter.Label(adlog,text='FOR ADMINS ONLY\nADMIN LOGIN\n\nENTER ADMIN ID', fg='#ccffff', bg='black',font={'Arial', 16})
    tl1.pack(pady=20,padx=20)
    adnu= tkinter.Entry(adlog)
    adnu.pack(pady=2)
    tl2=tkinter.Label(adlog,text='ENTER ADMIN KEY', fg='#ccffff', bg='black',font={'Arial', 16})
    tl2.pack(pady=25,padx=15)
    adki=tkinter.Entry(adlog)
    adki.pack(pady=2)
    def chkloga():
        global  adm_list
        adl=eval(adm_list)
        a_id=adnu.get()
        a_key=adki.get()
        c=sorted(adl)
        #print(c,a_id,a_key)
        if(c.count(a_id)>0 and a_key==adl[a_id]):###############this is a trail version in final versit
          admm()
          adlog.destroy()
        else:
            l8 = tkinter.Label(adlog, text='INVALID CREDENTIALS', fg='#ccffff', bg='black',font={'Arial', 14})
            l8.pack(pady=5,padx=5)
    but=tkinter.Button(adlog,text='CHECK',bg='black',fg='yellow',command=chkloga)
    but.pack(pady=23)
###################################################
#a="made by aaarc_adithya"
rt=tkinter.Tk()
#print(a)
#rt.iconbitmap('cpy.ico')
rt.title("ELECTION SOFTWARE")
rt.geometry('800x500+250+100')
rt.resizable(0,0)
rt.config(bg='black')
####################################################frames
top_bar=tkinter.Frame(rt,bg='black')
mid_sec=tkinter.Frame(rt,bg='black')
mid_sec2=tkinter.Frame(rt,bg='black')
mid_sec3=tkinter.Frame(rt,bg='#e6b800')
end_section=tkinter.Frame(rt,bg='black')
####################################################Top_bar_components
b1=tkinter.Button(top_bar,text='|||',bg='black',fg='#e6b800',relief=FLAT,command=adresche)
b1.grid(row=0,column=0,sticky='w',ipadx=5,padx=1)
sp1=tkinter.Label(top_bar,text='',bg='#e6b800',fg='#e6b800')
sp1.grid(row=0,column=1)
title1=tkinter.Label(top_bar,text=elec_name,bg='black',fg='#ccffff',font={'Arial',22})
title1.grid(row=0,column=2,padx=225,pady=5)

######################################################mid_section components

lab1m=tkinter.Label(mid_sec,text="\n\n\n\nMAKE YOUR VOICE COUNT,\n\nVOTE TODAY\n\n",bg='black',fg='#ccffff',font='Arial')
lab1m.pack()

b1m=tkinter.Button(mid_sec,text='LOGIN',bg='black',fg='#e6b800',relief=FLAT,command=votinglogin,font={'Arial',32})
b1m.pack(pady=25)
######################################################placing frames
top_bar.pack(anchor='w',padx=10,pady=5)

mid_sec.pack(pady=15)

###########################################################main_loop
rt.mainloop()
