# Imports
import requests, os, csv
from dotenv import load_dotenv
# -----------------------------------------------------------
# Reading Operation
fileName=input("Input Your CSV File,Please make Sure it's in the current director : ")
choosen=input("Enter Which roles You Want : CS or Ras or All : ")
choosen=choosen.strip().lower()
# --------------------------------------------------------------
# Code Initialization 
load_dotenv()
token = os.getenv('token')
# -------------------------------------------------
# Follow Code
def follow_me(peopleToFollow):
    print(peopleToFollow)
    headers = {'Authorization': 'token ' + token}
    requests.put(f'https://api.github.com/user/following/{peopleToFollow}',headers=headers)

# Main Code
with open(f'./{fileName}') as f:
    reader = csv.DictReader(f)
    roles = [line1['role'] for line1 in reader]

with open(f'./{fileName}') as f:
    reader = csv.DictReader(f)
    userName=[line2['GitHub link'] for line2 in reader]

numberOfRoles=len(roles)
numberOfUsers=len(userName)

if numberOfRoles!=numberOfUsers:
    print("Error: Must userName Numbers Equal Roles Numbers")
    quit()

for i in range(numberOfRoles):
    if roles[i]==choosen or choosen=="all":
        s=userName[i]
        x=s.find("github.com/")+len("github.com/")
        ans=""

        for  j in range(x,len(s)):
            if s[j]!="/":
                ans += s[j]
            else:
                break

        follow_me(ans)
        
    
# ---------------------------------------------------
# Final of Our Script 👌
# I Hope it Will Help you 😊