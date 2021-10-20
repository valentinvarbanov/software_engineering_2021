import random

github_accounts = [ 
    "Alexander1022",
    "AngelStoyanov33",
    "atanasatanasov03",
    "Vic-Dim",
    "Vicktoria853",
    "Vladikolev0321",
    "GerganaRoeva",
    "DeniBademi",
    "elizadamgova",
    "Ivan-Enchev",
    "Lilly7777",
    "mvvrachev",
    "marto55",
    "marti456",
    "Martincho2003",
    "VayerMaking",
    "petardmnv",
    "StelianRBG",
    "Teodor1331"
]



reviewer_1 = github_accounts.copy()
reviewer_2 = github_accounts.copy()

random.shuffle(reviewer_1)
random.shuffle(reviewer_2)

for index in range(len(github_accounts)):
    print(github_accounts[index] + " -> " + reviewer_1[index] + " " + reviewer_2[index])
