# python Injector

very simple python script that allows you to inject a file into someones computer to a specified path and run it

## How To Use


##Alot of this stuff is not specific enough, hard to understand, etc. ill make a youtbue vid later but for now this is all you get :)
 1. download the code from the green button. Or you can go to the release tab and download the zip folder. Install all the dependencies too (pip install -r r.txt in cwd)
 2. open up "main.py" in your text editor and replace DOWNLOAD_LINK to your download link. View the example below
 ![](images1exmaple1.png)
 1. If you are injecting a python file and want it to be ran, set this to True. Otherwise, leave it false
 2. look at line 22. here you will add the path you want the file injected to in quotations. Leave out the filename as that is are already covered and make sure to add an extra backslash to the path. you can also add user + to the beginning if you want to add C:\Users\username to the beginning of the path. Here is an example:
   
  ![2](images/example2.png)
  
  in this case, the full path will be C:\Users\usernameofpcuser\documents\nameoftheinjectedfile
  
  here is another example:
  
  ![3](images/example3.png)
  
  In this case, the full path will be C:\Program Files (x86)\Steam\nameoftheinjectedfile
  
  You can also add a full path in the quotations of this is too complicated

  6. if you want to compile the code into an executable, run "build.bat"; or, open up command prompt in the current directory and type: `pyinstaller --clean --onefile --noconsole -i NONE main.py`
  


 
