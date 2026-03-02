#Create a list
#Prompt the user to enter five foods, and store the responses in the list
#Display the list on one line, each item seperated by commas
#Calculate how many characters were entered and display this to the user
#Hint: Using the len() function will be useful here
#Below is a sample of what your output might look like. You do not have to follow the text exactly.
#
#Enter a food: pizza
#Enter a food: beef jerkey
#Enter a food: rice triangles
#Enter a food: steamed chinese bun
#Enter a food: fried chicken
#
#Your entered foods are:
#pizza, beef jerkey, rice triangles, steamed chinese bun, fried chicken 
#You entered a total of 62 characters

foodList = []
for i in range(5):
    foodList.append(str(input(f"Enter a food: {i+1}:")))

print("Your entered foods are: "  + str(foodList ))
charLength = 0
charLength = sum(len(food) for food in foodList)


print(f"You entered a total of {charLength} characters")