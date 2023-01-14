import webbrowser
from os import system, name

def clear():
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')

while True:
  clear()

  print(""" 
    ______     __                __      _______           __         
   / ____/    / /_  ____  ____  / /__   / ____(_)___  ____/ /__  _____
  / __/______/ __ \/ __ \/ __ \/ //_/  / /_  / / __ \/ __  / _ \/ ___/
 / /__/_____/ /_/ / /_/ / /_/ / ,<    / __/ / / / / / /_/ /  __/ /    
/_____/    /_.___/\____/\____/_/|_|  /_/   /_/_/ /_/\__,_/\___/_/     
                                                                      
""")

  bookname=input("Book: ")

  filetype=input("File type(pdf or epub): ")
  
  filetype=filetype.lower()

  if filetype != "pdf":

    print("Wrong file type!")
    
    filetype=input("File type(pdf or epub): ")
    
    filetype=filetype.lower()
  
  elif filetype != "epub":
    
    print("Wrong file type!")
    
    filetype=input("File type(pdf or epub): ")
    
    filetype=filetype.lower()

  webbrowser.open("https://www.google.com/search?q="+bookname+" "+"filetype:"+filetype)





  





