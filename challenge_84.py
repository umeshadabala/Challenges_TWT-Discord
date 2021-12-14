#Tech with tim challenge_84 submission
#Rules
#Enter the text with mixture of numbers and text
#Output will print without numbers
Text = input("Enter the text with mixture of numbers and text:  ") 
Output = ''.join(c if c not in map(str,range(0,10)) else "" for c in Text)
print(Output)
