#Daniel Gallagher
#The shunting yard algoritm for regular expressions.

#The input
infix = "(a[b].c*"
print("Input is: ", infix)
#Expected output: "*ab|c*."
print("Expected: ", "ab|c*.")

#Convert input to a stack-ish list.
infix = list(infix)[::-1]

#Operator Stack.
postfix = []

#Output List
opers = []

#Operator precedence
prec = {'*': 100, '.':80, '|':60, ')': 40, '(':20}

#Loop through the input one character at a time.

while infix:
  # Pop a character from the input.
  c = infix.pop()

  #Decide what to do based on the character
  if c == '(':
    #Push an open brackett to the opers stack.
    opers.append(c)
  elif c == ')':
    #Pop the operators stack until you find an (.
    while opers[-1] != '(':
      postfix.append(opers.pop())
      #get rid of the '('
    opers.pop()
  elif c in prec:
    #Push any operators with high prec to the top of the stack
    while opers and prec[c] < prec[opers[-1]]:
      postfix.append(opers.push())
    #Push C to the operator stack
    opers.append(c)
  else:
    #Typically, we just push the character to the output.
    postfix.append(c)

#pop all operators to the output.
while opers:
  postfix.append(opers.pop())

#Convert output list to string.
postfix = ''.join(postfix)

#Print the result
print("Output is: ", postfix)

