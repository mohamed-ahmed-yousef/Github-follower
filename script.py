# Imports
import requests, csv
from tqdm import tqdm

# -----------------------------------------------------------
# Reading Operation
token=input("here https://github.com/settings/tokens -> generate new token and allow user:follow then PASTE TOKEN here: ")
fileName=input("Input Your CSV File,Please make Sure it's in the current director : ")
choosen=input("Enter Which roles You Want : CS or Ras or All : ")
choosen=choosen.strip().lower()
# -------------------------------------------------
# Follow Code
def follow_me(peopleToFollow):
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

followed = {}
count = 0

for i in tqdm(range(numberOfRoles)):
    
    if roles[i].lower()==choosen or choosen=="all":
    
        s=userName[i]
        x=s.find("github.com/")+len("github.com/")
        ans=""
        
        for  j in range(x,len(s)):
            if s[j]!="/":
                ans += s[j]
            else:
                break
        
        if followed.get(ans) is None:
            follow_me(ans)
            followed[ans] = True
            count +=1
        
        
print(f'{count} People has been followed! 🥳')
# ---------------------------------------------------
# Final of Our Script 👌
# I Hope it Will Help you 😊