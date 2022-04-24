import easygui
import tkinter

#Character Chart
full_name = input("Character's full name: ")
meaning_name= input("Reason or meaning of name: ")
nickname = input("Character’s nickname: ")
reason_nickname = input("Reason for nickname: ")
birth_date = input("Birth date: ")

#Physical appearance
age = (input("Age: "))
weight = input("Weight: ")
height = input("Height: ")
body_build = input("Body Build: ")
eye_color= input("Eye color: ")
skin_tone = input("Skin tone: ")
distinguishing_marks = input("Distinguishing marks: ")
hair_color = input("Hair color: ")
hairstyle = input("Hairstyle: ")
voice = input("Voice: ")
attractiveness = input("Overall attractiveness: ")
fav_outfit = input("Favorite outfit: ")


#Personality
good_personality = input("Good personality traits: ")
bad_personality = input("Bad personality traits: ")
default_mood = input("Mood character is most often in: ")
humor= input("Sense of humor: ")
greatest_joy = input("Character’s greatest joy in life: ")
greatest_fear = input("Character’s greatest fear in life: ")
why_fear = input("Cause of fear or trauma: ")
anger_when = input("Enraged when: ")
sad_when = input("Depressed or sad when: ")
priorities = input("Priorities: ")
life_philosophy = input("Life philosophy: ")
greatest_strength = input("Greatest strength: ")
greatest_weakness = input("Greatest weakness: ")
biggest_regret = input("Biggest regret: ")
biggest_accomplishment = input("Biggest accomplishment: ")
darkest_secret = input("Character’s darkest secret: ")

#Goals
motivation = input("Drives and motivations: ")
short_goals = input("Immediate goals: ")
long_goals = input("Long term goals: ")
goal_plan = input("How the character plans to accomplish these goals: ")

#Past
hometown = input("Hometown: ")
childhood = input("Type of childhood: ")
childhood_hero = input("Childhood hero: ")
education = input("Level of education: ")
hist_finance = input("Finances: ")

#Present
current_location = input("Current location: ")
current_occupation = input("Occupation: ")
current_finance = input("Finances: ")

#Family
mother = input("Mother: ")
mother_rship = input("Relationship with her: ")
father = input("Father: ")
father_rship = input("Relationship with him: ")
siblings = input("Siblings: ")
siblings_rship = input("Relationship with them: ")
spouse = input("Spouse: ")
spouse_rship = input("Relationship with him/her: ")
children = input("Children: ")
children_rship = input("Relationship with them: ")

#Favourites
fav_color = input("Favourite color: ")
hate_color = input("Least favourite color: ")
fav_music = input("Music: ")
fav_food = input("Food: ")
fav_lit = input("Literature: ")
fav_possession = input("Most prized possession: ")

#Habits
hobbies = input("Hobbies: ")
spending_habits = input("Spending habits: ")
smokes = input("Smokes: ")
drinks = input("Drinks: ")
drugs = input("Other drugs: ")
best_skill = input("Extremely skilled at: ")
worst_skill = input("Extremely unskilled at: ")
manners = input("Mannerisms: ")

#Traits
opti_pessi = input("Optimist or pessimist? ")
intro_extro = input("Introvert or extrovert? ")
risk_lvl = input("Daredevil or cautious? ")
logic_emo = input("Logical or emotional? ")
messy_neat = input("Disorderly and messy or methodical and neat? ")
confidence_lvl = input("Confident or unsure of himself/herself? ")

#Self-perception
self_thought = input("How he/she feels about himself/herself: ")
best_trait = input("What does the character consider his/her best personality trait? ")
worst_trait = input("What does the character consider his/her worst personality trait? ")
self_change = input("What would the character most like to change about himself/herself: ")

#Relationships with others
opinion_people = input("Opinion of other people in general: ")
enemy = input("Person character most hates: ")
best_friend = input("Best friend(s): ")
love_interest = input("Love interest(s): ")
mentor = input("Person character goes to for advice: ")
responsibility = input("Person character feels responsible for or takes care of: ")




easygui.msgbox(f"Character Chart \nCharacter’s full name: {full_name} \nReason or meaning of name: {meaning_name} \nCharacter’s nickname: {nickname} \nReason for nickname: {reason_nickname} \nBirth date: {birth_date} \
\n\nPhysical appearance \nAge: {age} \nWeight: {weight} \nHeight: {height} \nBody Build: {body_build} \nEye color: {eye_color} \nSkin tone: {skin_tone} \nDistinguishing marks: {distinguishing_marks} \nHair color: {hair_color} \nHairstyle: {hairstyle} \nVoice: {voice} \nOverall attractiveness: {attractiveness} \nFavorite outfit: {fav_outfit} \
\n\nPersonality \nGood personality traits: {good_personality} \nBad personality traits: {bad_personality} \nDefault character mood: {default_mood} \nSense of humor: {humor} \nCharacter’s greatest joy: {greatest_joy} \nCharacter’s greatest fear: {greatest_fear} \nCause of fear: {why_fear} \nEnraged when: {anger_when} \nSad when: {sad_when} \nPriorities: {priorities} \nLife philosophy: {life_philosophy} \nGreatest strength: {greatest_strength} \nGreatest weakness: {greatest_weakness} \nBiggest regret: {biggest_regret} \nBiggest accomplishment: {biggest_accomplishment} \nCharacter’s darkest secret: {darkest_secret} \
\n\nGoals \nMotivations: {motivation} \nImmediate goals: {short_goals} \nLong term goals: {long_goals} \nPlans to accomplish these goals: {goal_plan} \
\n\nPast \nHometown: {hometown} \nType of childhood: {childhood} \nChildhood hero: {childhood_hero} \nLevel of education: {education} \nFinances: {hist_finance} \
\n\nPresent \nCurrent location: {current_location} \nOccupation: {current_occupation} \nFinances: {current_finance} \
\n\nFamily \nMother: {mother} \nRelationship 'with' her: {mother_rship} \nFather: {father} \nRelationship 'with' him: {father_rship} \nSiblings: {siblings} \nRelationship 'with' them: {siblings_rship} \nSpouse: {spouse} \nRelationship 'with' him/her: {spouse_rship} \nChildren: {children} \nRelationship 'with' them: {children_rship} \
\n\nFavourites \nFavourite color: {fav_color} \nLeast favourite color: {hate_color} \nMusic: {fav_music} \nFood: {fav_food} \nLiterature: {fav_lit} \nMost prized possession: {fav_possession} \
\n\nHabits \nHobbies: {hobbies} \nSpending habits: {spending_habits} \nSmokes: {smokes} \nDrinks: {drinks} \nOther drugs: {drugs} \nExtremely skilled at: {best_skill} \nExtremely unskilled at: {worst_skill} \nMannerisms: {manners} \
\n\nTraits \nOptimist 'or' pessimist? {opti_pessi} \nIntrovert 'or' extrovert? {intro_extro} \nDaredevil 'or' cautious? {risk_lvl} \nLogical 'or' emotional? {logic_emo} \nDisorderly 'and' messy 'or' methodical 'and' neat? {messy_neat} \nConfident 'or' unsure of himself/herself? {confidence_lvl} \
\n\nSelf-perception \nHow he/she feels about himself/herself: {self_thought} \nWhat does the character consider his/her best personality trait? {best_trait} \nWhat does the character consider his/her worst personality trait? {worst_trait} \nWhat would the character most like to change about himself/herself: {self_change} \
\n\nRelationships 'with' others \nOpinion of other people 'in' general: {opinion_people} \nPerson character most hates: {enemy} \nBest friend(s): {best_friend} \nLove interest(s): {love_interest} \nPerson character goes to 'for' advice: {mentor} \nPerson character feels responsible 'for or' takes care of: {responsibility}", title="Character Sheet")