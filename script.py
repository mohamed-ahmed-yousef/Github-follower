# Imports
import requests, csv,os
from tqdm import tqdm

# -----------------------------------------------------------
# Reading Operation
token=input("\nhere https://github.com/settings/tokens -> generate new token\n and allow user:follow then PASTE TOKEN here: ")
print("\nPlease Make a sure that CSV file and Script.js file in the Same Folder 😄 ")
fileName=input("Input Your CSV File : ")

# File Path Handling
currentRunningPyFile = __file__
toRemoveFromPath = os.path.basename(__file__)
lenghtOfRunningFile = len(toRemoveFromPath)
lengthOfCompletePath = len(currentRunningPyFile)
currentRunningPyFile = currentRunningPyFile[:lengthOfCompletePath-lenghtOfRunningFile]
fileName = currentRunningPyFile+fileName

# -------------------------------------------------
# Follow Code
def follow_me(peopleToFollow):
    headers = {'Authorization': 'token ' + token}
    requests.put(f'https://api.github.com/user/following/{peopleToFollow}',headers=headers)

# unFollow Code
def not_follow_me(peopleToFollow):
    headers = {'Authorization': 'token ' + token}
    requests.delete(
        f'https://api.github.com/user/following/{peopleToFollow}', headers=headers)

# Read Code
try:
    with open(f'{fileName}') as f:
        reader = csv.DictReader(f)
        roles = [line1['role'] for line1 in reader]

    with open(f'{fileName}') as f:
        reader = csv.DictReader(f)
        userName = [line2['GitHub link'] for line2 in reader]
except:
    print("\n AGAIN,Please Make CSV File and Script.py File in The Same Folder and Enter Only a CORRECT File Name 😊 \n")
    quit()

numberOfRoles=len(roles)
numberOfUsers=len(userName)

if numberOfRoles!=numberOfUsers:
    print("Error: Must userName Numbers Equal Roles Numbers")
    quit()

# Roles
choosen=input("Enter Which ones You Want to follow or not follow : CS or Ras or All : ").strip().lower()
followOrNot = input("Enter What You Want to Do :\"follow\" or \"unfollow\" : ").strip().lower()


followed = {}
count = 0

if followOrNot == "follow":
    for i in tqdm(range(numberOfRoles)):
        if roles[i].lower() == choosen or choosen == "all":
            s = userName[i]
            x = s.find("github.com/")+len("github.com/")
            ans = ""

            for j in range(x, len(s)):
                if s[j] != "/":
                    ans += s[j]
                else:
                    break

            if followed.get(ans) is None:
                follow_me(ans)
                followed[ans] = True
                count +=1

elif followOrNot == "unfollow":
    for i in tqdm(range(numberOfRoles)):
        if roles[i].lower() == choosen or choosen == "all":
            s = userName[i]
            x = s.find("github.com/")+len("github.com/")
            ans = ""

            for j in range(x, len(s)):
                if s[j] != "/":
                    ans += s[j]
                else:
                    break
            

            if followed.get(ans) is None:
                not_follow_me(ans)
                followed[ans] = True
                count +=1
else:
    print("Please : Enter A Correct Action \"follow\" or \"unfollow\"")

        
        
print(f'{count} People has been {followOrNot}ed 🥳')
# ---------------------------------------------------
# Final of Our Script 👌
# I Hope it Will Help you 😊