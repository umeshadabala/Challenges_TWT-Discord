#Challenge
#Tech with tim challenge_84 submission
#Rules
#Enter the text with mixture of numbers and text
#Output will print without numbers
#Story:
#In addition to Boe Jiden having difficulty going up stairs, he also has difficulty writing on the keyboard. He keeps accidently typing numbers when there is no need for them.
#Task: You are given a number T and T testcases follow, for each testcase remove any numbers embedded into words, and print the resulting sentence.

for i in range(int(input())):
  text = input()
  Output = ''.join(t if t not in map(str,range(0,10)) else "" for t in text)
  print(Output)
#Input
3
h8i how ar5e y0ou
i9m go0od thanks
ok by7e
#Output
hi how are you
im good thanks
ok bye
#Task completed
