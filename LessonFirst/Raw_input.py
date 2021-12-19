from past.builtins import raw_input

name = raw_input("What is your name?")
age = raw_input("How old are you?")

print ("Your name is:", name)
print ("You are " + age + " years old.")

after_ten = int(age) + 10
print ("You will be " + str(after_ten) + " years old after ten years.")