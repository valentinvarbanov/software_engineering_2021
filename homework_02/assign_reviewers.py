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

should_shuffle = True
while should_shuffle:
    random.shuffle(reviewer_1)
    random.shuffle(reviewer_2)

    should_shuffle = False

    # reshuffle again if there are duplicates within one line
    for index in range(len(reviewer_1)):

        reviewers = [github_accounts[index], reviewer_1[index], reviewer_2[index]]
        
        if len(set(reviewers)) != len(reviewers):
            # duplicate
            should_shuffle = True
            break

for index in range(len(github_accounts)):
    print("| " + github_accounts[index] + " | " + reviewer_1[index] + " | " + reviewer_2[index] + " |")
