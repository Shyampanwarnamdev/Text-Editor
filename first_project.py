import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os

########################################## main menu ############################################
# ---------------------------&&&&&&&&&&& End main menu &&&&&&&&&&&-------------------------------

main_application = tk.Tk()
main_menu = tk.Menu()

# file
new_icon = tk.PhotoImage(f='new.png')
open_icon = tk.PhotoImage(file='icon\\open.png')
save_icon = tk.PhotoImage(f='save.png')
saveas_icon = tk.PhotoImage(f='save.png')
exit_icon = tk.PhotoImage(f='exit.png')

file = tk.Menu(main_menu,tearoff=0)


# edit
copy_icon = tk.PhotoImage(f='copy.png')
paste_icon = tk.PhotoImage(f='paste.png')
cut_icon = tk.PhotoImage(f='cut.png')
clearall_icon = tk.PhotoImage(f='clearall.png')
find_icon = tk.PhotoImage(f='find.png')

edit = tk.Menu(main_menu,tearoff=0)

# view
toolbar_icon = tk.PhotoImage(f='toolbar.png')
statusbar_icon = tk.PhotoImage(f='statusbar.png')
view = tk.Menu(main_menu,tearoff=0)

# color theme
lightdefault_icon = tk.PhotoImage(f='lightdefault.png')
lightplus_icon = tk.PhotoImage(f='lightplus.png')
dark_icon = tk.PhotoImage(f='dark.png')
red_icon = tk.PhotoImage(f='red.png')
monokai_icon = tk.PhotoImage(f='monokai.png')
nightblue_icon = tk.PhotoImage(f='nightblue.png')

theme_choice = tk.StringVar()
color_icon = (lightdefault_icon,lightplus_icon,dark_icon,red_icon,monokai_icon,nightblue_icon)
color_dict = {
    'Light Default' : ('#000000','#ffffff'),
    'Light Plus' : ('#474747','#e0e0e0'),
    'Dark' : ('#c4c4c4','#2d2d2d'),
    'Red' : ('2d2d2d','#ffe8e8'),
    'Monokai' : ('#d3b774','#474747'),
    'Night Blue' : ('#ededed','#6b9dc2')
}
color_theme = tk.Menu(main_menu,tearoff=0)

main_menu.add_cascade(label = 'File',menu=file)
main_menu.add_cascade(label = 'Edit',menu=edit)
main_menu.add_cascade(label = 'View',menu=view)
main_menu.add_cascade(label = 'Color Theme',menu=color_theme)


########################################## toolbar ############################################


tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill = tk.X)

font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuple
font_box.current(0)
font_box.grid(row=0,column=0,padx=5)

size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar,width=10,textvariable=size_var,state='readonly')
font_size['values'] = tuple(range(8,80,2))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)

# # bold button
bold_icon = tk.PhotoImage(file="icon\\bold.png")
bold_button = ttk.Button(tool_bar,image=bold_icon)
bold_button.grid(row=0,column=2,padx=5)
# italic icon
italic_icon = tk.PhotoImage(file='icon\\italic.png')
italic_button = ttk.Button(tool_bar,image=italic_icon)
italic_button.grid(row=0,column=3,padx=5)
# underline icon
underline_icon = tk.PhotoImage(file='icon\\underline.png')
underline_button = ttk.Button(tool_bar,image=underline_icon)
underline_button.grid(row=0,column=4,padx=5)
# font icon
font_color_icon = tk.PhotoImage(f='icon\\open.png')
font_color_button = ttk.Button(tool_bar,image=font_color_icon)
font_color_button.grid(row=0,column=5,padx=5)
#allign left
align_left_icon=tk.PhotoImage(f='align_left.png')
align_left_button=ttk.Button(tool_bar,image=align_left_icon)
align_left_button.grid(row=0,column=6,padx=5)
#allign center
align_center_icon=tk.PhotoImage(f='align_center.png')
align_center_button=ttk.Button(tool_bar,image=align_center_icon)
align_center_button.grid(row=0,column=7,padx=5)
#allign right
align_right_icon=tk.PhotoImage(f='icon\\underline.png')
align_right_button=ttk.Button(tool_bar,image=align_right_icon)
align_right_button.grid(row=0,column=8,padx=5)

# ---------------------------&&&&&&&&&&& End tool bar &&&&&&&&&&&-------------------------------

########################################## text editor ############################################

text_editor = tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)
scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)



# font functionality

current_font_family = 'Ariel'
current_font_size = 14

def change_font(event=None):
    global current_font_family
    global current_font_size
    current_font_family = font_family.get()
    current_font_size = font_size.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind('<<ComboboxSelected>>',change_font)
font_size.bind('<<ComboboxSelected>>',change_font)

# bold button functionality
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if(text_property.actual()['weight']=='normal'):
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if(text_property.actual()['weight']=='bold'):
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

# italic button functionality
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if(text_property.actual()['slant']=='roman'):
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if(text_property.actual()['slant']=='italic'):
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))

# underline button functionality
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if(text_property.actual()['underline']==0):
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if(text_property.actual()['underline']==1):
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))


bold_button.configure(command=change_bold)
italic_button.configure(command=change_italic)
underline_button.configure(command=change_underline)

# font color fuctionality
def change_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_button.configure(command=change_color)

# allign left
def align_left():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')


# allign center
def align_center():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')


# allign center
def align_right():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')


align_left_button.configure(command=align_left)
align_center_button.configure(command=align_center)
align_right_button.configure(command=align_right)


# ---------------------------&&&&&&&&&&& End text editor &&&&&&&&&&&-------------------------------


########################################## status bar ############################################
status_bar = ttk.Label(main_application,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed=False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words = len(text_editor.get(1.0,'end-1c').split())
        characters = len(text_editor.get(1.0,'end-1c').replace(' ',' '))
        status_bar.config(text=f'characters : {characters} , words : {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',changed)
# ---------------------------&&&&&&&&&&& End status bar &&&&&&&&&&&-------------------------------



########################################## main menu functionality ############################################

# &&&&&&&& file function &&&&&&&&
# new functionality
url = ''
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0,tk.END)

file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N',command=new_file)

# open fuctionality
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title='Selectfile',filetypes=(('Text File','*.txt'),('All Files','*.*')))
    try:
        with open(url,'r') as rf:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,rf.read())
    except FileNotFoundError:
        return
    except :
        return 
    main_application.title(os.path.basename(url))

file.add_command(label='Open',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)

# Save functionality

def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as wf:
                wf.write(content)
            url.close()
        else:
            url = filedialog.asksaveasfile(mode = 'w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
            content2 = text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return 

file.add_command(label='Save',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+S',command = save_file)

# save as functionality
def saveas_file(event=None):
    global url
    try:
        content = text_editor.get(1.0,tk.END)
        url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
        url.write(content)
        url.close()
    except:
        return 

file.add_command(label='Save As',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+N',command= saveas_file)

# exit functionality
def exit_func(event=None):
    global url,text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('warning','Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as wf:
                        wf.write(content)
                        main_application.destroy()
                else:
                    content2 = text_editor.get(1.0,tk.END)
                    url = filedialog.asksaveasfile(mode='w',defaultextension='.text',filetypes=(('Text File','*.txt'),('All files','*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return 

file.add_command(label='Exit',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+Q',command=exit_func)
# &&&&&&&&&& edit commands &&&&&&&&&&&

#  copy , paste , cut and clear_all functionality
edit.add_command(label='Copy',image = copy_icon,compound = tk.LEFT,accelerator='Ctrl+C',command=lambda:text_editor.event_generate('<Control c>'))
edit.add_command(label='Paste',image = paste_icon,compound = tk.LEFT,accelerator = 'Ctrl + V',command=lambda:text_editor.event_generate('<Control v>'))
edit.add_command(label='Cut',image = cut_icon,compound = tk.LEFT,accelerator = 'Ctrl + X',command=lambda:text_editor.event_generate('<Control x>'))
edit.add_command(label='Clear_all',image = clearall_icon,compound = tk.LEFT,accelerator = 'Ctrl + Alt + X',command=lambda:text_editor.delete(1.0,tk.END))

# find functionality
def find(event=None):
    def find():
        word = find_entry.get()
        text_editor.tag_remove('match',1.0,tk.END)
        matches=0
        if word:
            start_pos = 1.0
            while True:
                start_pos = text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos} + {len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')
    
    def replace():
        word = find_entry.get()
        replace_text = replace_entry.get()
        content = text_editor.get(1.0,tk.END)
        new_content = content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

    # def replace():
    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+200+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)
    
    ## frame
    find_frame = ttk.LabelFrame(find_dialogue,text = 'Find/Replace')
    find_frame.pack(pady=20)

    ## labels
    find_label =ttk.Label(find_frame,text='Find : ')
    replace_label =ttk.Label(find_frame,text='Replace : ')

    find_label.grid(row=0,column=0,padx=4,pady=4)
    replace_label.grid(row=1,column=0,padx=4,pady=4)

    ## entry
    find_entry = ttk.Entry(find_frame,width=20)
    replace_entry = ttk.Entry(find_frame,width=20)

    find_entry.grid(row=0,column=1,padx=4,pady=4)
    replace_entry.grid(row=1,column=1,padx=4,pady=4)

    ## button
    find_button = ttk.Button(find_frame,text='Find',command=find)
    replace_button = ttk.Button(find_frame,text='Replace',command=replace)
    
    find_button.grid(row=2,column=0,padx=4,pady=4)
    replace_button.grid(row=2,column=1,padx=4,pady=4)

    find_dialogue.mainloop()


edit.add_command(label='Find',image = find_icon,compound = tk.LEFT,accelerator = 'Ctrl + F',command = find)

## view checkbuttons

show_toolbar=tk.BooleanVar()
show_toolbar.set(True)
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)
def hide_toolbar():
    print(show_toolbar.get())
    if show_toolbar.get():
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill = tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
    else:
        tool_bar.pack_forget()
        
def hide_statusbar():
    if show_statusbar.get():
        status_bar.pack(side=tk.BOTTOM)
    else:
        status_bar.pack_forget()

view.add_checkbutton(label='Tool Bar',image=toolbar_icon,variable=show_toolbar,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label='Status Bar',image=statusbar_icon,variable=show_statusbar,compound=tk.LEFT,command=hide_statusbar)

# color theme functionality
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color,bg_color = color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,foreground=fg_color)


count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icon[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)

main_application.config(menu=main_menu)

## bind shortcut keys
main_application.bind("<Control-n>",new_file)
main_application.bind("<Control-o>",open_file)
main_application.bind("<Control-s>",save_file)
main_application.bind("<Control-Alt-s>",saveas_file)
main_application.bind("<Control-q>",exit_func)
main_application.bind("<Control-f>",find)


main_application.mainloop()