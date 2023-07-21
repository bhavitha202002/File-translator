# Import tkinter and required libraries
import os
import tkinter as tk
from tkinter import ttk,messagebox,filedialog
from tkinter.filedialog import askopenfile

# Import google translator
import googletrans
from googletrans import Translator

# Getting  the languages
language=googletrans.LANGUAGES
all_languages=list(language.values())
lang1=language.keys()

'''************************************************************************************************************************************************************
****************************************************************TRANSLATE FUNCTION ************************************************************************
**************************************************************************************************************************************************************'''

# This is the translate function that translates the text from one language to the other and it also contain error handling mechanisms when the source,target languages,source text is not available

def translate():
    source_content=source_text.get(1.0,tk.END)
    t1=Translator()
    try:
        trans_text=t1.translate(source_content,src=sourcecombo.get(),dest=targetcombo.get())
        trans_text=trans_text.text
        
        target_text.delete(1.0,tk.END)
        target_text.insert(tk.END,trans_text)
    except Exception as e:
        if(str(e)=='invalid source language'):
            messagebox.showwarning("Warning","Please select source language")
        elif(str(e)=='invalid destination language'):
            messagebox.showwarning("Warning","Please select target language")
        elif(source_text.get(1.0,tk.END)=='\n'):
            messagebox.showwarning("Warning","Source File empty")
        else:
            print(str(e))
    return None
    

'''*************************************************************************************************************************************************************
******************************************************************UPLOAD FUNCTION******************************************************************************'
*************************************************************************************************************************************************************'''

# This function takes a file as input and also contain error handling mechanism if we try to upload the file again without removing the previous file

def upload():
    if(source_text.get(1.0,tk.END)=='\n'):
        file_path = filedialog.askopenfilename(initialdir='C:\\Users\\B.Bhavitha\\OneDrive\\Desktop',filetypes=[("Text Files",".txt"),("Word files",".docx"),("PDF files",".pdf"),("All files","*.*")])
        if(file_path):
            file_name=''
            for i in range(len(file_path)-1,0,-1):
                if(file_path[i]=="/"):
                   break
                else:
                    file_name+=file_path[i]
            file_name = file_name[::-1]
            if('.txt' in file_name):
                source_file_label.configure(text=file_name,fg='dark green')
                try:
                    with open(file_path,'r',encoding="utf-16") as file_obj:
                        if(os.stat(file_path).st_size==0):
                            restart()
                            messagebox.showwarning("warning","Source file empty,please upload again")
                        else:
                            file_content=file_obj.read()
                            source_text.insert(tk.END,file_content)
                            file_obj.close()
                except:
                    try:
                        with open(file_path,'r',encoding="utf-8") as file_obj:
                            if(os.stat(file_path).st_size==0):
                                restart()
                                messagebox.showwarning("warning","Source file empty,please upload again")
                            else:
                                file_content=file_obj.read()
                                source_text.insert(tk.END,file_content)
                                file_obj.close()
                    except:
                        with open(file_path,'r') as file_obj:
                            if(os.stat(file_path).st_size==0):
                                restart()
                                messagebox.showwarning("warning","Source file empty,please upload again")
                            else:
                                file_content=file_obj.read()
                                source_text.insert(tk.END,file_content)
                                file_obj.close()
            else:
                messagebox.showwarning("warning","ONLY TEXT FILES ALLOWED")
                restart()
        
    else:
        messagebox.showwarning("Warning","File already uploaded,please restart")
        
            
'''*************************************************************************************************************************************************************
***************************************************************** RESTART FUNCTION**************************************************************************
*************************************************************************************************************************************************************'''

# This function is used to restart the entire operation again

def restart():
    source_text.delete(1.0,tk.END)
    target_text.delete(1.0,tk.END)
    source_file_label.configure(text="File not uploaded",fg='red')
    file_path=''
    sourcecombo.set("SELECT LANGUAGE")
    targetcombo.set("SELECT LANGUAGE")

'''**************************************************************************************************************************************************************
******************************************************************DOWNLOAD FUNCTION************************************************************************
*************************************************************************************************************************************************************'''

# This function is used to download the target file in the desired language and also contain error handling mechanism when there is no target file and the source file is not translated 

def download():
    source_file_name=source_file_label["text"]
    if(source_file_name=='File not uploaded'):
        messagebox.showwarning("Warning","Please upload source file")
    else:
        if(targetcombo.get()=='SELECT LANGUAGE' and sourcecombo.get()=='SELECT LANGUAGE'):
            messagebox.showwarning("warning","please select source and target language to translate")
        elif(sourcecombo.get()=='SELECT LANGUAGE'):
            messagebox.showwarning("warning","Please select source language to translate")
        elif(targetcombo.get()=='SELECT LANGUAGE'):
            messagebox.showwarning("warning","Please select target language to translate")
        else:
            target_file_name='C:\\Users\\B.Bhavitha\\OneDrive\\Desktop\\'+targetcombo.get()+source_file_name
            if target_text.get("1.0", tk.END)!="\n":
                target_content=target_text.get(1.0,tk.END)
                with open(target_file_name,"wb") as writer:
                    corpus=target_content.encode(encoding="utf-8")
                    writer.write(corpus)
                    messagebox.showinfo("Message","Download completed")
            else:
                messagebox.showwarning("warning","Please translate source content")

'''*************************************************************************************************************************************************************
*******************************************************************DRIVER CODE******************************************************************************
**************************************************************************************************************************************************************'''
# creating a window
window = tk.Tk(className='FILE-TRANSLATOR')

# Maximize the window Size using state property
#window.state('zoomed')

#Maximize the window Size using attribute property


window.attributes('-fullscreen', True)

#setting window background color
#window['background']='#c27ba0' 
#window['background']='#d5a6bd'
window['background']='cyan'


head_label=tk.Label(text='FILE TRANSLATOR',fg="blue",bg="white",font=("TIMES",24),width=85,height=1)
head_label.place(x=0,y=2)
#head_label.pack()

# creating a close button
close_button = tk.Button(text="x",width=5,height=2,bg="#ff0000",fg="white",command=window.destroy)
close_button.place(x=1490,y=3)

# creating source language combo box
sourcecombo=ttk.Combobox(window,values=all_languages,font="gabriola",state="r")
sourcecombo.place(x=260,y=100)
sourcecombo.set("SELECT LANGUAGE")

# creating source file name label
source_file_label = tk.Label(window,text="File not uploaded",font="monaco",bg='peach puff',fg='red')
source_file_label.place(x=250,y=180)

#creating target language combo box
targetcombo=ttk.Combobox(window,values=all_languages,font="gabriola",state="r")
targetcombo.place(x=1120,y=100)
targetcombo.set("SELECT LANGUAGE")

# creating left frame
lframe=tk.Frame(window,bg="Black",bd=5)
lframe.place(x=135,y=238,width=440,height=400)

#creating right frame
rframe=tk.Frame(window,bg="Black",bd=5)
rframe.place(x=1000,y=238,width=440,height=400)

# creating the left textbox
source_text = tk.Text(lframe,font="Times",bg='white')
source_text.place(height=390,width=430)

# creating the right textbox
target_text = tk.Text(rframe,font="Times",bg='white')
target_text.place(height=390,width=430)

#creating scrollbar for left textbox
left_scrollbar=tk.Scrollbar(lframe)
left_scrollbar.pack(side="right",fill="y")

left_scrollbar.configure(command=source_text.yview)
source_text.configure(yscrollcommand=left_scrollbar.set)

#creating scrollbar for right textbox
right_scrollbar=tk.Scrollbar(rframe)
right_scrollbar.pack(side="right",fill="y")

right_scrollbar.configure(command=target_text.yview)
target_text.configure(yscrollcommand=right_scrollbar.set)

# creating the translate button
translate_button = tk.Button(text="TRANSLATE",font=("gabriola",20),width=14,bg='spring green',fg='black',command=translate)
translate_button.place(x=720,y=360)

# creating upload button
upload_button = tk.Button(window,text="UPLOAD",font="TIMES",width=12,bg='gold',fg='black',command=upload)
upload_button.place(x=275,y=700)

# creating restart button
restart_button = tk.Button(text="RESTART",font="TIMES",width=12,bg='blue',fg='white',command=restart)
restart_button.place(x=735,y=700)

# creating download button
download_button = tk.Button(text="\u2193DOWNLOAD",font="TIMES",bg='tomato',fg='black',command=download)
download_button.place(x=1160,y=700)
                            
# For event handling
window.mainloop()
