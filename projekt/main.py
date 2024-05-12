from tkinter import messagebox
from tkinter import *
import tkinter as tk
from tkinter import ttk
import psycopg2
from datetime import date
import time
import numpy as np
from PIL import Image, ImageTk

today = date.today()
t = time.localtime()
cur_ura = time.strftime("%H.%M", t)
d1 = today.strftime("%d.%m.%Y")

izbira = 0


conn = psycopg2.connect(host = "localhost",dbname = "postgres", user = "postgres", password= "admin", port = 5432)
izbira1 = 0
izbira2 = 0
cur = conn.cursor()
cur.execute("""SELECT * FROM produkti;""")
#print(cur.fetchall())
jeodprt1 = False
jeodprt2 = False
jeodprt3 = False
class Aplikacija(tk.Frame):

    def __init__(self, master=None):
        global a
        super().__init__(master)
        self.master = master

        self.grid()
        self.kreiraj()

        self.zapri = tk.Button( text="Zapri",bg = 'red', command=root.destroy,padx = 50 ,pady = 20).grid (row=4,column = 3)



        img= Image.open("slikaa.png")
        rszimg = img.resize((100,60),Image.ANTIALIAS)
        conimg = ImageTk.PhotoImage(rszimg)

        self.image_label = tk.Label(image=conimg)
        self.image_label.image = conimg
        self.image_label.grid(row=1,column = 3)


    def klikgumba(self):
      print("a")
    def jeodprt1(self,win):
        global jeodprt1
        jeodprt1 = False
        win.destroy()

    def jeodprt2(self, win):
        global jeodprt2
        jeodprt2 = False
        win.destroy()

    def jeodprt3(self, win):
        global jeodprt3
        jeodprt3 = False
        win.destroy()


    def klik(self,event):
        print("a")














    def skladiscnik(self):
        main_window = Tk()
        main_window.winfo_toplevel().title("Skladiščnik")
        self.sprejemanje_dobave = tk.Button(main_window,text="SPREJEMANJE DOBAVE",bg = 'rosybrown', command=self.sprejemanje_dobave, padx=50,pady=20).grid(row=1, column=1)
        Label(main_window, text = "   \n   ").grid(row=2,column = 1)
        self.sprejemanje_odpreme = tk.Button(main_window,text="SPREJEMANJE ODPREME", bg= 'dark sea green',command=self.sprejemanje_odpreme, padx=50,pady=20).grid(row=3, column=1)
        tk.Button(main_window,text="Zapri", command=main_window.destroy,bg = 'red', padx=50, pady=20).grid(row=10, column=10)



    def sprejemanje_dobave(self):
        tree = ttk.Treeview()
        global jeodprt3, d1, cur_ura
        if jeodprt3:
            messagebox.showinfo("opozorilo", "je ze odprt")
        if not jeodprt3:
            jeodprt3 = True
            main_window = Tk()
            tk.Button(main_window, text="Zapri", command=main_window.destroy,bg = 'red', padx=50, pady=20).grid(row=10, column=10)

            contactinfo = []

            dobavitelj = Label(main_window, text="kdo dobavlja : ")
            produkt = Label(main_window, text="kaj dobavlja : ")
            kolicina = Label(main_window, text="količina : ")
            datum = Label(main_window, text="datum : ")
            uraa = Label(main_window, text="ura : ")

            dobavitelj.grid(sticky=E, row=1, column=1)
            produkt.grid(sticky=E, row=2, column=1)
            kolicina.grid(sticky=E, row=3, column=1)
            datum.grid(sticky=E, row=4, column=1)
            uraa.grid(sticky=E, row=5, column=1)

            kdo = Entry(main_window)
            kaj = Entry(main_window)
            koliko = Entry(main_window)
            kdaj = Entry(main_window)
            ura = Entry(main_window)

            Label(main_window, text="PODATKI O DOBAVI : ").grid(row=0, column=1)
            kdo.grid(row=1, column=2)
            kaj.grid(row=2, column=2)
            koliko.grid(row=3, column=2)
            kdaj.grid(row=4, column=2)
            ura.grid(row=5, column=2)

            Label(main_window, text="   ").grid(row=1, column=3)

            today = date.today()

            # dd/mm/YY
            d1 = today.strftime("%d.%m.%Y")

            Label(main_window, text="datum : " + d1).grid(sticky=W, row=4, column=4)

            t = time.localtime()
            cur_ura = time.strftime("%H.%M", t)
            Label(main_window, text="ura : " + cur_ura).grid(sticky=W, row=5, column=4)

            tekst = ""

            def generate_table(contact_information, window):
                global tree
                # define columns

                columns = ('kdo', 'kaj', 'koliko', 'kdaj', 'ura')
                tree = ttk.Treeview(window, columns=columns, show='headings')

                # define headings

                tree.heading('kdo', text='dostavljalec')
                tree.heading('kaj', text='produkt')
                tree.heading('koliko', text='količina')
                tree.heading('kdaj', text='datum')
                tree.heading('ura', text='ura')


                # add data to the treeview
                cur.execute("""SELECT ime_podjetja, ime_produkta, kolicina, datum, ura FROM dobava WHERE prislo = 'ne' ;""")
                for contact in cur.fetchall():
                    # print(contact)
                    tree.insert('', tk.END, values=contact)
                tree.bind('<<TreeviewSelect>>', item_selected)

                tree.grid(row=0, column=0, sticky='nsew')

            def item_selected(event):
                global tree, table_window, cur_ura, d1, izbira, tekst
                for selected_item in tree.selection():
                    item = tree.item(selected_item)
                    # record = item['values']
                    # show a message
                record = item['values']
                kdo.delete(0, END)
                kdo.insert(0, record[0])
                kaj.delete(0, END)
                kaj.insert(0, record[1])
                koliko.delete(0, END)
                koliko.insert(0, record[2])
                kdaj.delete(0, END)
                kdaj.insert(0, d1)
                ura.delete(0, END)
                ura.insert(0, cur_ura)

                table_window.destroy()






            def open_table(name, phone_number, contact_information):

                global table_window
                do = True
                for i in contactinfo:
                    if i[0] == name:
                        do = False
                if do:
                    # contactinfo.append([name, phone_number, address_field])
                    table_window = Toplevel()
                    generate_table(contactinfo, table_window)
                else:
                    messagebox.showinfo("showinfo", "ze obstaja")

            def potrdi_dobavo():
                global tree, table_window, cur_ura, d1, izbira, tekst
                kajj = "'" + kaj.get() + "'"
                kdoo = "'" + kdo.get() + "'"

                cur.execute("""SELECT ime_podjetja FROM dob_podjetja;""")
                pod = []
                for row in cur.fetchall():
                    pod.append(row[0])

                cur.execute("""SELECT ime_produkta FROM produkti;""")
                prod = []
                for row in cur.fetchall():
                    prod.append(row[0])
                besedilo = f'SELECT * FROM dobava WHERE ime_podjetja = {kdoo} AND ime_produkta = {kajj}'
                cur.execute(besedilo)
                prihodid = cur.fetchone()

                if prihodid == None:
                    messagebox.showinfo("OPOZORILO", "ta dobava ne obstaja")
                else:
                    da = 'da'
                    da = "'"+da + "'"
                    cur.execute(f'UPDATE dobava SET prislo = {da} WHERE ime_podjetja = {kdoo} AND ime_produkta = {kajj}')

                    kdo.delete(0, END)
                    kaj.delete(0, END)
                    koliko.delete(0, END)
                    kdaj.delete(0, END)
                    ura.delete(0, END)

            Label(main_window, text=" ").grid(row=7, column=1)

            Button(main_window, text="POTRDI",bg = 'medium sea green', command=lambda: potrdi_dobavo(), padx=10, pady=10).grid(row=8,
                                                                                                              column=2)

            Button(main_window, text="izberi dobavo",bg = 'wheat4', command=lambda: odpri_tabelo(),
                   padx=10, pady=10).grid(row=1, column=4, rowspan=2)



            main_window.geometry('650x400')
            main_window.mainloop()

    def sprejemanje_odpreme(self):
        tree = ttk.Treeview()
        global jeodprt3, d1, cur_ura
        jeodprt = False
        if jeodprt3:
            messagebox.showinfo("opozorilo", "je ze odprt")
        if not jeodprt3:

            main_window = Tk()
            tk.Button(main_window, text="Zapri",bg = 'red', command=main_window.destroy, padx=50, pady=20).grid(row=10, column=10)

            contactinfo = []

            labkdo = Label(main_window, text="kdo dobavlja : ")
            labkaj = Label(main_window, text="kaj dobavlja : ")
            labkoliko = Label(main_window, text="kolicina : ")
            labkdaj = Label(main_window, text="datum : ")
            labura = Label(main_window, text="ura : ")
            labopo = Label(main_window, text="opombe : ")

            kdo = Entry(main_window)
            kaj = Entry(main_window)
            koliko = Entry(main_window)
            kdaj = Entry(main_window)
            ura = Entry(main_window)
            opombe = Entry(main_window)

            Label(main_window, text="PODATKI O PRIHODU : ").grid(row=0, column=1)
            kdo.grid(row=1, column=2)
            kaj.grid(row=2, column=2)
            koliko.grid(row=3, column=2)
            kdaj.grid(row=4, column=2)
            ura.grid(row=5, column=2)
            opombe.grid(row=6, column=2)

            labkdo.grid(sticky=E, row=1, column=1)
            labkaj.grid(sticky=E, row=2, column=1)
            labkoliko.grid(sticky=E, row=3, column=1)
            labkdaj.grid(sticky=E, row=4, column=1)
            labura.grid(sticky=E, row=5, column=1)
            labopo.grid(sticky=E, row=6, column=1)

            Label(main_window, text="   ").grid(row=1, column=3)

            today = date.today()

            # dd/mm/YY
            d1 = today.strftime("%d.%m.%Y")

            Label(main_window, text="datum : " + d1).grid(sticky=W, row=4, column=4)

            t = time.localtime()
            cur_ura = time.strftime("%H.%M", t)
            Label(main_window, text="ura : " + cur_ura).grid(sticky=W, row=5, column=4)

            tekst = ""

            def generate_table(contact_information, window):
                global tree
                # define columns

                columns = ('kdo', 'kaj', 'koliko', 'kdaj', 'ura')
                tree = ttk.Treeview(window, columns=columns, show='headings')

                # define headings

                tree.heading('kdo', text='dostavljalec')
                tree.heading('kaj', text='produkt')
                tree.heading('koliko', text='kolicina')
                tree.heading('kdaj', text='datum')
                tree.heading('ura', text='ura')

                # add data to the treeview
                cur.execute("""SELECT ime_podjetja, ime_produkta, kolicina, datum,ura FROM narocila;""")
                for contact in cur.fetchall():
                    # print(contact)
                    tree.insert('', tk.END, values=contact)
                tree.bind('<<TreeviewSelect>>', item_selected)

                tree.grid(row=0, column=0, sticky='nsew')

            def item_selected(event):
                global tree, table_window, cur_ura, d1, izbira, tekst
                for selected_item in tree.selection():
                    item = tree.item(selected_item)
                    # record = item['values']
                    # show a message
                record = item['values']
                kdo.delete(0, END)
                kdo.insert(0, record[1])
                kaj.delete(0, END)
                kaj.insert(0, record[2])
                koliko.delete(0, END)
                koliko.insert(0, record[3])
                kdaj.delete(0, END)
                kdaj.insert(0, d1)
                ura.delete(0, END)
                ura.insert(0, cur_ura)

                table_window.destroy()

                izbira = IntVar()
                izbira = Checkbutton(main_window, text="vkljuci v opombe", variable=izbira, onvalue=1, offvalue=0)
                izbira.grid(row=7, column=4)

                if raz_datum(record[4], d1) == 0:
                    # print(raz_datum(kdaj.get(), d1))

                    opozorilot = (raz_ure(ura.get(), cur_ura))
                    Label(main_window, text=opozorilot).grid(sticky=W, row=6, column=4)
                elif raz_datum(record[4], d1) > 0:
                    opozorilot = ("Narocilo zamuja " + str((raz_datum(record[4], d1))) + "dni. ")
                    Label(main_window, text=opozorilot).grid(sticky=W, row=6, column=4)
                else:
                    opozorilot = ("Narocilo prehiteva " + str(-(raz_datum(record[4], d1))) + " dni. ")
                    Label(main_window, text=opozorilot).grid(sticky=W, row=6, column=4)

                tekst = opozorilot

            def open_table(name, phone_number, contact_information):

                global table_window
                do = True
                for i in contactinfo:
                    if i[0] == name:
                        do = False
                if do:
                    # contactinfo.append([name, phone_number, address_field])
                    table_window = Toplevel()
                    generate_table(contactinfo, table_window)
                else:
                    messagebox.showinfo("showinfo", "ze obstaja")

            def raz_ure(u1, u2):
                a1 = u1.split(".")
                a2 = u2.split(".")
                raz = (int(a1[0]) - int(a2[0])) * 60
                raz += int(a1[1]) - int(a2[1])
                dog = ""
                if raz < 10 and raz > -10:
                    return "brez zamude."
                if raz > 0:
                    dog = "prehiteva"
                elif raz < 0:
                    dog = "zamuja"
                    raz = -raz

                if raz >= 60 or raz <= -60:
                    return dog + " " + str(int(raz / 60)) + " h in  " + str(raz % 60) + " min. "

                return dog + " " + str(raz % 60) + " min. "

            def raz_datum(u1, u2):
                dnevi_v_mescih = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                a1 = u1.split(".")
                a2 = u2.split(".")
                b1 = [int(i) for i in a1]
                b2 = [int(i) for i in a2]
                c1 = b1[0] + sum(dnevi_v_mescih[:b1[1] - 1]) + b1[2] * 356
                c2 = b2[0] + sum(dnevi_v_mescih[:b2[1] - 1]) + b2[2] * 356

                raz = c2 - c1
                return raz

            def potrdi_prihod():
                global tree, table_window, cur_ura, d1, izbira, tekst

                # record = item['values']
                # show a message

                # record = [kdo.get(),kaj.get(),koliko.get(),kdaj.get(),ura.get()]
                kajj = "'" + kaj.get() + "'"
                kdoo = "'" + kdo.get() + "'"
                kolikoo = koliko.get()
                kdajj = kdaj.get()
                uraa = ura.get()
                dat = '28.02.2024'
                ur = '18.00'
                cur.execute(f'SELECT * FROM narocila WHERE ime_podjetja = {kdoo} AND ime_produkta = {kajj} AND kolicina = {kolikoo} AND datum = {dat} AND ura = {ur}')
                out = cur.fetchone()

                dat = out[4]
                ur = out[5]

                opozorilot = ""
                if raz_datum(dat, d1) == 0:
                    # print(raz_datum(kdaj.get(), d1))

                    opozorilot = (raz_ure(ur, cur_ura))
                    Label(main_window, text=opozorilot).grid(sticky=W, row=6, column=4)
                elif raz_datum(dat, d1) > 0:
                    opozorilot = ("Narocilo zamuja " + str((raz_datum(dat, d1))) + "dni. ")
                    Label(main_window, text=opozorilot).grid(sticky=W, row=6, column=4)
                else:
                    opozorilot = ("Narocilo prehiteva " + str(-(raz_datum(dat, d1))) + " dni. ")
                    Label(main_window, text=opozorilot).grid(sticky=W, row=6, column=4)

                # opozorilot = opozorilot + + "Moralo bi priti "+record[4]

                cur.execute("""SELECT ime_podjetja FROM nar_podjetja;""")
                pod = []
                for row in cur.fetchall():
                    pod.append(row[0])

                cur.execute("""SELECT ime_produkta FROM produkti;""")
                prod = []
                for row in cur.fetchall():
                    prod.append(row[0])
                besedilo = f'SELECT * FROM narocila WHERE ime_podjetja = {kdoo} AND ime_produkta = {kajj}'
                cur.execute(besedilo)
                narociloid = cur.fetchone()
                print(narociloid)
                if narociloid == None:
                    messagebox.showinfo("OPOZORILO", "ta prevzem ne obstaja")


                else:
                    kdajj = "'" + kdaj.get() + "'"
                    uraa = "'" + ura.get() + "'"
                    if izbira:
                        tekst = opozorilot + " " + opombe.get()
                    cur.execute("""SELECT MAX(id) FROM prisli_prihodi;""")
                    a = cur.fetchone()
                    stevilka = int(a[0]) + 1
                    tekst = opombe.get()
                    if tekst == "":
                        tekst = "ni opomb"
                    tekst = "'" + tekst + "'"
                    da = 'da'
                    da = "'" + da + "'"
                    besedilo = f'UPDATE narocila SET prislo = {da} WHERE narociloID = {narociloid[0]}'
                    cur.execute(besedilo)

                    #besedilo = f'DELETE FROM prihodi WHERE id = {narociloid[0]} '
                    #cur.execute(besedilo)

                    kdo.delete(0, END)
                    kaj.delete(0, END)
                    koliko.delete(0, END)
                    kdaj.delete(0, END)
                    ura.delete(0, END)

            Label(main_window, text=" ").grid(row=7, column=1)

            Button(main_window, text="potrdi prihod", command=lambda: potrdi_prihod(), padx=10, pady=10).grid(row=8,
                                                                                                              column=2)

            Button(main_window, text="izberi prihod", command=lambda: open_table(kdo.get(), kaj.get(), contactinfo),
                   padx=10, pady=10).grid(row=1, column=4, rowspan=2)

            tk.Button(main_window, text="Quit", command=lambda: [self.jeodprt3(main_window)], padx=50,
                      pady=20).grid(row=12, column=12)

            main_window.geometry('550x300')
            main_window.mainloop()




    def logistika(self):
        main_window = Tk()
        main_window.winfo_toplevel().title("logistik")
        self.dodajanjedob = tk.Button(main_window,text="DODAJ PODJETJE ZA ODPREMO", command=self.dodajdob,bg = 'SpringGreen2', padx=33, pady=20).grid(row=8, column=1)
        self.dodajanjedob = tk.Button(main_window,text="DODAJ NOVO ODPREMO", command=self.dodajnarocilo,bg = 'SpringGreen2', padx=50, pady=20).grid(row=7, column=1)
        self.dodajanjedob = tk.Button(main_window,text="PREGLED PRODUKTOV", command=self.pregledprod,bg = 'gold', padx=50, pady=20).grid(row=2, column=1)
        self.dodajanjedob = tk.Button(main_window,text="DODAJ NOV PRODUKT", command=self.dodajprodukt, padx=50,bg = 'gold', pady=20).grid(row=1, column=1)
        self.dodajanjedob = tk.Button(main_window,text="DODAJ NOVO DOBAVO", command=self.dodajprevzem,bg = 'cornflower blue', padx=50, pady=20).grid(row=4, column=1)
        self.dodajanjedob = tk.Button(main_window, text="DODAJ PODJETJE ZA DOBAVO", command=self.dodajprevzem,bg='cornflower blue', padx=33, pady=20).grid(row=5, column=1)
        self.lab1 = tk.Label(main_window, text=" ",    ).grid(row=3, column=1)
        self.lab2 = tk.Label(main_window, text=" ",    ).grid(row=6, column=1)


        tk.Button(main_window,text="Zapri",bg = 'red', command=main_window.destroy, padx=50, pady=20).grid(row=10, column=10)





    def dodajdob(self):
        main_window = Tk(screenName="dodaj dobavitelja")
        main_window.winfo_toplevel().title("dodaj dobavitelja")
        tk.Button(main_window, text="Zapri",bg = 'red', command=main_window.destroy, padx=50, pady=20).grid(row=10, column=10)

        labime = Label(main_window, text="naziv podjetja : ")
        labkon = Label(main_window, text="telefonska številka : ")
        labnas = Label(main_window, text="naslov podjetja : ")
        ime = Entry(main_window)
        nas = Entry(main_window)
        kon = Entry(main_window)
        labime.grid(row=1, column=0)
        labnas.grid(row=2, column=0)
        labkon.grid(row=3, column=0)

        ime.grid(row=1, column=1)
        nas.grid(row=2, column=1)
        kon.grid(row=3, column=1)

        def dodaj_dobavitelja():
            cur.execute("""SELECT ime FROM dobavitelji;""")
            dobavitelji = []
            for row in cur.fetchall():
                dobavitelji.append(row[0])
            dobavitelj = ime.get()
            print(dobavitelj)
            print(dobavitelji)
            if dobavitelj in dobavitelji:
                messagebox.showinfo("NAPAKA", "ta dobavitelj s tem imenom ze obstaja")
            else:
                dobavitelj = "'" + dobavitelj + "'"
                kontakt = "'" + kon.get() + "'"
                naslov = "'" + nas.get() + "'"
                tekst = f'INSERT INTO dobavitelji (ime,kontakt,naslov) VALUES ({dobavitelj},{kontakt},{naslov})'
                # INSERT INTO dobavitelji (ime,kontakt,naslov) VALUES ('NIKE','nike@gmail.com','Slovenska cesta 35')
                cur.execute(tekst)

        tk.Button(main_window, text="dodaj dobavitelja",bg = 'hot pink', command=lambda: [dodaj_dobavitelja()]).grid(row=4, column=1)


        main_window.mainloop()


    def dodajnarocilo(self):
        main_window = Tk(screenName="dodaj dobavitelja")
        main_window.winfo_toplevel().title("dodajanje naročil")
        tk.Button(main_window, text="Zapri",bg = 'red', command=main_window.destroy, padx=50, pady=20).grid(row=10, column=10)

        contactinfo = []

        labkdo = Label(main_window, text="kdo dobavlja : ")
        labkaj = Label(main_window, text="kaj dobavlja : ")
        labkoliko = Label(main_window, text="količina : ")
        labkdaj = Label(main_window, text="kdaj dobavlja (datum) : ")
        labura = Label(main_window, text="predvidena ura : ")

        kdo = Entry(main_window)
        kaj = Entry(main_window)
        koliko = Entry(main_window)
        kdaj = Entry(main_window)
        ura = Entry(main_window)

        kdo.grid(row=1, column=4)
        kaj.grid(row=2, column=4)
        koliko.grid(row=3, column=4)
        kdaj.grid(row=4, column=4)
        ura.grid(row=5, column=4)

        labkdo.grid(row=1, column=3)
        labkaj.grid(row=2, column=3)
        labkoliko.grid(row=3, column=3)
        labkdaj.grid(row=4, column=3)
        labura.grid(row=5, column=3)

        def generate_table(contact_information, window):
            global tree
            # define columns

            columns = ('produkt', 'kolicina', 'enote')
            tree = ttk.Treeview(window, columns=columns, show='headings')

            # define headings
            tree.heading('produkt', text='produkt')
            tree.heading('kolicina', text='kolicina')
            tree.heading('enote', text='enote')

            # add data to the treeview
            cur.execute("""SELECT * FROM produkti;""")
            for contact in cur.fetchall():
                # print(contact)
                tree.insert('', tk.END, values=contact)
            tree.bind('<<TreeviewSelect>>', item_selected)

            tree.grid(row=0, column=0, sticky='nsew')

        def item_selected(event):
            global tree, table_window
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                # record = item['values']
                # show a message
                record = item['values']
                kaj.delete(0, END)
                kaj.insert(0, record[0])
                table_window.destroy()
                opozorilo = Label(main_window,
                                  text=f'enote: {record[2]}')
                opozorilo.grid(row=3, column=5)

        def open_table():
            global table_window
            do = True
            for i in contactinfo:
                if i[0] == name:
                    do = False
            if do:
                # contactinfo.append([name, phone_number, address_field])
                table_window = Toplevel()
                generate_table(contactinfo, table_window)
            else:
                messagebox.showinfo("showinfo", "ze obstaja")

                # ustvari novo okno za tabelo
        def odpri_tabelo():
            global table_window
            table_window = Toplevel()
            tabela(table_window)
        #ustvari drevesno strukturo in tabelo s podatki
        def tabela(okno):
            global tree
            #določanje naslovov stolpcev
            stolpci = ('ime dobavitelja', 'telefonska številka', 'uradni naslov')
            tree = ttk.Treeview(okno, columns=stolpci, show='headings')
            #kreiranje stolpcev
            tree.heading('ime dobavitelja', text='ime dobavitelja')
            tree.heading('telefonska številka', text='telefonska številka')
            tree.heading('uradni naslov', text='uradni naslov')
            #zajemanje podatkov
            cur.execute("""SELECT * FROM dob_podjetja;""")
            for podatki in cur.fetchall():
                #vstavljanje podatkov v drevo
                tree.insert('', tk.END, values=podatki)
            #prikaz tabele v oknu
            tree.bind('<<TreeviewSelect>>', izbran_podatek)
            tree.grid(row=0, column=0, sticky='nsew')

        #se kliče ko kliknemo na podatek v tabeli
        def izbran_podatek():
            global tree, table_window
            for izbranpodatek in tree.selection():
                element = tree.item(izbranpodatek)
                lista = element['values']
                kdo.delete(0, END)
                kdo.insert(0, lista[0])

                table_window.destroy() #zapre tabelo



        def dodaj_narocilo(kd, ka, ko, kda, ur):
            kdo = "'" + kd + "'"
            kaj = "'" + ka + "'"
            koliko = "'" + ko + "'"
            kdaj = "'" + kda + "'"
            ura = "'" + ur + "'"
            cur.execute("""SELECT MAX(id) FROM dobava;""")
            a = cur.fetchone()
            id = a[0] + 1

            cur.execute("""SELECT ime_podjetja FROM dob_podjetja;""")
            dobav = []
            for row in cur.fetchall():
                dobav.append(row[0])

            cur.execute("""SELECT ime_produkta FROM produkti;""")
            prod = []
            for row in cur.fetchall():
                prod.append(row[0])

            if kd not in dobav:
                messagebox.showinfo("NAPAKA",
                                    "dobavitelj ne obstaja, prosim preveri zapis ali dodaj novega dobavitelja.")
            elif ka not in prod:
                messagebox.showinfo("NAPAKA", "produkt ne obstaja, prosim preveri pri zapisu ali dodaj nov produkt.")
            else:
                text = f'INSERT INTO dobava (id,kdo,kaj,koliko,kdaj,ura) VALUES ({id},{kdo},{kaj},{koliko},{kdaj},{ura})'
                cur.execute(text)


        tk.Button(main_window, text="dodaj predivdeno narocilo",command=lambda: dodaj_narocilo(kdo.get(), kaj.get(), koliko.get(), kdaj.get(),ura.get())).grid(row=6, column=4)

        tk.Button(main_window, text="izberi dobavitelja",command=lambda: odpri_tabelo()).grid(row=1, column=5)

        tk.Button(main_window, text="izberi produkt", command=lambda: open_table()).grid(row=2, column=5)
        main_window.mainloop()

    def pregledprod(self):
        main_window = Tk(screenName="dodaj dobavitelja")
        main_window.winfo_toplevel().title("Pregled produktov")
        tk.Button(main_window, text="Zapri",bg = 'red', command=main_window.destroy, padx=20, pady=10).grid(row=10, column=10)

        Label(main_window, text="produkt:").grid(row=2, column=0)
        produktima = Entry(main_window)
        produktima.grid(row=2, column=1)



        def generiraj_tabelo(window):
            global tree
            # define columns

            columns = ('produkt', 'kolicina', 'enote')
            tree = ttk.Treeview(window, columns=columns, show='headings')

            # define headings
            tree.heading('produkt', text='produkt')
            tree.heading('kolicina', text='količina')
            tree.heading('enote', text='enote')

            # add data to the treeview
            cur.execute("""SELECT * FROM produkti;""")
            for vrstica in cur.fetchall():
                # print(contact)
                tree.insert('', tk.END, values=vrstica)


            tree.grid(row=0, column=0, sticky='nsew')


        def odpritabelo():
            global table_window
            do = True

            if do:
                # contactinfo.append([name, phone_number, address_field])
                table_window = Toplevel()
                generiraj_tabelo( table_window)
            else:
                messagebox.showinfo("showinfo", "ze obstaja")

        def generiraj_tabelo1(window):
            global tree, izbira1, izbira2
            # define columns

            columns = ('kdo', 'kaj', 'koliko', 'kdaj', 'ura', 'prisel')
            tree = ttk.Treeview(window, columns=columns, show='headings')

            # define headings

            tree.heading('kdo', text='podjetje')
            tree.heading('kaj', text='produkt')
            tree.heading('koliko', text='količina')
            tree.heading('kdaj', text='datum')
            tree.heading('ura', text='ura')
            tree.heading('prisel', text='že prišlo?')

            # add data to the treeview
            b = []
            prod = "'" + produktima.get() + "'"
            cur.execute(f'SELECT ime_podjetja,ime_produkta,kolicina,datum,ura,prislo FROM dobava WHERE ime_produkta = {prod};')
            a = cur.fetchall()

            for contact in a:
                # print(contact)
                tree.insert('', tk.END, values=contact)

            tree.grid(row=0, column=0, sticky='nsew')

        def odpritabelo1():
            global table_window
            do = True
            if do:
                # contactinfo.append([name, phone_number, address_field])
                table_window = Toplevel()
                generiraj_tabelo1(table_window)
            else:
                messagebox.showinfo("showinfo", "ze obstaja")

        def generiraj_tabelo2(window):
            global tree, izbira1, izbira2
            # define columns

            columns = ( 'kdo', 'kaj', 'koliko', 'kdaj', 'ura', 'prisel')
            tree = ttk.Treeview(window, columns=columns, show='headings')

            # define headings

            tree.heading('kdo', text='kdo')
            tree.heading('kaj', text='kaj')
            tree.heading('koliko', text='koliko')
            tree.heading('kdaj', text='kdaj')
            tree.heading('ura', text='ura')
            tree.heading('prisel', text='ze prisel?')

            # add data to the treeview
            b = []
            prod = "'" + produktima.get() + "'"
            cur.execute(f'SELECT ime_podjetja,ime_produkta,kolicina,datum,ura,prislo FROM odprema WHERE ime_produkta = {prod};')
            a = cur.fetchall()




            for contact in a:
                # print(contact)
                tree.insert('', tk.END, values=contact)

            tree.grid(row=0, column=0, sticky='nsew')

        def odpritabelo2():
            global table_window
            do = True
            cur.execute('''SELECT ime_produkta from produkti''')
            if produktima.get() not in cur.fetchall():
                do = False
            if do:
                # contactinfo.append([name, phone_number, address_field])
                table_window = Toplevel()
                generiraj_tabelo2( table_window)
            else:
                messagebox.showinfo("showinfo", "ta produkt ne obstaja")

        tk.Button(main_window, text="preglej produkte",bg = 'CadetBlue2', command=lambda: odpritabelo()).grid(row=0, column=1)
        tk.Button(main_window, text="dobave produkta",bg='AntiqueWhite2', command=lambda: odpritabelo1()).grid(row=2, column=3)
        tk.Label(main_window,text = ' ').grid(row=1,column = 2)
        tk.Label(main_window, text='').grid(row=1, column=0)
        tk.Button(main_window, text="odpreme produkta",bg='LightPink1', command=lambda: odpritabelo2()).grid(row=3, column=3)



        main_window.mainloop()

        #izbira2 = IntVar()
        #izbira1 = IntVar()
        # Checkbutton(main_window, text="pretekli prihodi", variable=izbira1, onvalue=1, offvalue=0).grid(row=8, column=1)

        # Checkbutton(main_window, text="prihodnji prihodi", variable=izbira2, onvalue=1, offvalue=0).grid(row=9, column=1)


    def dodajprodukt(self):
        main_window = Tk(screenName="dodaj dobavitelja")
        main_window.winfo_toplevel().title("dodajanje produktov")
        tk.Button(main_window, text="Zapri",bg = 'red', command=main_window.destroy, padx=10, pady=10).grid(row=10, column=10)

        prodime = Label(main_window, text="ime produkta : ")
        prodeno = Label(main_window, text="enote : ")

        pime = Entry(main_window)
        peno = Entry(main_window)

        prodime.grid(row=1, column=1,sticky = E)
        prodeno.grid(row=2, column=1,sticky = E)

        pime.grid(row=1, column=2)
        peno.grid(row=2, column=2)



        def dodaj_produkt(ime, enote):

            # INSERT INTO products (name,quantity,enota) VALUES ('jabolka',30,'komadov')
            imee = "'" + ime + "'"
            enotee = "'" + enote + "'"

            cur.execute("""SELECT ime_produkta FROM produkti;""")
            prod = []
            for row in cur.fetchall():
                prod.append(row[0])
            if ime in prod:
                messagebox.showinfo("NAPAKA", "produkt s tem imenom že obstaja")
            else:
                tekst = f'INSERT INTO produkti VALUES ({imee},0,{enotee})'

                cur.execute(tekst)

        tk.Button(main_window, text="dodaj produkt",bg = 'CadetBlue1', command=lambda: dodaj_produkt(pime.get(), peno.get())).grid(row=3, column=2)


        main_window.mainloop()

    def dodajprevzem(self):
        main_window = Tk(screenName="dodaj prevzem")
        main_window.winfo_toplevel().title("DODAJANJE DOBAV")
        tk.Button(main_window, text="Zapri",bg = 'red', command=main_window.destroy, padx=20, pady=10).grid(row=10, column=10)


        contactinfo = []

        labkdo = Label(main_window, text="kdo dobavlja : ")
        labkaj = Label(main_window, text="kaj dobavlja : ")
        labkoliko = Label(main_window, text="količina : ")
        labkdaj = Label(main_window, text="kdaj dobavlja (datum) : ")
        labura = Label(main_window, text="predvidena ura : ")

        kdo = Entry(main_window)
        kaj = Entry(main_window)
        koliko = Entry(main_window)
        kdaj = Entry(main_window)
        ura = Entry(main_window)

        kdo.grid(row=1, column=4)
        kaj.grid(row=2, column=4)
        koliko.grid(row=3, column=4)
        kdaj.grid(row=4, column=4)
        ura.grid(row=5, column=4)

        labkdo.grid(row=1, column=3, sticky = E)
        labkaj.grid(row=2, column=3, sticky = E)
        labkoliko.grid(row=3, column=3, sticky = E)
        labkdaj.grid(row=4, column=3, sticky = E)
        labura.grid(row=5, column=3, sticky = E)

        def tabela1(contact_information, window):
            global tree
            # define columns

            columns = ('ime dobavitelja', 'kontakni podatki', 'uradni naslov')
            tree = ttk.Treeview(window, columns=columns, show='headings')

            # define headings
            tree.heading('ime dobavitelja', text='ime dobavitelja')
            tree.heading('kontakni podatki', text='telefonska številka')
            tree.heading('uradni naslov', text='uradni naslov')

            # add data to the treeview
            cur.execute("""SELECT * FROM dob_podjetja;""")
            for contact in cur.fetchall():
                # print(contact)
                tree.insert('', tk.END, values=contact)
            tree.bind('<<TreeviewSelect>>', izbranpodatek1)

            tree.grid(row=0, column=0, sticky='nsew')

        # item_selected
        def izbranpodatek1(event):
            global tree, table_window
            for izbranpodatek in tree.selection():
                item = tree.item(izbranpodatek)
                # record = item['values']
                # show a message
                record = item['values']
                kdo.delete(0, END)
                kdo.insert(0, record[0])
                table_window.destroy()

        # open_table
        def odpri_tabelo1():
            global table_window
            do = True
            for i in contactinfo:
                if i[0] == name:
                    do = False
            if do:
                # contactinfo.append([name, phone_number, address_field])
                table_window = Toplevel()
                tabela1(contactinfo, table_window)
            else:
                messagebox.showinfo("showinfo", "ze obstaja")

        def generate_table(contact_information, window):
            global tree
            # define columns

            columns = ('produkt', 'kolicina', 'enote')
            tree = ttk.Treeview(window, columns=columns, show='headings')

            # define headings
            tree.heading('produkt', text='produkt')
            tree.heading('kolicina', text='kolicina')
            tree.heading('enote', text='enote')

            # add data to the treeview
            cur.execute("""SELECT * FROM produkti;""")
            for contact in cur.fetchall():
                # print(contact)
                tree.insert('', tk.END, values=contact)
            tree.bind('<<TreeviewSelect>>', item_selected)

            tree.grid(row=0, column=0, sticky='nsew')

        def item_selected(event):
            global tree, table_window
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                # record = item['values']
                # show a message
                record = item['values']
                kaj.delete(0, END)
                kaj.insert(0, record[0])
                table_window.destroy()
                opozorilo = Label(main_window,
                                  text=f'enote: {record[2]}')
                opozorilo.grid(row=3, column=5)

        def open_table():
            global table_window
            do = True
            for i in contactinfo:
                if i[0] == name:
                    do = False
            if do:
                # contactinfo.append([name, phone_number, address_field])
                table_window = Toplevel()
                generate_table(contactinfo, table_window)
            else:
                messagebox.showinfo("showinfo", "ze obstaja")

        tk.Button(main_window, text="dodaj dobavo",bg = 'coral',
                  command=lambda: dodaj_narocilo(kdo.get(), kaj.get(), koliko.get(), kdaj.get(), ura.get())).grid(row=6,
                                                                                                                  column=4)

        tk.Button(main_window, text="izberi dobavitelja",bg = 'peach puff',
                  command=lambda: odpri_tabelo1()).grid(row=1, column=5)

        tk.Button(main_window, text="izberi produkt",bg = 'lemon chiffon', command=lambda: open_table()).grid(row=2, column=5)

        main_window.mainloop()





    def kreiraj(self):


        self.logistik = tk.Button( text="LOGISTIK", command=self.logistika,bg = 'LightBlue1',padx = 50 ,pady = 20).grid (row=1,column = 1)

        self.skladiscnik = tk.Button(text="SKLADIŠČNIK", command=self.skladiscnik,bg  ='DarkOliveGreen1', padx=39, pady=20).grid(row=2, column=1)




root = tk.Tk()
app = Aplikacija(master=root)
app.mainloop()

conn.commit()
cur.close()
conn.close()

