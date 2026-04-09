import os
os.system("cls" if os.name=="nt" else "clear")
os.system("git add .")
os.system('git commit -m "Automated Commit"')
os.system("git push")