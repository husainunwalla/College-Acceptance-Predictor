personalityDict = {
  "ISTJ" : "Inspector",
  "ISTP" : "Crafter",
  "ISFJ" : "Protector",
  "ISFP" : "Artist",
  "INFJ" : "Advocate",
  "INFP" : "Mediator",
  "INTJ" : "Architect",
  "INTP" : "Thinker",
  "ESTP" : "Persuader",
  "ESTJ" : "Director",
  "ESFP" : "Performer",
  "ESFJ" : "Caregiver",
  "ENFP" : "Champion",
  "ENFJ" : "Giver",
  "ENTP" : "Debater",
  "ENTJ" : "Commander"
}

def find_personality(answers):
    countOfA: int = 0
    countOfB: int = 0
    personalityType: str = ''
    count = 0
    for answer in answers:
            if answer == 'A':
                countOfA = countOfA + 1
            if answer == 'B':
                countOfB = countOfB + 1
            count = count + 1 
            
            if count == 5:
                print('a:',countOfA, ' b:', countOfB)
                if countOfA > countOfB:
                    personalityType = personalityType + 'E'
                else:
                    personalityType = personalityType + 'I'
                countOfA = 0
                countOfB = 0
            elif count == 10:
                print('a:',countOfA, ' b:', countOfB)
                if countOfA > countOfB:
                    personalityType = personalityType + 'S'
                else:
                    personalityType = personalityType + 'N'
                countOfA = 0
                countOfB = 0
            elif count == 15:
                print('a:',countOfA, ' b:', countOfB)
                if countOfA > countOfB:
                    personalityType = personalityType + 'T'
                else:
                    personalityType = personalityType + 'F'
                countOfA = 0
                countOfB = 0
            elif count == 20:
                print('a:',countOfA, ' b:', countOfB)
                if countOfA > countOfB:
                    personalityType = personalityType + 'J'
                else:
                    personalityType = personalityType + 'P'

    if personalityType in personalityDict :
        return personalityDict[personalityType]
    
    return "All questions not answered properly"
