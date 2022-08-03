import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill_name=len(names) #to get the length of the string
random_choice = random.randint(0, bill_name-1) #
person_who_will_pay = names[random_choice] #chaging the random number generated back to string
print(person_who_will_pay + " is going to buy the meal today!")
