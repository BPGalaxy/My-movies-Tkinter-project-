import configparser
import sqlite3
import os
from tkinter.messagebox import *
import shutil
import tkinter

config = configparser.ConfigParser()

def Update(OldDB: dir, directory):
    config.read(OldDB)
    open(directory, "x")
    conn = sqlite3.connect(directory)
    c = conn.cursor()

    bg_color = config["Settings"]["bg_color"]
    fg_color = config["Settings"]["fg_color"]
    font = config["Settings"]["font"]
    backup_dir = config["Settings"]["backup_dir"]

    c.execute("CREATE TABLE Settings(ProfileNumber PRIMARY KEY, bg_color, fg_color, font, backup_dir, auth)")
    c.execute(f'INSERT INTO Settings(ProfileNumber, bg_color, fg_color, font, backup_dir, auth) VALUES (0, "{bg_color}", "{fg_color}", "{font}", "{backup_dir}", "Database of My movies app")')
    c.execute("CREATE TABLE MovieData(moviename PRIMARY KEY, dateadded, session, episode, time, status, datefinished)")

    movies = config.sections()
    movies.pop(0)
    for movie in movies:
        moviename = movie
        dateadded = config[movie]["date added"]
        session = config[movie]["session"]
        episode = config[movie]["episode"] 
        time = config[movie]["time"]
        status = config[movie]["status"]
        c.execute(f'INSERT INTO MovieData(moviename, dateadded, session, episode, time, status, datefinished) VALUES ("{moviename}", "{dateadded}", "{session}", "{episode}", "{time}", "{status}", "0")')
    conn.commit()
    conn.close()
    return 

def dbRecovery(window, directory):
            showinfo("Recovery",
                     f"You must select 'Movie.ini' file to recovery your data")
            file = tkinter.filedialog.askopenfilename(title="Select 'Movie.ini file'",
                                                      filetypes=[('Ini files', '*.ini')])
            global auth
            if file == '':
                return "Canceled"

            elif "Movie.ini" in file:
                shutil.copy(file, str(os.getcwd()))
                
            if 'Database of "My movies" app' in open(str(os.getcwd()) + "/Movie.ini", "r").read():
                 return "Setting"

            else:
                showerror("info", 'This is not a "My movies" database file')
                yesno = askyesno("Question", "Do you wanna try again?")
                if yesno is True:
                    dbRecovery(window, directory)
                else:
                    window.destroy()





        