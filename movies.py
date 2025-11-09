import configparser
import sqlite3
import tkinter.filedialog
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import tkinter.dialog as log
from tkinter.simpledialog import *
import os
import shutil
import datetime
try:
    import UpdateDB
except:
    pass
window = Tk()

window.geometry('355x390')
window.minsize(200, 200)
window.title('movie')
config = configparser.ConfigParser()
directory = str(os.getcwd()) + "\Movie.db"
auth = 'Database of My movies app'

Len1 = 0
Len2 = 0
version = "1.2.0"

def checkdb(dbdir):
    conn = sqlite3.connect(dbdir)
    c = conn.cursor()

    try:
        getdb = c.execute("PRAGMA table_info(Settings)").fetchall()
    except:
        return "Not Validated1"
    
    SettingsColoums = ['ProfileNumber', 'bg_color', 'fg_color', 'font', 'backup_dir', 'auth']
    Len = 0

    for data in getdb:    
        if Len == 0:
            try:
                pn = c.execute(f"SELECT ProfileNumber FROM Settings WHERE ProfileNumber = 0").fetchall()[0][0]
            except:
                conn.close()
                return "Not Validated"
            if type(pn) is int and pn == 0:
                pass
            else:
                conn.close()
                return "Not Validated"
            
        if data[1] == SettingsColoums[Len]:
            Len += 1
        else:
            conn.close()
            return "Not Validated"
        
        if Len == 5:
            backup_dir = c.execute(f"SELECT {data[1]} FROM Settings WHERE ProfileNumber = 0").fetchall()[0][0]
            if os.path.isdir(backup_dir) or backup_dir == "none":
                pass
            else:
                conn.close()
                return "Not Validated"
        
        if Len == 6:
            authcheck = c.execute("SELECT auth FROM Settings WHERE PRofileNumber = 0").fetchall()[0][0]
            if authcheck == "Database of My movies app":
                pass
            else:
                conn.close()
                return "Not Validated"
            
    getbg = c.execute('SELECT "bg_color" FROM Settings WHERE ProfileNumber = 0').fetchall()[0][0]
    getfg = c.execute('SELECT "fg_color" FROM Settings WHERE ProfileNumber = 0').fetchall()[0][0]
    getfont = c.execute('SELECT "font" FROM Settings WHERE ProfileNumber = 0').fetchall()[0][0]
    
    try:
        Label(window, text="Enter your movie's name", fg=getfg, bg=getbg, font=getfont)   
    except:
        return "Not Validated"  
    
    try:
        getdb = c.execute("PRAGMA table_info(MovieData)").fetchall()
    except:
        conn.close()
        return "Not Validated"
    
    MovieDataColoums = ["moviename", "dateadded", "session", "episode", "time", "status", "datefinished"]
    Len = 0

    MovieListTemp = c.execute("SELECT moviename FROM MovieData").fetchall()
    MovieList = []

    for a in MovieListTemp:
        for b in a:
            MovieList.append(b)

    for data in getdb:
        if data[1] == MovieDataColoums[Len]:
            Len += 1
        else:
            conn.close()
            return "Not Validated"
        
        if Len == 5:
            if MovieList == []:
                pass
            else:
                for movie in MovieList:
                    status = c.execute(f'SELECT status FROM MovieData WHERE moviename = "{movie}"').fetchall()[0][0]
                    datefinished = c.execute(f'SELECT datefinished FROM MovieData WHERE moviename = "{movie}"').fetchall()[0][0]
                    if status == "False" and datefinished == "0":
                        pass
                    elif status == "True" and datefinished != "0":
                        pass
                    else:
                        conn.close()
                        return "Not Validated"
        
        if Len == 7:
            return "Validated"

class dberror():
    def NewDB(self):
        open(directory, "x")
        conn = sqlite3.connect(directory)
        c = conn.cursor()

        c.execute("CREATE TABLE Settings(ProfileNumber PRIMARY KEY, bg_color, fg_color, font, backup_dir, auth)")
        c.execute('INSERT INTO Settings(ProfileNumber, bg_color, fg_color, font, backup_dir, auth) VALUES (0, "snow", "gray70", "Arial", "none", "Database of My movies app")')
        c.execute("CREATE TABLE MovieData(moviename PRIMARY KEY, dateadded, session, episode, time, status, datefinished)")
        conn.commit()
        try:    
            bg_color = c.execute("SELECT bg_color FROM Settings WHERE ProfileNumber = 0").fetchall()[0][0]
        except:
            ShowDbError()

        window.configure(bg=bg_color)
        auth = c.execute("SELECT auth FROM Settings WHERE ProfileNumber = 0").fetchall()[0][0]
        conn.close()
        return Setting()
    
    def recovery(self):
        try:
            os.remove(str(os.getcwd()) + "/Movie.db")
        except:
            pass
        yesno = askyesno("Question",
                         "Do you wanna recover your data?\n(only if you have a backup from database in database folder!)")
        if yesno is True:
            showinfo("Recovery",
                     f"You must select 'Movie.db' file to recovery your data\n(Hint:go to that directory")
            file = tkinter.filedialog.askopenfilename(title="Select 'Movie.db file'",
                                                      filetypes=[('DB files', '*.db')])
            global auth
            if file == '':
                window.destroy()

            elif "Movie.db" in file:
                global conn
                global c
                conn = sqlite3.connect(file)
                c = conn.cursor()
            else:
                pass

            if checkdb(file) == "Validated":
                shutil.copy(file, directory)
                shutil.copy(directory, c.execute("SELECT backup_dir FROM Settings WHERE ProfileNumber = 0").fetchall()[0][0])
                showinfo('copy', 'Datas recovered successfully')

                try:
                    bg_color = c.execute("SELECT bg_color FROM Settings WHERE ProfileNumber = 0").fetchall()[0][0]
                except:
                    ShowDbError()
                window.configure(bg=bg_color)
                auth = c.execute("SELECT auth FROM Settings WHERE ProfileNumber = 0").fetchall()[0][0]
                return Setting()
            else:
                showerror("info", 'This is not a "My movies" database file')
                yesno = askyesno("Question", "Do you wanna try again?")
                if yesno is True:
                    dberror.recovery("self")
                else:
                    window.destroy()

        else:
            showinfo("Recovery", f"This app will make another database automatically\nBut your data will be removed")
            return dberror.NewDB("self")
        

def ShowDbError():
    showerror("db validation error", "Looks like db file is modified and is invalid.\n you must create a new one or recover your db file.")
    Q = log.Dialog(None,{'title':'db invalid','text':"Choose an action",'default':0,'bitmap':log.DIALOG_ICON,'strings': ("Recover Data", "Make a new db")})

    func = dberror()
    if Q.num == 0:
        return func.recovery()
    elif Q.num == 1:
        return func.NewDB()
        
def main():
    if checkdb(directory) != "Validated":
        ShowDbError()       

    conn = sqlite3.connect(directory)
    c = conn.cursor()
    shutil.copy(directory, c.execute("SELECT backup_dir FROM Settings WHERE ProfileNumber = 0").fetchall()[0][0])
    MovieListTemp = c.execute("SELECT moviename FROM MovieData").fetchall()
    MovieList = []

    for a in MovieListTemp:
        for b in a:
            MovieList.append(b)
    global bg_color
    global fg_color
    global font

    def ChangeCurrentTheme(Theme):
        if checkdb(directory) != "Validated":
            ShowDbError()
        #{"Theme Name":("Background Color"," Foreground Color")}
        themedict = {"Halloween":("gray20", "darkorange"), "Christmas":("firebrick4", "limegreen"), "White":("snow", "gray70"), "Light Blue":("light sky blue", "RoyalBlue4"), "Dark Blue":("midnight blue", "RoyalBlue1"), "Light Green":("DarkOliveGreen1", "darkgreen"), "Dark Green":("darkgreen", "DarkOliveGreen1"), "Light Orange":("coral", "OrangeRed4"), "Dark Orange":("Orangered4", "coral"), "Red":("red4", "coral"), "Yellow":("goldenrod","lightgoldenrod"), "Black":("gray1","gray64"), "Light Purple":("MediumPurple1", "purple4"), "Dark Purple":("purple4", "MediumPurple1"), "Light Pink":("orchid1", "DeepPink4"), "Dark Pink":("maroon4", "orchid1"), "Blackpink":("gray15", "orchid1")}
        
        global bg_color
        global fg_color
        global font

        if Theme == "Halloween":
            font = "Jokerman"
        elif Theme == "Christmas":
            font = "Forte"
        else:
            try:
                font = "Arial"
            except:
                ShowDbError()

        if Theme == "Default":
            try:
                bg_color = c.execute("SELECT bg_color FROM Settings WHERE ProfileNumber = 0").fetchall()[0][0]
                fg_color = c.execute("SELECT fg_color FROM Settings WHERE ProfileNumber = 0").fetchall()[0][0]
            except:
                ShowDbError()
            window.configure(bg=bg_color)
            text1.destroy()
            b_add.destroy()
            b_list.destroy()
            exitb.destroy()
            main()
        else:
            bg_color = themedict.get(Theme)[0]
            fg_color = themedict.get(Theme)[1]
            window.configure(bg=bg_color)
            text1.destroy()
            b_add.destroy()
            b_list.destroy()
            exitb.destroy()
            main()
        
    
    def ChangeCurrentFont(Font):
        if checkdb(directory) != "Validated":
            ShowDbError()
        global font
        if Font == "Default":
            try:
                font = c.execute("SELECT font FROM Settings WHERE ProfileNumber = 0").fetchall()[0][0]
            except:
                ShowDbError()
        else:
            font = Font
        text1.destroy()
        b_add.destroy()
        b_list.destroy()
        exitb.destroy()
        main()

    def s_default_theme():
        if checkdb(directory) != "Validated":
            ShowDbError()
        text1.destroy()
        b_add.destroy()
        b_list.destroy()
        exitb.destroy()

        def next():
            if checkdb(directory) != "Validated":
                ShowDbError()
            
            conn = sqlite3.connect(directory)
            c = conn.cursor()

            #{"Theme Name":("Background Color"," Forgeround Color")}
            themedict = {"Halloween":("gray20", "darkorange"), "Christmas":("firebrick4", "limegreen"), "White":("snow", "gray70"), "Light Blue":("light sky blue", "RoyalBlue4"), "Dark Blue":("midnight blue", "RoyalBlue1"), "Light Green":("DarkOliveGreen1", "darkgreen"), "Dark Green":("darkgreen", "DarkOliveGreen1"), "Light Orange":("coral", "OrangeRed4"), "Dark Orange":("Orangered4", "coral"), "Red":("red4", "coral"), "Yellow":("goldenrod","lightgoldenrod"), "Black":("gray1","gray64"), "Light Purple":("MediumPurple1", "purple4"), "Dark Purple":("purple4", "MediumPurple1"), "Light Pink":("orchid1", "DeepPink4"), "Dark Pink":("maroon4", "orchid1"), "Blackpink":("gray15", "orchid1")}
            theme = menu.get()
            global bg_color
            global fg_color
            global font

            bg_color = themedict.get(theme)[0]
            fg_color = themedict.get(theme)[1]
            
            window.configure(background=bg_color)
            if theme == "Halloween":
                font = "Jokerman"
            elif theme == "Christmas":
                font = "Forte"
            else:
                font = "Arial"

            c.execute(f'UPDATE Settings SET "bg_color" = "{bg_color}" WHERE ProfileNumber = 0')
            c.execute(f'UPDATE Settings SET "fg_color" = "{fg_color}" WHERE ProfileNumber = 0')
            c.execute(f'UPDATE Settings SET "font" = "{font}" WHERE ProfileNumber = 0')

            conn.commit()

            t_drop_title.destroy()
            t_drop.destroy()
            Next.destroy()
            Back.destroy()
            showinfo("Saved", f"{theme} saved as your default theme successfully")
            main()
                

        def changed_option(self):
            if checkdb(directory) != "Validated":
                ShowDbError()
            theme = menu.get()
            global fg_color
            global bg_color
            themedict = {"Halloween":("gray20", "darkorange"), "Christmas":("firebrick4", "limegreen"), "White":("snow", "gray70"), "Light Blue":("light sky blue", "RoyalBlue4"), "Dark Blue":("midnight blue", "RoyalBlue1"), "Light Green":("DarkOliveGreen1", "darkgreen"), "Dark Green":("darkgreen", "DarkOliveGreen1"), "Light Orange":("coral", "OrangeRed4"), "Dark Orange":("Orangered4", "coral"), "Red":("red4", "coral"), "Yellow":("goldenrod","lightgoldenrod"), "Black":("gray1","gray64"), "Light Purple":("MediumPurple1", "purple4"), "Dark Purple":("purple4", "MediumPurple1"), "Light Pink":("orchid1", "DeepPink4"), "Dark Pink":("maroon4", "orchid1"), "Blackpink":("gray15", "orchid1")}
            
            if theme == "Halloween":
                tempfont = "Jokerman"
            elif theme == "Christmas":
                tempfont = "Forte"
            else:
                tempfont = "Arial"

            tempbg_color = themedict.get(theme)[0]
            tempfg_color = themedict.get(theme)[1]
            window.configure(background=tempbg_color)

            t_style.configure("TMenubutton", background=tempfg_color, foreground=tempbg_color, font=tempfont)
            t_drop_title.configure(fg=tempfg_color, bg=tempbg_color, font=tempfont)
            Next.configure(fg=tempfg_color, bg=tempbg_color, font=tempfont)
            Back.configure(fg=tempfg_color, bg=tempbg_color, font=tempfont)

        menubar.destroy()
        menu = StringVar(window)
        options = ["Halloween","Christmas", "White", 'Light Blue', 'Dark Blue', "Light Green", "Dark Green", 'Light Orange', 'Dark Orange' , 'Red', 'Yellow', 'Black', 'Light Purple', 'Dark Purple', 'Light Pink',
                'Dark Pink', 'Blackpink']

        t_drop_title = Label(window, text='Select a theme to set as default theme', fg=fg_color, bg=bg_color,
                             activebackground=fg_color, activeforeground=bg_color, font=(font, 12))
        t_drop_title.pack(pady=(0, 10))
        t_drop = ttk.OptionMenu(window, menu, 'Select a theme', *(options), command=changed_option)
        t_drop.pack(pady=(0, 20))

        t_style = ttk.Style()
        t_style.configure("TMenubutton", background=fg_color, foreground=bg_color, font=font)

        Next = Button(window, text='Save changes', fg=fg_color, bg=bg_color, activebackground=fg_color,
                      activeforeground=bg_color, command=next)
        Next.pack(pady=(10, 0))

        def back():
            if checkdb(directory) != "Validated":
                ShowDbError()
            global bg_color
            global fg_color
            bg_color = bg_color
            fg_color = fg_color
            window.configure(background=bg_color)
            t_drop.destroy()
            t_drop_title.destroy()
            Next.destroy()
            Back.destroy()
            main()

        Back = Button(window, text='Back', fg=fg_color, bg=bg_color, activebackground=fg_color,
                      activeforeground=bg_color, command=back)
        Back.pack(side="bottom", anchor="sw")

    def s_default_font():
        if checkdb(directory) != "Validated":
            ShowDbError()
        text1.destroy()
        b_add.destroy()
        b_list.destroy()
        exitb.destroy()

        def next():
            if checkdb(directory) != "Validated":
                ShowDbError()

            global font    
            conn = sqlite3.connect(directory)
            c = conn. cursor()
            font = menu.get()
            
            c.execute(f'UPDATE Settings SET "font" = "{font}" WHERE ProfileNumber = 0')
            conn.commit()
            f_drop_title.destroy()
            f_drop.destroy()
            Next.destroy()
            Back.destroy()
            showinfo("Saved", f"{font.title()} saved as your default font successfully")
            conn.close()
            main()

        def changed_option(self):
            if checkdb(directory) != "Validated":
                ShowDbError()
            global font
            tempfont = menu.get()

            f_style.configure("TMenubutton", font=tempfont)
            f_drop_title.configure(font=tempfont)
            Next.configure(font=tempfont)

        global fg_color
        global bg_color
        global font
        menubar.destroy()
        menu = StringVar(window)
        f_options = ["Arial", "Cambria", "Sylfaen", "Candara", "Georgia", "Verdana", "SimSun", "Calibri", "Consolas", "Century", "Forte", "Courier", "Jokerman", "Mistral", "Vivaldi", "Rockwell", "Onyx"]
        f_drop_title = Label(window, text='Select a font to set as default font', fg=fg_color, bg=bg_color,
                             activebackground=fg_color, activeforeground=bg_color, font=(font, 12))
        f_drop_title.pack(pady=(0, 10))
        f_drop = ttk.OptionMenu(window, menu, 'Choose one', *(f_options), command=changed_option)
        f_drop.pack(pady=(0, 20))

        f_style = ttk.Style()
        f_style.configure("TMenubutton", background=fg_color, foreground=bg_color, font=font)

        Next = Button(window, text='Save changes', fg=fg_color, bg=bg_color, activebackground=fg_color,
                      activeforeground=bg_color, command=next)
        Next.pack(pady=(10, 0))

        def back():
            if checkdb(directory) != "Validated":
                ShowDbError()
            global fg_color
            global bg_color
            global font
            bg_color = bg_color
            fg_color = fg_color
            font = font
            window.configure(background=bg_color)
            f_drop.destroy()
            f_drop_title.destroy()
            Next.destroy()
            Back.destroy()
            main()

        Back = Button(window, text='Back', fg=fg_color, bg=bg_color, activebackground=fg_color,
                      activeforeground=bg_color, command=back)
        Back.pack(side="bottom", anchor="sw")

    menubar = Menu(window, fg=fg_color, bg=bg_color)

    themes = Menu(menubar, fg=fg_color, bg=bg_color, activebackground=fg_color, activeforeground=bg_color, tearoff=0)
    ThemeOptions = ["Default", "Halloween","Christmas", "White", 'Light Blue', 'Dark Blue', "Light Green", "Dark Green", 'Light Orange', 'Dark Orange' , 'Red', 'Yellow', 'Black', 'Light Purple', 'Dark Purple', 'Light Pink',
                'Dark Pink', 'Blackpink']
    for option in ThemeOptions:
            themes.add_command(label=option, activebackground=fg_color, activeforeground=bg_color, command= lambda option=option: ChangeCurrentTheme(option),
                       font=font)
    menubar.add_cascade(label='Themes', activebackground=fg_color, activeforeground=bg_color, menu=themes,
                        font=font)
    
    fonts = Menu(menubar, fg=fg_color, bg=bg_color, activebackground=fg_color, activeforeground=bg_color, tearoff=0)
    FontOptions = ["Default", "Arial", "Cambria", "Sylfaen", "Candara", "Georgia", "Verdana", "SimSun", "Calibri", "Consolas", "Century", "Forte", "Courier", "Jokerman", "Mistral", "Vivaldi", "Rockwell", "Onyx"]
    for option in FontOptions:
        fonts.add_command(label=option.title(), activebackground=fg_color, activeforeground=bg_color, command= lambda option=option: ChangeCurrentFont(option),
                      font=option)
    menubar.add_cascade(label='Fonts', activebackground=fg_color, activeforeground=bg_color, menu=fonts, font=font)

    def control():
        if checkdb(directory) != "Validated":
            ShowDbError()
        text1.destroy()
        b_add.destroy()
        b_list.destroy()
        exitb.destroy()
        backup_folder()

    setting = Menu(menubar, fg=fg_color, bg=bg_color, activebackground=fg_color, activeforeground=bg_color, tearoff=0)
    setting.add_command(label='Change your backup folder', activebackground=fg_color, activeforeground=bg_color,
                        command=control, font=font)
    setting.add_command(label='set a default theme', activebackground=fg_color, activeforeground=bg_color,
                        command=s_default_theme, font=font)
    setting.add_command(label='Set a default font', activebackground=fg_color, activeforeground=bg_color,
                        command=s_default_font, font=font)
    menubar.add_cascade(label='Setting', activebackground=fg_color, activeforeground=bg_color, menu=setting, font=font)

    credit = Menu(menubar, fg=fg_color, bg=bg_color, activebackground=fg_color, activeforeground=bg_color, tearoff=0)
    credit.add_command(label='Instagram', activebackground=fg_color, activeforeground=bg_color,
                       command=lambda: os.system('python -m webbrowser -t "https://www.instagram.com/mu._sic_lover"'),
                       font=font)
    credit.add_command(label='Telegram', activebackground=fg_color, activeforeground=bg_color,
                       command=lambda: os.system('python -m webbrowser -t "https://t.me/BP_Galaxy"'), font=font)
    credit.add_command(label='GitHub', activebackground=fg_color, activeforeground=bg_color,
                       command=lambda: os.system('python -m webbrowser -t "https://github.com/BPGalaxy"'), font=font)
    menubar.add_cascade(label='Made by Arthur', activebackground=fg_color, activeforeground=bg_color, menu=credit,
                        font=font)

    window.config(menu=menubar)

    def add():
        if checkdb(directory) != "Validated":
            ShowDbError()
        if len(MovieList) >= 8:
            showerror("Error",
                      "You can't add more than 8 movies in graphical version!\nIf you wanna add more, use command prompt version of app")
            text1.destroy()
            b_add.destroy()
            b_list.destroy()
            exitb.destroy()
            return main()
        menubar.destroy()
        b_list.destroy()
        b_add.destroy()
        text1.destroy()
        exitb.destroy()

        def back():
            if checkdb(directory) != "Validated":
                ShowDbError()
            label.destroy()
            entry.destroy()
            next1.destroy()
            Back.destroy()
            main()

        def values():
            if checkdb(directory) != "Validated":
                ShowDbError()
            global Len1
            Len1 += 1
            try:
                name = entry.get()
                if name == '':
                    showerror('Invalid', 'This filed is necessary!')
                    label.destroy()
                    entry.destroy()
                    next1.destroy()
                    Back.destroy()
                    return add()
                elif name in MovieList:
                    showerror('Already exist', 'Another movie with this name is already exist!')
                    label.destroy()
                    entry.destroy()
                    next1.destroy()
                    Back.destroy()
                    return add()
                label.destroy()
                text1.destroy()
                entry.destroy()
                next1.destroy()
                Back.destroy()
            except:
                pass

            def back2():
                if checkdb(directory) != "Validated":
                    ShowDbError()
                session.destroy()
                e_session.destroy()
                episode.destroy()
                e_episode.destroy()
                time.destroy()
                e_time.destroy()
                next2.destroy()
                Back2.destroy()
                add()

            def save():
                if checkdb(directory) != "Validated":
                    ShowDbError()
                error = False
                v_session = e_session.get()
                v_episode = e_episode.get()
                v_time = e_time.get()
                year = datetime.datetime.now().year
                month = datetime.datetime.now().month
                day = datetime.datetime.now().day
                hour = datetime.datetime.now().hour
                minute = datetime.datetime.now().minute
                second = datetime.datetime.now().second
                date_added = f"\n{year}/{month}/{day}\n{hour}:{minute}:{second}"

                if v_session == '':
                    v_session = '1'
                else:
                    try:
                        int(v_session)
                    except:
                        showwarning('Alert', 'Just enter a number')
                        error = True
                        pass

                if v_episode == '':
                    v_episode = '1'
                else:
                    try:
                        int(v_episode)
                    except:
                        showwarning('Alert', 'Just enter a number')
                        error = True
                        pass

                if v_time == '':
                    v_time = '00:00:00'

                else:
                    T_len = 0
                    num1 = 60
                    num2 = 60
                    try:
                        num1 = int(v_time[3:5])
                        num2 = int(v_time[6:8])
                    except:
                        showwarning('Wrong value', 'Enter a valid time value')
                        error = True
                        pass

                    if num1 > 60 or num2 > 60:
                        showwarning('Wrong value', 'Enter a valid time value')
                        error = True
                        pass

                    elif len(v_time) == 8 and error is False:
                        for letter in v_time:
                            global Len1
                            Len1 = Len1 + 1
                            if T_len == 1 or T_len == 2 or T_len == 4 or T_len == 5 or T_len == 7 or T_len == 8:
                                try:
                                    int(letter)
                                    continue
                                except:
                                    error = True
                                    break

                            elif T_len == 3 or T_len == 6:
                                if letter == ':':
                                    continue
                                else:
                                    error = True
                                    break

                    elif error is False:
                        showwarning('Wrong value', 'Enter a valid time value')
                        error = True
                        pass

                if error is True:
                    session.destroy()
                    e_session.destroy()
                    episode.destroy()
                    e_episode.destroy()
                    time.destroy()
                    e_time.destroy()
                    next2.destroy()
                    Back.destroy()
                    Back2.destroy()
                    movies()

                else:
                    c = conn.cursor()
                    c.execute(f'INSERT INTO MovieData(moviename, dateadded, session, episode, time, status, datefinished) VALUES ("{name}", "{date_added}", {v_session}, {v_episode}, "{v_time}", "False", "0")')
                    conn.commit()
                    c.close()

                    showinfo('Saved', 'New movie added to list successfully')
                    session.destroy()
                    e_session.destroy()
                    episode.destroy()
                    e_episode.destroy()
                    time.destroy()
                    e_time.destroy()
                    next2.destroy()
                    Back.destroy()
                    Back2.destroy()
                    main()

            session = Label(window, text="Enter up to the session you've watched", fg=fg_color, bg=bg_color,
                            activebackground=fg_color, activeforeground=bg_color, font=font)
            e_session = Entry(window, fg=fg_color, bg=bg_color, font=font)
            session.pack(pady=5)
            e_session.pack()

            episode = Label(window, text="Enter up to the episode you've watched", fg=fg_color, bg=bg_color,
                            activebackground=fg_color, activeforeground=bg_color, font=font)
            e_episode = Entry(window, fg=fg_color, bg=bg_color, font=font)
            episode.pack(pady=5)
            e_episode.pack()

            time = Label(window, text="Enter up to the time you've watched\nHint: enter the time by example: 00:00:00",
                         fg=fg_color, bg=bg_color, activebackground=fg_color, activeforeground=bg_color, font=font)
            e_time = Entry(window, fg=fg_color, bg=bg_color, font=font)
            time.pack(pady=5)
            e_time.pack()

            next2 = Button(window, text='Next', fg=fg_color, bg=bg_color, activebackground=fg_color,
                           activeforeground=bg_color, command=save, font=font)
            next2.pack(pady=7)
            next2.bind('<Enter>', func=lambda e: next2.config(bg=fg_color, fg=bg_color))
            next2.bind('<Leave>', func=lambda e: next2.config(bg=bg_color, fg=fg_color))

            Back2 = Button(window, text='Back', fg=fg_color, bg=bg_color, activebackground=fg_color,
                           activeforeground=bg_color, command=back2, font=font)
            Back2.pack(side="bottom", anchor="sw")
            Back2.bind('<Enter>', func=lambda e: Back2.config(bg=fg_color, fg=bg_color))
            Back2.bind('<Leave>', func=lambda e: Back2.config(bg=bg_color, fg=fg_color))

            if Len1 <= 1:
                showwarning("Hint",
                            "If you don't fill a form, default value will be saved\nDefault values:\nsession: 1\nepisode: 1\ntime: 00:00:00")

        label = Label(window, text="Enter your movie's name", fg=fg_color, bg=bg_color, activebackground=fg_color,
                      activeforeground=bg_color, font=font)
        label.pack()

        entry = Entry(window, fg=fg_color, bg=bg_color, font=font)
        entry.pack()
        entry.bind('<Enter>', func=lambda e: entry.config(bg=fg_color, fg=bg_color))
        entry.bind('<Leave>', func=lambda e: entry.config(bg=bg_color, fg=fg_color))

        next1 = Button(window, text='Next', fg=fg_color, bg=bg_color, activebackground=fg_color,
                       activeforeground=bg_color, command=values, font=font)
        next1.pack(pady=10)
        next1.bind('<Enter>', func=lambda e: next1.config(bg=fg_color, fg=bg_color))
        next1.bind('<Leave>', func=lambda e: next1.config(bg=bg_color, fg=fg_color))

        Back = Button(window, text='Back', fg=fg_color, bg=bg_color, activebackground=fg_color,
                      activeforeground=bg_color, command=back, font=font)
        Back.pack(side="bottom", anchor="sw")
        Back.bind('<Enter>', func=lambda e: Back.config(bg=fg_color, fg=bg_color))
        Back.bind('<Leave>', func=lambda e: Back.config(bg=bg_color, fg=fg_color))

    def movies():
        if checkdb(directory) != "Validated":
            ShowDbError()

        conn = sqlite3.connect(directory)
        MovieListTemp = c.execute("SELECT moviename FROM MovieData").fetchall()
        MovieList = []

        for a in MovieListTemp:
            for b in a:
                MovieList.append(b)

        menubar.destroy()
        b_add.destroy()
        b_list.destroy()
        text1.destroy()
        exitb.destroy()
        exitb.destroy()

        values = {}

        def back3():
            if checkdb(directory) != "Validated":
                ShowDbError()
            try:
                none.destroy()
                suggest.destroy()
            except:
                m_label.destroy()
                for section in MovieList:
                    button_name = f"section_{section}"
                    if button_name == "section_Settings":
                        continue
                    else:
                        section_buttons[button_name].destroy()
            Back3.destroy()
            main()

        def make_show(choice, status):
            if checkdb(directory) != "Validated":
                ShowDbError()

            def back4():
                if checkdb(directory) != "Validated":
                    ShowDbError()
                name.destroy()
                for value in values:
                    values[value].destroy()
                b_1.destroy()
                b_2.destroy()
                Back4.destroy()
                movies()

            def update(movie: str):
                if checkdb(directory) != "Validated":
                    ShowDbError()
                global Len2
                global c
                Len2 += 1
                name.destroy()
                for value in values:
                    values[value].destroy()
                b_1.destroy()
                b_2.destroy()
                Back4.destroy()
                c = conn.cursor()


                def back5():
                    if checkdb(directory) != "Validated":
                        ShowDbError()
                    c = conn.cursor()
                    MStatus = c.execute(f'SELECT status FROM MovieData WHERE moviename = "{movie}"').fetchall()[0][0]
                    session.destroy()
                    e_session.destroy()
                    episode.destroy()
                    e_episode.destroy()
                    time.destroy()
                    e_time.destroy()
                    next2.destroy()
                    Back5.destroy()
                    SetAsWatched.destroy()
                    make_show(movie, MStatus)

                def save():
                    if checkdb(directory) != "Validated":
                        ShowDbError()
                    error = False
                    v_session = e_session.get()
                    v_episode = e_episode.get()
                    v_time = e_time.get()
                    if v_session == '':
                        v_session = c.execute(f'SELECT session FROM MovieData WHERE moviename = "{movie}"').fetchall()[0][0]
                    else:
                        try:
                            int(v_session)
                        except:
                            showwarning('Alert', 'Just enter a number')
                            error = True
                            pass

                    if v_episode == '':
                        v_episode = c.execute(f'SELECT episode FROM MovieData WHERE moviename = "{movie}"').fetchall()[0][0]
                    else:
                        try:
                            int(v_episode)
                        except:
                            showwarning('Alert', 'Just enter a number')
                            error = True
                            pass

                    if v_time == '':
                        v_time = c.execute(f'SELECT time FROM MovieData WHERE moviename = "{movie}"').fetchall()[0][0]

                    else:
                        T_len = 0
                        num1 = 60
                        num2 = 60
                        try:
                            num1 = int(v_time[3:5])
                            num2 = int(v_time[6:8])
                        except:
                            showwarning('Wrong value', 'Enter a valid time value')
                            error = True
                            pass

                        if num1 > 60 or num2 > 60:
                            showwarning('Wrong value', 'Enter a valid time value')
                            error = True
                            pass

                        elif len(v_time) == 8 and error is False:
                            for letter in v_time:
                                T_len = T_len + 1
                                if T_len == 1 or T_len == 2 or T_len == 4 or T_len == 5 or T_len == 7 or T_len == 8:
                                    try:
                                        int(letter)
                                        continue
                                    except:
                                        error = True
                                        break

                                elif T_len == 3 or T_len == 6:
                                    if letter == ':':
                                        continue
                                    else:
                                        error = True
                                        break

                        elif error is False:
                            showwarning('Wrong value', 'Enter a valid time value')
                            error = True
                            pass

                    if error is True:
                        session.destroy()
                        e_session.destroy()
                        episode.destroy()
                        e_episode.destroy()
                        time.destroy()
                        e_time.destroy()
                        next2.destroy()
                        Back4.destroy()
                        Back5.destroy()
                        SetAsWatched.destroy()
                        update(movie)

                    else:
                        c.execute(f'UPDATE MovieData SET "session" = "{v_session}" WHERE moviename = "{movie}"')
                        c.execute(f'UPDATE MovieData SET "episode" = "{v_episode}" WHERE moviename = "{movie}"')
                        c.execute(f'UPDATE MovieData SET "time" = "{v_time}" WHERE moviename = "{movie}"')
                        conn.commit()
                        conn.close
                        
                        showinfo('Saved', 'Changes saved successfully')
                        session.destroy()
                        e_session.destroy()
                        episode.destroy()
                        e_episode.destroy()
                        time.destroy()
                        e_time.destroy()
                        next2.destroy()
                        Back4.destroy()
                        Back5.destroy()
                        SetAsWatched.destroy()
                        make_show(movie, 'False')
                def saw():
                    if checkdb(directory) != "Validated":
                        ShowDbError()
                    yesno = askyesno("Set As Watched", "Did you finish watching this movie?")
                    if yesno is True:
                        year = datetime.datetime.now().year
                        month = datetime.datetime.now().month
                        day = datetime.datetime.now().day
                        hour = datetime.datetime.now().hour
                        minute = datetime.datetime.now().minute
                        second = datetime.datetime.now().second

                        date_finished = f"\n{year}/{month}/{day}\n{hour}:{minute}:{second}"

                        c = conn.cursor()

                        c.execute(f'UPDATE MovieData SET "datefinished" = "{date_finished}" WHERE moviename = "{movie}"')
                        c.execute(f'UPDATE MovieData SET "status" = "True" WHERE moviename = "{movie}"')
                        conn.commit()
                        conn.close()

                        showinfo("Set As Watched", "Set the status for this movie as watched!")
                        session.destroy()
                        e_session.destroy()
                        episode.destroy()
                        e_episode.destroy()
                        time.destroy()
                        e_time.destroy()
                        next2.destroy()
                        Back4.destroy()
                        Back5.destroy()
                        SetAsWatched.destroy()
                        make_show(movie, 'True')

                session = Label(window, text="Enter up to the session you've watched", fg=fg_color, bg=bg_color,
                                activebackground=fg_color, activeforeground=bg_color, font=font)
                e_session = Entry(window, fg=fg_color, bg=bg_color, font=font)
                session.pack(pady=5)
                e_session.pack()
                e_session.bind('<Enter>', func=lambda e: e_session.config(bg=fg_color, fg=bg_color))
                e_session.bind('<Leave>', func=lambda e: e_session.config(bg=bg_color, fg=fg_color))

                episode = Label(window, text="Enter up to the episode you've watched", fg=fg_color, bg=bg_color,
                                activebackground=fg_color, activeforeground=bg_color, font=font)
                e_episode = Entry(window, fg=fg_color, bg=bg_color, font=font)
                episode.pack(pady=5)
                e_episode.pack()
                e_episode.bind('<Enter>', func=lambda e: e_episode.config(bg=fg_color, fg=bg_color))
                e_episode.bind('<Leave>', func=lambda e: e_episode.config(bg=bg_color, fg=fg_color))

                time = Label(window,
                             text="Enter up to the time you've watched\nHint: enter the time by example: 00:00:00",
                             fg=fg_color, bg=bg_color, activebackground=fg_color, activeforeground=bg_color, font=font)
                e_time = Entry(window, fg=fg_color, bg=bg_color, font=font)
                time.pack(pady=5)
                e_time.pack()
                e_time.bind('<Enter>', func=lambda e: e_time.config(bg=fg_color, fg=bg_color))
                e_time.bind('<Leave>', func=lambda e: e_time.config(bg=bg_color, fg=fg_color))

                next2 = Button(window, text='Next', fg=fg_color, bg=bg_color, activebackground=fg_color,
                               activeforeground=bg_color, command=save, font=font)
                next2.pack(pady=7)
                next2.bind('<Enter>', func=lambda e: next2.config(bg=fg_color, fg=bg_color))
                next2.bind('<Leave>', func=lambda e: next2.config(bg=bg_color, fg=fg_color))

                SetAsWatched = Button(window, text='Set This Movie As Watched', fg=fg_color, bg=bg_color, activebackground=fg_color,
                               activeforeground=bg_color, command=saw, font=font)
                SetAsWatched.pack(pady=7)
                SetAsWatched.bind('<Enter>', func=lambda e: SetAsWatched.config(bg=fg_color, fg=bg_color))
                SetAsWatched.bind('<Leave>', func=lambda e: SetAsWatched.config(bg=bg_color, fg=fg_color))

                Back5 = Button(window, text='Back', fg=fg_color, bg=bg_color, activebackground=fg_color,
                               activeforeground=bg_color, command=back5, font=font)
                Back5.pack(side="bottom", anchor="sw")
                Back5.bind('<Enter>', func=lambda e: Back5.config(bg=fg_color, fg=bg_color))
                Back5.bind('<Leave>', func=lambda e: Back5.config(bg=bg_color, fg=fg_color))
                if Len2 <= 1:
                    Session = c.execute(f'SELECT session FROM MovieData WHERE moviename = "{movie}"').fetchall()[0][0]
                    Episode = c.execute(f'SELECT episode FROM MovieData WHERE moviename = "{movie}"').fetchall()[0][0]
                    Time = c.execute(f'SELECT time FROM MovieData WHERE moviename = "{movie}"').fetchall()[0][0]
                    showwarning("Hint",
                                f"If you don't fill a form, default value will be saved\nDefault values:\nsession: {Session}\nepisode: {Episode}\ntime: {Time}")

            def delete(movie: str, status):
                if checkdb(directory) != "Validated":
                    ShowDbError()
                if status == "False":
                    name.destroy()
                    for value in values:
                        values[value].destroy()
                    b_1.destroy()
                    b_2.destroy()
                    Back4.destroy()
                else:
                    name.destroy()
                    watched_t.destroy()
                    for value in values:
                        values[value].destroy()
                    b_2.destroy()
                    Back6.destroy()

                def yes():
                    if checkdb(directory) != "Validated":
                        ShowDbError()

                    conn = sqlite3.connect(directory)
                    c = conn.cursor()
                    c.execute(f'DELETE FROM MovieData WHERE moviename = "{movie}"')
                    conn.commit()
                    conn.close()

                    showinfo('Deleted', f"{movie} deleted from your movie's list successfully")
                    ask.destroy()
                    yes.destroy()
                    No.destroy()
                    movies()

                def no(status):
                    if checkdb(directory) != "Validated":
                        ShowDbError()
                    ask.destroy()
                    yes.destroy()
                    No.destroy()
                    make_show(movie, status)

                ask = Label(window, text=f"Are you sure you wanna delete: \n{movie}\n From your movie's list",
                            fg=fg_color, bg=bg_color, activebackground=fg_color, activeforeground=bg_color, font=(font, 14))
                yes = Button(window, text="Yes, i'm sure", fg=fg_color, bg=bg_color, activebackground=fg_color,
                             activeforeground=bg_color, command=yes, font=font)
                No = Button(window, text="No, take me back", fg=fg_color, bg=bg_color, activebackground=fg_color,
                            activeforeground=bg_color, command=lambda: no(status), font=font)
                ask.pack()
                yes.pack(pady=(40, 0))
                No.pack()
                yes.bind('<Enter>', func=lambda e: yes.config(bg=fg_color, fg=bg_color))
                yes.bind('<Leave>', func=lambda e: yes.config(bg=bg_color, fg=fg_color))
                No.bind('<Enter>', func=lambda e: No.config(bg=fg_color, fg=bg_color))
                No.bind('<Leave>', func=lambda e: No.config(bg=bg_color, fg=fg_color))

            m_label.destroy()
            for section in MovieList:
                button_name = f"section_{section}"
                if button_name == "section_Settings":
                    continue
                else:
                    section_buttons[button_name].destroy()
            Back3.destroy()

            def back6():
                if checkdb(directory) != "Validated":
                    ShowDbError()
                name.destroy()
                watched_t.destroy()
                for value in values:
                    values[value].destroy()
                b_2.destroy()
                Back6.destroy()
                movies()

            name = Label(window, text=choice, fg=fg_color, bg=bg_color, activebackground=fg_color,
                         activeforeground=bg_color, font=(font, 18))
            name.pack()

            titles = ["Date Added", "Session", "Episode", "Time"]
            Len = 0
            if status == "False":
                for value in c.execute(f"SELECT * FROM MovieData WHERE moviename = '{choice}'").fetchall()[0]:
                    if value == choice:
                        continue
                    values[str(titles[Len])] = Label(window, text=titles[Len] + ': ' + str(value), fg=fg_color,
                                          bg=bg_color, activebackground=fg_color, activeforeground=bg_color, font=(font, 13))

                    if titles[Len] == 'Date Added':
                        values[str(titles[Len])].pack(anchor='center', pady=(25, 0))
                    else:
                        values[str(titles[Len])].pack(anchor='center')
                    if titles[Len] == "Time":
                        break
                    Len += 1
                Back4 = Button(window, text='Back', fg=fg_color, bg=bg_color, activebackground=fg_color,
                               activeforeground=bg_color, command=back4, font=font)
                Back4.pack(side="bottom", anchor="sw")
                Back4.bind('<Enter>', func=lambda e: Back4.config(bg=fg_color, fg=bg_color))
                Back4.bind('<Leave>', func=lambda e: Back4.config(bg=bg_color, fg=fg_color))

                b_1 = Button(window, text='Update information', fg=fg_color, bg=bg_color, activebackground=fg_color,
                             activeforeground=bg_color, command=lambda: update(choice), font=font)
                b_1.bind('<Enter>', func=lambda e: b_1.config(bg=fg_color, fg=bg_color))
                b_1.bind('<Leave>', func=lambda e: b_1.config(bg=bg_color, fg=fg_color))
                b_1.pack(side='bottom',)

                b_2 = Button(window, text='Delete this movie from list', fg=fg_color, bg=bg_color,
                             activebackground=fg_color, activeforeground=bg_color, command=lambda: delete(choice, status), font=font)
                b_2.pack(side='bottom')
                b_2.bind('<Enter>', func=lambda e: b_2.config(bg=fg_color, fg=bg_color))
                b_2.bind('<Leave>', func=lambda e: b_2.config(bg=bg_color, fg=fg_color))

            else:
                watched_t = Label(window, text="You finished watching this movie.", fg=fg_color,
                                  bg=bg_color, activebackground=fg_color, activeforeground=bg_color, font=(font, 13))
                watched_t.pack(anchor='center', pady=(20, 20))

                titles = ["Date Added", "Date Finished"]
                Date_Added = c.execute(f'SELECT "dateadded" FROM MovieData WHERE moviename = "Arcane"').fetchall()[0][0]
                Date_Finished = c.execute(f'SELECT "datefinished" FROM MovieData WHERE moviename = "{choice}"').fetchall()[0][0]

                values[str(titles[0])] = Label(window, text=titles[0] + ': ' + Date_Added, fg=fg_color,
                                          bg=bg_color, activebackground=fg_color, activeforeground=bg_color, font=font)
                values[str(titles[0])].pack(anchor='center')

                values[str(titles[1])] = Label(window, text=titles[1] + ': ' + str(Date_Finished), fg=fg_color,
                                          bg=bg_color, activebackground=fg_color, activeforeground=bg_color, font=font)
                values[str(titles[1])].pack(anchor='center')


                Back6 = Button(window, text='Back', fg=fg_color, bg=bg_color, activebackground=fg_color,
                               activeforeground=bg_color, command=back6)
                Back6.pack(side="bottom", anchor="sw")
                Back6.bind('<Enter>', func=lambda e: Back6.config(bg=fg_color, fg=bg_color))
                Back6.bind('<Leave>', func=lambda e: Back6.config(bg=bg_color, fg=fg_color))

                b_2 = Button(window, text='Delete this movie from list', fg=fg_color, bg=bg_color,
                                 activebackground=fg_color, activeforeground=bg_color, command=lambda: delete(choice, status))
                b_2.pack(anchor='s', pady=(42, 0))
                b_2.bind('<Enter>', func=lambda e: b_2.config(bg=fg_color, fg=bg_color))
                b_2.bind('<Leave>', func=lambda e: b_2.config(bg=bg_color, fg=fg_color))

        section_buttons = {}
        if MovieList == []:
            def suggest():
                if checkdb(directory) != "Validated":
                    ShowDbError()
                none.destroy()
                suggest.destroy()
                Back3.destroy()
                add()

            none = Label(window, text="Looks like you haven't added any movies yet...", fg=fg_color, bg=bg_color,
                         activebackground=fg_color, activeforeground=bg_color, font=(font, 12))
            none.pack(pady=(100, 0))

            suggest = Button(window, text='Add a movie now!', fg=fg_color, bg=bg_color, activebackground=fg_color,
                             activeforeground=bg_color, command=suggest, font=font)
            suggest.pack(pady=(10, 0))

            suggest.bind('<Enter>', func=lambda e: suggest.config(bg=fg_color, fg=bg_color))
            suggest.bind('<Leave>', func=lambda e: suggest.config(bg=bg_color, fg=fg_color))

        else:
            m_label = Label(window, text='Your movies:', fg=fg_color, bg=bg_color, activebackground=fg_color,
                            activeforeground=bg_color, font=(font, 18))
            m_label.pack(anchor='center', pady=(0, 10))

            for section in MovieList:
                button_name = f"section_{section}"
                section_buttons[button_name] = Button(window, text=section, fg=fg_color, bg=bg_color,
                                                      activebackground=fg_color, activeforeground=bg_color,
                                                      font=font, command=lambda section=section: make_show(section, c.execute(f"SELECT status FROM MovieData WHERE moviename = '{section}'").fetchall()[0][0]))
                section_buttons[button_name].pack(anchor='center', pady=3)

        Back3 = Button(window, text='Back', fg=fg_color, bg=bg_color, activebackground=fg_color,
                       activeforeground=bg_color, command=back3, font=font)
        Back3.pack(side="bottom", anchor="se")

        Back3.bind('<Enter>', func=lambda e: Back3.config(bg=fg_color, fg=bg_color))
        Back3.bind('<Leave>', func=lambda e: Back3.config(bg=bg_color, fg=fg_color))

    text1 = Label(window, text='Choose one:', fg=fg_color, bg=bg_color, activebackground=fg_color,
                  activeforeground=bg_color, font=(font, 18))
    text1.pack(anchor="center",pady=20)

    b_add = Button(window, text='New Movie', fg=fg_color, bg=bg_color, activebackground=fg_color,
                   activeforeground=bg_color, command=add, font=font)
    b_list = Button(window, text='Movie List', fg=fg_color, bg=bg_color, activebackground=fg_color,
                    activeforeground=bg_color, command=movies, font=font)
    b_add.pack(anchor="center", pady=10)
    b_list.pack(anchor="center")

    b_add.bind('<Enter>', func=lambda e: b_add.config(bg=fg_color, fg=bg_color))
    b_add.bind('<Leave>', func=lambda e: b_add.config(bg=bg_color, fg=fg_color))
    b_list.bind('<Enter>', func=lambda e: b_list.config(bg=fg_color, fg=bg_color))
    b_list.bind('<Leave>', func=lambda e: b_list.config(bg=bg_color, fg=fg_color))

    def quit(event):
        if checkdb(directory) != "Validated":
            ShowDbError()
        window.destroy()

    exitb = Button(window, text='exit', fg=fg_color, bg=bg_color, activebackground=fg_color, activeforeground=bg_color, font=font)
    exitb.pack(side="bottom", anchor="sw")

    exitb.bind('<Enter>', func=lambda e: exitb.config(bg=fg_color, fg=bg_color))
    exitb.bind('<Leave>', func=lambda e: exitb.config(bg=bg_color, fg=fg_color))

    exitb.bind('<Double-1>', quit)
    exitb.bind('<Enter>')


def backup_folder():
    if checkdb(directory) != "Validated":
        ShowDbError()
        
    conn = sqlite3.connect(directory)
    c = conn.cursor()

    b_dir = tkinter.filedialog.askdirectory(mustexist=True, title='Select a backup dir')
    if b_dir == '':
        main()
    else:
        c = conn.cursor()
        c.execute(f'UPDATE Settings SET "backup_dir" = "{b_dir}" WHERE ProfileNumber = 0')
        conn.commit()

        showinfo('Backup dir', 'Default backup dir saved successfully\nYou can change it anytime from menubar')
        global bg_color
        global fg_color
        global font
        try:
            bg_color = c.execute("SELECT bg_color FROM Settings WHERE ProfileNumber = 0").fetchall()[0][0]
            fg_color = c.execute("SELECT fg_color FROM Settings WHERE ProfileNumber = 0").fetchall()[0][0]
            font = c.execute("SELECT font FROM Settings WHERE ProfileNumber = 0").fetchall()[0][0]
        except:
            ShowDbError()
        window.configure(bg=bg_color)
        conn.close()
        try:
            os.remove(str(os.getcwd()) + "/UpdateDB.py")
        except:
            pass
        return main()


def Setting():
    if os.path.exists(directory):
        conn = sqlite3.connect(directory)
        c = conn.cursor()
        global bg_color
        global fg_color
        global font
        
        global auth
        if checkdb(directory) == "Validated":
            if c.execute("SELECT backup_dir FROM Settings WHERE ProfileNumber = 0").fetchall()[0][0]== 'none':
                showinfo('Backup dir',
                         'You must select a directory to app be able to make auto backup from your datas there')
                backup_folder()
            else:
                try:
                    bg_color = c.execute("SELECT bg_color FROM Settings WHERE ProfileNumber = 0").fetchall()[0][0]
                    fg_color = c.execute("SELECT fg_color FROM Settings WHERE ProfileNumber = 0").fetchall()[0][0]
                    font = c.execute("SELECT font FROM Settings WHERE ProfileNumber = 0").fetchall()[0][0]
                except:
                    ShowDbError()
                window.configure(bg=bg_color)
                auth = c.execute("SELECT auth FROM Settings WHERE ProfileNumber = 0").fetchall()[0][0]
                return main()
        else:
            showerror('Invalid db file',
                         'Your DataBase File Is Invalid.\nTry Recovering data or reset db file.')
            conn.close()
            dberror.recovery("self")

    else:
        OldDB = str(os.getcwd()) + "\Movie.ini"
        if os.path.exists(OldDB):
            if 'Database of "My movies" app' in open(OldDB, "r").read():
                Q1 = log.Dialog(None,{'title':'db found','text':"An old 'My Movies' db file found.\n transfer its' data or make a new empty db?",'default':0,'bitmap':log.DIALOG_ICON,'strings': ("Transfer Data", "Make a new db")})      
                if Q1.num == 0:
                    UpdateDB.Update(OldDB, directory)
                    showinfo("Complete", "Your Datas Transfered successfully!")
                    os.remove(OldDB)
                    os.remove(str(os.getcwd()) + "/UpdateDB.py")
                    return Setting()
                elif Q1.num == 1:
                    os.remove(OldDB)
                    os.remove(str(os.getcwd()) + "/UpdateDB.py")
                    return dberror.NewDB("self")

            else:
                Q2 = log.Dialog(None,{'title':'db invalid','text':"A file named 'Movie.ini' Found but it's not a valid db file for this app.\nmake a new db or recover your .ini file?",'default':0,'bitmap':log.DIALOG_ICON,'strings': ("Recover Data", "Make a new db")})
                
                if Q2.num == 0:
                    a = UpdateDB.dbRecovery(window, directory)
                    if a == "Setting":
                        showinfo("Recovered", "Your datas recoverd!\n Press ok to transfer them to the new db")
                        UpdateDB.Update(OldDB, directory)
                        os.remove(OldDB)
                        os.remove(str(os.getcwd()) + "/UpdateDB.py")
                        return Setting()
                    elif a == "Canceled":
                        return Setting()

                elif Q2.num == 1:
                    os.remove(OldDB)
                    os.remove(str(os.getcwd()) + "/UpdateDB.py")
                    return dberror.NewDB("self")
        else:
            showerror('Error', f"Database file(Movie.db) not found at '{directory}'")
            dberror.recovery("self")

Setting()
window.mainloop()
