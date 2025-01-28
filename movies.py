import configparser
import tkinter.filedialog
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import os
import shutil
import datetime

window = Tk()

window.geometry('285x285')
window.minsize(285, 285)
window.maxsize(285, 285)
window.title('movie')
config = configparser.ConfigParser()
directory = str(os.getcwd()) + "\movie.ini"

config.read(directory)
Len1 = 0
Len2 = 0
version = "1.0.0"

def main():
    shutil.copy(directory, config['Settings']['backup_dir'])
    global bg_color
    global fg_color
    global font

    def default_theme():
        global bg_color
        global fg_color
        bg_color = config['Settings']['bg_color']
        fg_color = config['Settings']['fg_color']
        window.configure(bg=bg_color)
        text1.destroy()
        b_add.destroy()
        b_list.destroy()
        exit.destroy()
        main()

    def lightblue_theme():
        global bg_color
        global fg_color
        bg_color = 'light sky blue'
        fg_color = 'RoyalBlue4'
        window.configure(bg=bg_color)
        text1.destroy()
        b_add.destroy()
        b_list.destroy()
        exit.destroy()
        main()

    def darkblue_theme():
        global bg_color
        global fg_color
        bg_color = 'midnight blue'
        fg_color = 'RoyalBlue1'
        window.configure(bg=bg_color)
        text1.destroy()
        b_add.destroy()
        b_list.destroy()
        exit.destroy()
        main()

    def red_theme():
        global bg_color
        global fg_color
        bg_color = 'red4'
        fg_color = 'ivory2'
        window.configure(bg=bg_color)
        text1.destroy()
        b_add.destroy()
        b_list.destroy()
        exit.destroy()
        main()

    def yellow_theme():
        global bg_color
        global fg_color
        bg_color = 'goldenrod'
        fg_color = 'lightgoldenrod'
        window.configure(bg=bg_color)
        text1.destroy()
        b_add.destroy()
        b_list.destroy()
        exit.destroy()
        main()

    def black_theme():
        global bg_color
        global fg_color
        bg_color = 'gray1'
        fg_color = 'gray64'
        window.configure(bg=bg_color)
        text1.destroy()
        b_add.destroy()
        b_list.destroy()
        exit.destroy()
        main()

    def lightpurple_theme():
        global bg_color
        global fg_color
        bg_color = 'MediumPurple1'
        fg_color = 'purple4'
        window.configure(bg=bg_color)
        text1.destroy()
        b_add.destroy()
        b_list.destroy()
        exit.destroy()
        main()

    def darkpurple_theme():
        global bg_color
        global fg_color
        bg_color = 'purple4'
        fg_color = 'MediumPurple1'
        window.configure(bg=bg_color)
        text1.destroy()
        b_add.destroy()
        b_list.destroy()
        exit.destroy()
        main()

    def lightpink_theme():
        global bg_color
        global fg_color
        bg_color = 'orchid1'
        fg_color = 'DeepPink4'
        window.configure(bg=bg_color)
        text1.destroy()
        b_add.destroy()
        b_list.destroy()
        exit.destroy()
        main()

    def darkpink_theme():
        global bg_color
        global fg_color
        bg_color = 'maroon4'
        fg_color = 'orchid1'
        window.configure(bg=bg_color)
        text1.destroy()
        b_add.destroy()
        b_list.destroy()
        exit.destroy()
        main()

    def blackpink_theme():
        global bg_color
        global fg_color
        bg_color = 'gray5'
        fg_color = 'orchid1'
        window.configure(bg=bg_color)
        text1.destroy()
        b_add.destroy()
        b_list.destroy()
        exit.destroy()
        main()

    def default_font():
        global font
        font = 'arial'
        text1.destroy()
        b_add.destroy()
        b_list.destroy()
        exit.destroy()
        main()

    def cambria_font():
        global font
        font = 'cambria'
        text1.destroy()
        b_add.destroy()
        b_list.destroy()
        exit.destroy()
        main()

    def sylfaen_font():
        global font
        font = 'sylfaen'
        text1.destroy()
        b_add.destroy()
        b_list.destroy()
        exit.destroy()
        main()

    def candara_font():
        global font
        font = 'candara'
        text1.destroy()
        b_add.destroy()
        b_list.destroy()
        exit.destroy()
        main()

    def s_default_theme():
        text1.destroy()
        b_add.destroy()
        b_list.destroy()
        exit.destroy()

        def next():
            theme = menu.get()
            if theme == 'Light Blue':
                global bg_color
                global fg_color
                bg_color = 'light sky blue'
                fg_color = 'RoyalBlue4'
                window.configure(background=bg_color)
                config['Settings'] = {'bg_color': bg_color,
                                      'fg_color': fg_color,
                                      'font': config['Settings']['font'],
                                      'backup_dir': config['Settings']['backup_dir']}
                with open(directory, 'w') as config_file:
                    config.write(config_file)
                t_drop_title.destroy()
                t_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{theme} saved as your default theme successfully")
                main()
                config.read(directory)

            elif theme == 'Dark Blue':
                bg_color = 'midnight blue'
                fg_color = 'RoyalBlue1'
                window.configure(background=bg_color)
                config['Settings'] = {'bg_color': bg_color,
                                      'fg_color': fg_color,
                                      'font': config['Settings']['font'],
                                      'backup_dir': config['Settings']['backup_dir']}
                with open(directory, 'w') as config_file:
                    config.write(config_file)
                t_drop_title.destroy()
                t_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{theme} saved as your default theme successfully")
                main()
                config.read(directory)

            elif theme == 'Red':
                bg_color = 'red4'
                fg_color = 'ivory2'
                window.configure(background=bg_color)
                config['Settings'] = {'bg_color': bg_color,
                                      'fg_color': fg_color,
                                      'font': config['Settings']['font'],
                                      'backup_dir': config['Settings']['backup_dir']}
                with open(directory, 'w') as config_file:
                    config.write(config_file)
                t_drop_title.destroy()
                t_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{theme} saved as your default theme successfully")
                main()
                config.read(directory)

            elif theme == 'Yellow':
                bg_color = 'goldenrod'
                fg_color = 'lightgoldenrod'
                window.configure(background=bg_color)
                config['Settings'] = {'bg_color': bg_color,
                                      'fg_color': fg_color,
                                      'font': config['Settings']['font'],
                                      'backup_dir': config['Settings']['backup_dir']}
                with open(directory, 'w') as config_file:
                    config.write(config_file)
                t_drop_title.destroy()
                t_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{theme} saved as your default theme successfully")
                main()
                config.read(directory)

            elif theme == 'Black':
                bg_color = 'gray1'
                fg_color = 'gray64'
                window.configure(background=bg_color)
                config['Settings'] = {'bg_color': bg_color,
                                      'fg_color': fg_color,
                                      'font': config['Settings']['font'],
                                      'backup_dir': config['Settings']['backup_dir']}
                with open(directory, 'w') as config_file:
                    config.write(config_file)
                t_drop_title.destroy()
                t_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{theme} saved as your default theme successfully")
                main()
                config.read(directory)

            elif theme == 'Light Purple':
                bg_color = 'MediumPurple1'
                fg_color = 'purple4'
                window.configure(background=bg_color)
                config['Settings'] = {'bg_color': bg_color,
                                      'fg_color': fg_color,
                                      'font': config['Settings']['font'],
                                      'backup_dir': config['Settings']['backup_dir']}
                with open(directory, 'w') as config_file:
                    config.write(config_file)
                t_drop_title.destroy()
                t_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{theme} saved as your default theme successfully")
                main()
                config.read(directory)

            elif theme == 'Dark Purple':
                bg_color = 'purple4'
                fg_color = 'MediumPurple1'
                window.configure(background=bg_color)
                config['Settings'] = {'bg_color': bg_color,
                                      'fg_color': fg_color,
                                      'font': config['Settings']['font'],
                                      'backup_dir': config['Settings']['backup_dir']}
                with open(directory, 'w') as config_file:
                    config.write(config_file)
                t_drop_title.destroy()
                t_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{theme} saved as your default theme successfully")
                main()
                config.read(directory)

            elif theme == 'Light Pink':
                bg_color = 'orchid1'
                fg_color = 'DeepPink4'
                window.configure(background=bg_color)
                config['Settings'] = {'bg_color': bg_color,
                                      'fg_color': fg_color,
                                      'font': config['Settings']['font'],
                                      'backup_dir': config['Settings']['backup_dir']}
                with open(directory, 'w') as config_file:
                    config.write(config_file)
                t_drop_title.destroy()
                t_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{theme} saved as your default theme successfully")
                main()
                config.read(directory)

            elif theme == 'Dark Pink':
                bg_color = 'maroon4'
                fg_color = 'orchid1'
                window.configure(background=bg_color)
                config['Settings'] = {'bg_color': bg_color,
                                      'fg_color': fg_color,
                                      'font': config['Settings']['font'],
                                      'backup_dir': config['Settings']['backup_dir']}
                with open(directory, 'w') as config_file:
                    config.write(config_file)
                t_drop_title.destroy()
                t_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{theme} saved as your default theme successfully")
                main()
                config.read(directory)

            elif theme == 'Blackpink':
                bg_color = 'gray5'
                fg_color = 'orchid1'
                window.configure(background=bg_color)
                config['Settings'] = {'bg_color': bg_color,
                                      'fg_color': fg_color,
                                      'font': config['Settings']['font'],
                                      'backup_dir': config['Settings']['backup_dir']}
                with open(directory, 'w') as config_file:
                    config.write(config_file)
                t_drop_title.destroy()
                t_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{theme} saved as your default theme successfully")
                main()
                config.read(directory)

        def changed_option(selected_option):
            theme = menu.get()
            global fg_color
            global bg_color

            if theme == 'Light Blue':
                global bg_color
                global fg_color
                bg_color = 'light sky blue'
                fg_color = 'RoyalBlue4'
                window.configure(background=bg_color)

            elif theme == 'Dark Blue':
                bg_color = 'midnight blue'
                fg_color = 'RoyalBlue1'
                window.configure(background=bg_color)

            elif theme == 'Red':
                bg_color = 'red4'
                fg_color = 'ivory2'
                window.configure(background=bg_color)

            elif theme == 'Yellow':
                bg_color = 'goldenrod'
                fg_color = 'lightgoldenrod'
                window.configure(background=bg_color)

            elif theme == 'Black':
                bg_color = 'gray1'
                fg_color = 'gray64'
                window.configure(background=bg_color)

            elif theme == 'Light Purple':
                bg_color = 'MediumPurple1'
                fg_color = 'purple4'
                window.configure(background=bg_color)

            elif theme == 'Dark Purple':
                bg_color = 'purple4'
                fg_color = 'MediumPurple1'
                window.configure(background=bg_color)

            elif theme == 'Light Pink':
                bg_color = 'orchid1'
                fg_color = 'DeepPink4'
                window.configure(background=bg_color)
                config.read(directory)

            elif theme == 'Dark Pink':
                bg_color = 'maroon4'
                fg_color = 'orchid1'
                window.configure(background=bg_color)

            elif theme == 'Blackpink':
                bg_color = 'gray5'
                fg_color = 'orchid1'
                window.configure(background=bg_color)

            t_style.configure("TMenubutton", background=fg_color, foreground=bg_color)
            t_drop_title.configure(fg=fg_color, bg=bg_color)
            Next.configure(fg=fg_color, bg=bg_color)
            Back.configure(fg=fg_color, bg=bg_color)

        menubar.destroy()
        menu = StringVar(window)
        options = ['Light Blue', 'Dark Blue', 'Red', 'Yellow', 'Black', 'Light Purple', 'Dark Purple', 'Light Pink',
                   'Dark Pink', 'Blackpink']
        global fg_color
        global bg_color
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
            global fg_color
            global bg_color
            fg_color = config['Settings']['fg_color']
            bg_color = config['Settings']['bg_color']
            window.configure(background=bg_color)
            t_drop.destroy()
            t_drop_title.destroy()
            Next.destroy()
            Back.destroy()
            main()

        Back = Button(window, text='Back', fg=fg_color, bg=bg_color, activebackground=fg_color,
                      activeforeground=bg_color, command=back)
        Back.place(y=260)

    def s_default_font():
        text1.destroy()
        b_add.destroy()
        b_list.destroy()
        exit.destroy()

        def next():
            theme = menu.get()
            if theme == 'Arial':
                font = "Arial"
                config['Settings'] = {'bg_color': config['Settings']['bg_color'],
                                      'fg_color': config['Settings']['fg_color'],
                                      'font': font, 'backup_dir': config['Settings']['backup_dir']}
                with open(directory, 'w') as config_file:
                    config.write(config_file)
                f_drop_title.destroy()
                f_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{font.title()} saved as your default font successfully")
                main()

            elif theme == 'Cambria':
                font = "Cambria"
                config['Settings'] = {'bg_color': config['Settings']['bg_color'],
                                      'fg_color': config['Settings']['fg_color'],
                                      'font': font, 'backup_dir': config['Settings']['backup_dir']}
                with open(directory, 'w') as config_file:
                    config.write(config_file)
                f_drop_title.destroy()
                f_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{font.title()} saved as your default font successfully")
                main()

            elif theme == 'Sylfaen':
                font = "Sylfaen"
                config['Settings'] = {'bg_color': config['Settings']['bg_color'],
                                      'fg_color': config['Settings']['fg_color'],
                                      'font': font, 'backup_dir': config['Settings']['backup_dir']}
                with open(directory, 'w') as config_file:
                    config.write(config_file)
                f_drop_title.destroy()
                f_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{font.title()} saved as your default font successfully")
                main()

            elif theme == 'Candara':
                font = "Candara"
                config['Settings'] = {'bg_color': config['Settings']['bg_color'],
                                      'fg_color': config['Settings']['fg_color'],
                                      'font': font, 'backup_dir': config['Settings']['backup_dir']}
                with open(directory, 'w') as config_file:
                    config.write(config_file)
                f_drop_title.destroy()
                f_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{font.title()} saved as your default font successfully")
                main()

        def changed_option(selected_option):
            theme = menu.get()
            global font

            if theme == 'Arial':
                font = 'Arial'

            elif theme == 'Cambria':
                font = 'Cambria'


            elif theme == 'Sylfaen':
                font = 'Sylfaen'

            elif theme == 'Candara':
                font = 'Candara'

            f_style.configure("TMenubutton", font=font)
            f_drop_title.configure(font=font)
            Next.configure(font=font)

        global fg_color
        global bg_color
        global font
        menubar.destroy()
        menu = StringVar(window)
        f_options = ['Arial', 'Cambria', 'Sylfaen', 'Candara']
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
            global fg_color
            global bg_color
            fg_color = config['Settings']['fg_color']
            bg_color = config['Settings']['bg_color']
            window.configure(background=bg_color)
            f_drop.destroy()
            f_drop_title.destroy()
            Next.destroy()
            Back.destroy()
            main()

        Back = Button(window, text='Back', fg=fg_color, bg=bg_color, activebackground=fg_color,
                      activeforeground=bg_color, command=back)
        Back.place(y=260)

    menubar = Menu(window, fg=fg_color, bg=bg_color)

    themes = Menu(menubar, fg=fg_color, bg=bg_color, activebackground=fg_color, activeforeground=bg_color, tearoff=0)
    themes.add_command(label='Default', activebackground=fg_color, activeforeground=bg_color, command=default_theme,
                       font=font)
    themes.add_command(label='Light Blue', activebackground=fg_color, activeforeground=bg_color,
                       command=lightblue_theme, font=font)
    themes.add_command(label='Dark Blue', activebackground=fg_color, activeforeground=bg_color, command=darkblue_theme,
                       font=font)
    themes.add_command(label='red', activebackground=fg_color, activeforeground=bg_color, command=red_theme, font=font)
    themes.add_command(label='yellow', activebackground=fg_color, activeforeground=bg_color, command=yellow_theme,
                       font=font)
    themes.add_command(label='black', activebackground=fg_color, activeforeground=bg_color, command=black_theme,
                       font=font)
    themes.add_command(label='Black Pink', activebackground=fg_color, activeforeground=bg_color,
                       command=blackpink_theme, font=font)
    themes.add_command(label='Light Purple', activebackground=fg_color, activeforeground=bg_color,
                       command=lightpurple_theme, font=font)
    themes.add_command(label='Dark Purple', activebackground=fg_color, activeforeground=bg_color,
                       command=darkpurple_theme, font=font)
    themes.add_command(label='Light Pink', activebackground=fg_color, activeforeground=bg_color,
                       command=lightpink_theme, font=font)
    themes.add_command(label='Dark Pink', activebackground=fg_color, activeforeground=bg_color, command=darkpink_theme,
                       font=font)
    menubar.add_cascade(label='Themes', activebackground=fg_color, activeforeground=bg_color, menu=themes, font=font)

    fonts = Menu(menubar, fg=fg_color, bg=bg_color, activebackground=fg_color, activeforeground=bg_color, tearoff=0)
    fonts.add_command(label='Arial', activebackground=fg_color, activeforeground=bg_color, command=default_font,
                      font='arial')
    fonts.add_command(label='Cambria', activebackground=fg_color, activeforeground=bg_color, command=cambria_font,
                      font='cambria')
    fonts.add_command(label='Sylfaen', activebackground=fg_color, activeforeground=bg_color, command=sylfaen_font,
                      font='sylfaen')
    fonts.add_command(label='Candara', activebackground=fg_color, activeforeground=bg_color, command=candara_font,
                      font='candara')
    menubar.add_cascade(label='Fonts', activebackground=fg_color, activeforeground=bg_color, menu=fonts, font=font)

    def control():
        text1.destroy()
        b_add.destroy()
        b_list.destroy()
        exit.destroy()
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
                       command=lambda: os.system('python -m webbrowser -t "https://t.me/music_lovr2"'), font=font)
    menubar.add_cascade(label='Made by alireza', activebackground=fg_color, activeforeground=bg_color, menu=credit,
                        font=font)

    window.config(menu=menubar)

    def add():
        if len(config.sections()) >= 8:
            showerror("Error",
                      "You can't add more than 8 movies in graphical version!\nIf you wanna add more, use command prompt version of app")
            text1.destroy()
            b_add.destroy()
            b_list.destroy()
            exit.destroy()
            return main()
        menubar.destroy()
        b_list.destroy()
        b_add.destroy()
        text1.destroy()
        exit.destroy()

        def back():
            label.destroy()
            entry.destroy()
            next1.destroy()
            Back.destroy()
            main()

        def values():
            global Len1
            Len1 += 1
            try:
                name = entry.get()
                if name == '':
                    showinfo('Invalid', 'This filed is necessary!')
                    label.destroy()
                    entry.destroy()
                    next1.destroy()
                    Back.destroy()
                    return add()
                elif name in config.sections():
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
                    config[name] = {'date added': date_added, 'session': v_session, 'episode': v_episode, 'time': v_time}
                    auth = config.get('Settings', 'auth')
                    file = open(directory, 'w')
                    file.write(auth)
                    file.close()
                    with open(directory, 'a') as config_file:
                        config.write(config_file)
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
            e_session = Entry(window, fg=fg_color, bg=bg_color)
            session.pack(pady=5)
            e_session.pack()

            episode = Label(window, text="Enter up to the episode you've watched", fg=fg_color, bg=bg_color,
                            activebackground=fg_color, activeforeground=bg_color, font=font)
            e_episode = Entry(window, fg=fg_color, bg=bg_color)
            episode.pack(pady=5)
            e_episode.pack()

            time = Label(window, text="Enter up to the time you've watched\nHint: enter the time by example: 00:00:00",
                         fg=fg_color, bg=bg_color, activebackground=fg_color, activeforeground=bg_color, font=font)
            e_time = Entry(window, fg=fg_color, bg=bg_color)
            time.pack(pady=5)
            e_time.pack()

            next2 = Button(window, text='Next', fg=fg_color, bg=bg_color, activebackground=fg_color,
                           activeforeground=bg_color, command=save)
            next2.pack(pady=7)
            next2.bind('<Enter>', func=lambda e: next2.config(bg=fg_color, fg=bg_color))
            next2.bind('<Leave>', func=lambda e: next2.config(bg=bg_color, fg=fg_color))

            Back2 = Button(window, text='Back', fg=fg_color, bg=bg_color, activebackground=fg_color,
                           activeforeground=bg_color, command=back2)
            Back2.place(x=0, y=260)
            Back2.bind('<Enter>', func=lambda e: Back2.config(bg=fg_color, fg=bg_color))
            Back2.bind('<Leave>', func=lambda e: Back2.config(bg=bg_color, fg=fg_color))

            if Len1 <= 1:
                showwarning("Hint",
                            "If you don't fill a form, default value will be saved\nDefault values:\nsession: 1\nepisode: 1\ntime: 00:00:00")

        label = Label(window, text="Enter your movie's name", fg=fg_color, bg=bg_color, activebackground=fg_color,
                      activeforeground=bg_color, font=font)
        label.pack()

        entry = Entry(window, fg=fg_color, bg=bg_color)
        entry.pack()
        entry.bind('<Enter>', func=lambda e: entry.config(bg=fg_color, fg=bg_color))
        entry.bind('<Leave>', func=lambda e: entry.config(bg=bg_color, fg=fg_color))

        next1 = Button(window, text='Next', fg=fg_color, bg=bg_color, activebackground=fg_color,
                       activeforeground=bg_color, command=values)
        next1.pack(pady=10)
        next1.bind('<Enter>', func=lambda e: next1.config(bg=fg_color, fg=bg_color))
        next1.bind('<Leave>', func=lambda e: next1.config(bg=bg_color, fg=fg_color))

        Back = Button(window, text='Back', fg=fg_color, bg=bg_color, activebackground=fg_color,
                      activeforeground=bg_color, command=back)
        Back.place(x=0, y=260)
        Back.bind('<Enter>', func=lambda e: Back.config(bg=fg_color, fg=bg_color))
        Back.bind('<Leave>', func=lambda e: Back.config(bg=bg_color, fg=fg_color))

    def movies():
        config.read(directory)
        menubar.destroy()
        b_add.destroy()
        b_list.destroy()
        text1.destroy()
        exit.destroy()
        exit.destroy()

        values = {}

        def back3():
            try:
                none.destroy()
                suggest.destroy()
            except:
                m_label.destroy()
                for section in config.sections():
                    button_name = f"section_{section}"
                    if button_name == "section_Settings":
                        continue
                    else:
                        section_buttons[button_name].destroy()
            Back3.destroy()
            main()

        def make_show(choice):

            def back4():
                name.destroy()
                for value in config[choice]:
                    values[value].destroy()
                b_1.destroy()
                b_2.destroy()
                Back4.destroy()
                movies()

            def update(movie: str):
                global Len2
                Len2 += 1
                name.destroy()
                for value in config[choice]:
                    values[value].destroy()
                b_1.destroy()
                b_2.destroy()
                Back4.destroy()

                def back5():
                    session.destroy()
                    e_session.destroy()
                    episode.destroy()
                    e_episode.destroy()
                    time.destroy()
                    e_time.destroy()
                    next2.destroy()
                    Back5.destroy()
                    make_show(movie)

                def save():
                    error = False
                    v_date_added = config.get(movie, 'date added')
                    v_session = e_session.get()
                    v_episode = e_episode.get()
                    v_time = e_time.get()
                    if v_session == '':
                        v_session = config[movie]['session']
                    else:
                        try:
                            int(v_session)
                        except:
                            showwarning('Alert', 'Just enter a number')
                            error = True
                            pass

                    if v_episode == '':
                        v_episode = config[movie]['episode']
                    else:
                        try:
                            int(v_episode)
                        except:
                            showwarning('Alert', 'Just enter a number')
                            error = True
                            pass

                    if v_time == '':
                        v_time = config[movie]['time']

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
                        update(movie)

                    else:
                        config[movie] = {'date added':v_date_added,'session': v_session, 'episode': v_episode, 'time': v_time}
                        auth = config.get('Settings', 'auth')
                        file = open(directory, 'w')
                        file.write(auth)
                        file.close()
                        with open(directory, 'a') as config_file:
                            config.write(config_file)
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
                        make_show(movie)

                session = Label(window, text="Enter up to the session you've watched", fg=fg_color, bg=bg_color,
                                activebackground=fg_color, activeforeground=bg_color, font=font)
                e_session = Entry(window, fg=fg_color, bg=bg_color)
                session.pack(pady=5)
                e_session.pack()
                e_session.bind('<Enter>', func=lambda e: e_session.config(bg=fg_color, fg=bg_color))
                e_session.bind('<Leave>', func=lambda e: e_session.config(bg=bg_color, fg=fg_color))

                episode = Label(window, text="Enter up to the episode you've watched", fg=fg_color, bg=bg_color,
                                activebackground=fg_color, activeforeground=bg_color, font=font)
                e_episode = Entry(window, fg=fg_color, bg=bg_color)
                episode.pack(pady=5)
                e_episode.pack()
                e_episode.bind('<Enter>', func=lambda e: e_episode.config(bg=fg_color, fg=bg_color))
                e_episode.bind('<Leave>', func=lambda e: e_episode.config(bg=bg_color, fg=fg_color))

                time = Label(window,
                             text="Enter up to the time you've watched\nHint: enter the time by example: 00:00:00",
                             fg=fg_color, bg=bg_color, activebackground=fg_color, activeforeground=bg_color, font=font)
                e_time = Entry(window, fg=fg_color, bg=bg_color)
                time.pack(pady=5)
                e_time.pack()
                e_time.bind('<Enter>', func=lambda e: e_time.config(bg=fg_color, fg=bg_color))
                e_time.bind('<Leave>', func=lambda e: e_time.config(bg=bg_color, fg=fg_color))

                next2 = Button(window, text='Next', fg=fg_color, bg=bg_color, activebackground=fg_color,
                               activeforeground=bg_color, command=save)
                next2.pack(pady=7)
                next2.bind('<Enter>', func=lambda e: next2.config(bg=fg_color, fg=bg_color))
                next2.bind('<Leave>', func=lambda e: next2.config(bg=bg_color, fg=fg_color))

                Back5 = Button(window, text='Back', fg=fg_color, bg=bg_color, activebackground=fg_color,
                               activeforeground=bg_color, command=back5)
                Back5.place(x=0, y=260)
                Back5.bind('<Enter>', func=lambda e: Back5.config(bg=fg_color, fg=bg_color))
                Back5.bind('<Leave>', func=lambda e: Back5.config(bg=bg_color, fg=fg_color))
                if Len2 <= 1:
                    showwarning("Hint",
                                f"If you don't fill a form, default value will be saved\nDefault values:\nsession: {config[movie]['session']}\nepisode: {config[movie]['episode']}\ntime: {config[movie]['time']}")

            def delete(movie: str):
                name.destroy()
                for value in config[choice]:
                    values[value].destroy()
                b_1.destroy()
                b_2.destroy()
                Back4.destroy()

                def yes():
                    config.remove_section(movie)
                    with open(directory, 'w') as config_file:
                        config.write(config_file)
                    showinfo('Deleted', f"{movie} deleted from your movie's list successfully")
                    ask.destroy()
                    yes.destroy()
                    no.destroy()
                    movies()

                def no():
                    ask.destroy()
                    yes.destroy()
                    no.destroy()
                    make_show(movie)

                ask = Label(window, text=f"Are you sure you wanna delete: \n{movie}\n From your movie's list",
                            fg=fg_color, bg=bg_color, activebackground=fg_color, activeforeground=bg_color, font=font)
                yes = Button(window, text="Yes, i'm sure", fg=fg_color, bg=bg_color, activebackground=fg_color,
                             activeforeground=bg_color, command=yes)
                no = Button(window, text="No, take me back", fg=fg_color, bg=bg_color, activebackground=fg_color,
                            activeforeground=bg_color, command=no)
                ask.pack()
                yes.pack(pady=(40, 0))
                no.pack()
                yes.bind('<Enter>', func=lambda e: yes.config(bg=fg_color, fg=bg_color))
                yes.bind('<Leave>', func=lambda e: yes.config(bg=bg_color, fg=fg_color))
                no.bind('<Enter>', func=lambda e: no.config(bg=fg_color, fg=bg_color))
                no.bind('<Leave>', func=lambda e: no.config(bg=bg_color, fg=fg_color))

            m_label.destroy()
            for section in config.sections():
                button_name = f"section_{section}"
                if button_name == "section_Settings":
                    continue
                else:
                    section_buttons[button_name].destroy()
            Back3.destroy()

            name = Label(window, text=choice, fg=fg_color, bg=bg_color, activebackground=fg_color,
                         activeforeground=bg_color, font=(font, 18))
            name.pack()
            for value in config[choice]:
                values[value] = Label(window, text=str(value) + ': ' + str(config[choice][value]), fg=fg_color,
                                      bg=bg_color, activebackground=fg_color, activeforeground=bg_color, font=font)
                if value == 'time added':
                    values[value].pack(anchor='center', pady=(5, 0))
                elif value == 'session':
                    values[value].pack(anchor='center', pady=(5, 0))
                else:
                    values[value].pack(anchor='center')

            Back4 = Button(window, text='Back', fg=fg_color, bg=bg_color, activebackground=fg_color,
                           activeforeground=bg_color, command=back4)
            Back4.place(x=0, y=260)
            Back4.bind('<Enter>', func=lambda e: Back4.config(bg=fg_color, fg=bg_color))
            Back4.bind('<Leave>', func=lambda e: Back4.config(bg=bg_color, fg=fg_color))

            b_1 = Button(window, text='Update information', fg=fg_color, bg=bg_color, activebackground=fg_color,
                         activeforeground=bg_color, command=lambda: update(choice))
            b_2 = Button(window, text='Delete this movie from list', fg=fg_color, bg=bg_color,
                         activebackground=fg_color, activeforeground=bg_color, command=lambda: delete(choice))
            b_1.pack(anchor='s', pady=(60, 0))
            b_2.pack(anchor='s')

            b_1.bind('<Enter>', func=lambda e: b_1.config(bg=fg_color, fg=bg_color))
            b_1.bind('<Leave>', func=lambda e: b_1.config(bg=bg_color, fg=fg_color))
            b_2.bind('<Enter>', func=lambda e: b_2.config(bg=fg_color, fg=bg_color))
            b_2.bind('<Leave>', func=lambda e: b_2.config(bg=bg_color, fg=fg_color))

        section_buttons = {}
        if config.sections() == ['Settings']:
            def suggest():
                none.destroy()
                suggest.destroy()
                Back3.destroy()
                add()

            none = Label(window, text="Looks like you haven't added any movies yet...", fg=fg_color, bg=bg_color,
                         activebackground=fg_color, activeforeground=bg_color, font=(font, 10))
            none.pack(pady=(100, 0))

            suggest = Button(window, text='Add a movie now!', fg=fg_color, bg=bg_color, activebackground=fg_color,
                             activeforeground=bg_color, command=suggest)
            suggest.pack(pady=(10, 0))

            suggest.bind('<Enter>', func=lambda e: suggest.config(bg=fg_color, fg=bg_color))
            suggest.bind('<Leave>', func=lambda e: suggest.config(bg=bg_color, fg=fg_color))

        else:
            m_label = Label(window, text='Your movies:', fg=fg_color, bg=bg_color, activebackground=fg_color,
                            activeforeground=bg_color, font=font)
            m_label.pack(anchor='nw', pady=(0, 10))

            for section in config.sections():
                button_name = f"section_{section}"
                if button_name == 'section_Settings':
                    continue
                else:
                    section_buttons[button_name] = Button(window, text=section, fg=fg_color, bg=bg_color,
                                                          activebackground=fg_color, activeforeground=bg_color,
                                                          font=font, command=lambda section=section: make_show(section))
                    section_buttons[button_name].pack(anchor='w')

        Back3 = Button(window, text='Back', fg=fg_color, bg=bg_color, activebackground=fg_color,
                       activeforeground=bg_color, command=back3)
        Back3.place(x=250, y=260)

        Back3.bind('<Enter>', func=lambda e: Back3.config(bg=fg_color, fg=bg_color))
        Back3.bind('<Leave>', func=lambda e: Back3.config(bg=bg_color, fg=fg_color))

    text1 = Label(window, text='Choose one:', fg=fg_color, bg=bg_color, activebackground=fg_color,
                  activeforeground=bg_color, font=font)
    text1.pack(pady=20)

    b_add = Button(window, text='New Movie', fg=fg_color, bg=bg_color, activebackground=fg_color,
                   activeforeground=bg_color, command=add)
    b_list = Button(window, text='Movie List', fg=fg_color, bg=bg_color, activebackground=fg_color,
                    activeforeground=bg_color, command=movies)
    b_add.place(x=72, y=100)
    b_list.place(x=142, y=100)

    b_add.bind('<Enter>', func=lambda e: b_add.config(bg=fg_color, fg=bg_color))
    b_add.bind('<Leave>', func=lambda e: b_add.config(bg=bg_color, fg=fg_color))
    b_list.bind('<Enter>', func=lambda e: b_list.config(bg=fg_color, fg=bg_color))
    b_list.bind('<Leave>', func=lambda e: b_list.config(bg=bg_color, fg=fg_color))

    def quit(event):
        window.destroy()

    exit = Button(window, text='Exit', fg=fg_color, bg=bg_color, activebackground=fg_color, activeforeground=bg_color)
    exit.place(x=0, y=260)

    exit.bind('<Enter>', func=lambda e: exit.config(bg=fg_color, fg=bg_color))
    exit.bind('<Leave>', func=lambda e: exit.config(bg=bg_color, fg=fg_color))

    exit.bind('<Double-1>', quit)
    exit.bind('<Enter>')


def backup_folder():
    b_dir = tkinter.filedialog.askdirectory(mustexist=True, title='Select a backup dir')
    if b_dir == '':
        showerror("Error", "You must select a directory")
        backup_folder()
    else:
        config['Settings'] = {'bg_color': config['Settings']['bg_color'], 'fg_color': config['Settings']['fg_color'],
                              'font': config['Settings']['font'], 'backup_dir': b_dir}
        with open(directory, 'w') as config_file:
            config.write(config_file)
        showinfo('Backup dir', 'Default backup dir saved successfully\nYou can change it anytime from menubar')
        global bg_color
        global fg_color
        global font
        bg_color = config['Settings']['bg_color']
        fg_color = config['Settings']['fg_color']
        font = config['Settings']['font']
        window.configure(bg=bg_color)
        return main()


def Setting():
    def recovery():
        yesno = askyesno("Question",
                         "Do you wanna recover your data?\n(only if you have a backup from database in database folder!)")
        if yesno is True:
            showinfo("Recovery",
                     f"You must select 'Movie.ini' file to recovery your data\n(Hint:go to that directory")
            file = tkinter.filedialog.askopenfilename(title="Select 'Movie.ini file'",
                                                      filetypes=[('Ini files', '*.ini')])

            if file == '':
                window.destroy()

            elif "Movie.ini" in file and '#Database of "My movies" app' in open(file, 'r').read():
                shutil.copyfile(file, directory)
                showinfo('copy', 'Datas recovered successfully')
                config.read('"G:/Alireza/Programing/#Files/PythonFiles/Movie.ini')
                config.read(directory)
                bg_color = config['Settings']['bg_color']
                fg_color = config['Settings']['fg_color']
                font = config['Settings']['font']
                window.configure(bg=bg_color)
                return Setting()
            else:
                showerror("info", 'This is not a "My movies" database file')
                yesno = askyesno("Question", "Do you wanna try again?")
                if yesno is True:
                    recovery()
                else:
                    window.destroy()
        else:
            showinfo("Recovery", f"This app will make another database automatically\nBut your data will be removed")
            f = open(directory, 'x')
            f.write(
                '#Database of "My movies" app\n[Settings]\nbg_color = snow\nfg_color = gainsboro\nfont = Arial\nbackup_dir = none')
            f.close()
            config.read(directory)
            bg_color = config['Settings']['bg_color']
            fg_color = config['Settings']['fg_color']
            font = config['Settings']['font']
            window.configure(bg=bg_color)
            return Setting()

    if os.path.exists(directory):
        global bg_color
        global fg_color
        global font
        config.read(directory)
        if '#Database of "My movies" app' in open(directory, 'r').read():
            if config['Settings']['backup_dir'] == 'none':
                showinfo('Backup dir',
                         'You must select a directory to app be able to make auto backup from your datas there')
                backup_folder()
            else:
                config.read(directory)
                bg_color = config['Settings']['bg_color']
                fg_color = config['Settings']['fg_color']
                font = config['Settings']['font']
                window.configure(bg=bg_color)
                return main()
        else:
            backuptext = open(directory, 'r').read()
            file = open(directory, 'w')
            file.write(f'#Database of "My movies" app\n{backuptext}')
            file.close()
            if config['Settings']['backup_dir'] == 'none':
                showinfo('Backup dir',
                         'You must select a directory to app be able to make auto backup from your datas there')
                backup_folder()
            else:
                config.read(directory)
                bg_color = config['Settings']['bg_color']
                fg_color = config['Settings']['fg_color']
                font = config['Settings']['font']
                window.configure(bg=bg_color)
                return main()

    else:
        showerror('Error', "Database file(Movie.ini) not found at 'G:/Alireza/Programing/#Files/PythonFiles'")
        recovery()

Setting()
window.mainloop()