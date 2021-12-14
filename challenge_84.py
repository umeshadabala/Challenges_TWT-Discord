#Tech with tim challenge_84 submission
#Rules
#Enter the text with mixture of numbers and text
#Output will print without numbers
for i in range(int(input())):
  text = input()
  Output = ''.join(t if t not in map(str,range(0,9)) else "" for t in text)
  print(Output)




