# fb-brute-force-attack

##### Based on my latest repo (**Facebook Automation**).   
##### Tested on linux only

#### simply, it read wordlist file that contains passwords you want to try and call the Facebook class from facebook module( my latest repo ) and try to log in with every password exists in the file. and if password is correct, it collect some information for you like name, email, id, correct password, and put them into the fb.json file.        

## To run it :     
#### 1)pip install selenium     
#### 2)install firefox geckodriver from (https://github.com/mozilla/geckodriver/releases) and move it into /bin folder.
#### 3)sudo chmod +x /bin/geckodriver
#### 4)python3 brute-fb.py

#### If you want see what happens, just remove **gui = "no"** in Facebook() from brute-fb.py script.   
