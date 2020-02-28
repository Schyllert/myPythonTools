# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

  


root = Tk()
root.withdraw()

finalFileName = ""
finalFileExtension = ".png"
while True:
    
    folder_selected = filedialog.askdirectory(title = 'Select folder that contains files to be renamed')
    tkz = folder_selected + "/"
    selected = False
    #Is this the correct folder? If not reselect folder OR quit
    answer = messagebox.askyesnocancel("Warning!! - press cancel if unsure", "Is this the correct selected folder? " + tkz)
    if (answer == True):
        selected = True
        break
    if (answer == None):
        break
    
# Function to rename multiple files 
def reName(): 
    i = 0
        
    for filename in os.listdir(tkz): 
        dst = finalFileName + str(i) + finalFileExtension
        src = tkz + filename 
        dst = tkz + dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
        
# Driver Code 
if __name__ == '__main__': 
      

    # Will continue to ask for inputs for file name/extension and if user accepts his/her input will continue to run reName()
    if (selected == True):
        
        while True:
            USER_INP_NAME = simpledialog.askstring(title="File name selection", prompt="Select file name: ")
            USER_INP_EXTENSION = simpledialog.askstring(title="File extension selection", prompt="Select file extension .jpg~: ")
            checkInputName = messagebox.askyesno("", "Is this the correct file name? " + USER_INP_NAME)
            checkInputExtension = messagebox.askyesno("", "Is this the correct file extension? " + USER_INP_EXTENSION)
            
            if ((checkInputName == True) and (checkInputExtension == True)):
                finalFileName = USER_INP_NAME
                finalFileExtension = USER_INP_EXTENSION
                reName()
                break
    else:
        messagebox.showinfo("Info", "No files were changed") 
        
 
