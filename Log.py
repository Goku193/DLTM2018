import re
import sys
wartosci = []

print ("Podaj formule: ")
form = raw_input()
print ("Formula: " + str(form))


zmienne = re.findall('[a-z]', form)
zmien = sorted(list(set(zmienne)))
print ('Wykrylem ' + str(len(zmien)) + ' zmienne.')
print ('Sa to: ' + str(zmien) + '. Podaj kolejno wartosci (0,1) zatwierdzajac enterem.')

for p in zmien:
    wart = raw_input()
    if wart == '1':
        wartosci.append(1)
    if wart == '0':
        wartosci.append(0)
    print (p + ': ' + wart)
    form = form.replace(p, wart)

#form = form[::-1]

def parse_pn(form):

    operatorstack = []
    operandstack = []

    for token in form:
        if token == "A" or token == "K" or token == "E" or token == "C" or token == 'N':
            operatorstack.append(token)
            pending = False
        else:
            if pending is False:
                operand = token
                operandstack.append(operand)
            if pending is True:
                if len(operandstack)!= 0:
                    operand2 = token
                    operator = operatorstack.pop()
                    if operator == 'K' and (operand == '1' and operand2 == '1'):
                        result = '1'
                    elif operator == 'A' and (operand == '1' or operand2 == '1'):
                        result = '1'
                    elif operator == 'C' and not (operand == '1' and operand2 == '0'):
                        result = '1'
                    elif operator == 'E' and ((operand == '1' and operand2 == '1') or (operand == '0' and operand2 == '0')):
                        result = '1'
                    else:
                        result = '0'
                    operandstack.pop()
                    operandstack.append(result)
            pending = True
    if len(operatorstack) == 1 and len(operandstack) == 2:
      operand2 = operandstack.pop()
      operand = operandstack.pop()
      operator = operatorstack.pop()
      if operator == 'K' and (operand == '1' and operand2 == '1'):
        result = '1'
      elif operator == 'A' and (operand == '1' or operand2 == '1'):
        result = '1'
      elif operator == 'C' and not (operand == '1' and operand2 == '0'):
        result = '1'
      elif operator == 'E' and ((operand == '1' and operand2 == '1') or (operand == '0' and operand2 == '0')):
        result = '1'
      else:
        result = '0'
      operandstack.append(result)
    return operandstack.pop()

if __name__ == '__main__':

    expression = list(form)
    result = parse_pn(expression)
    if result == '1':
      print "Prawda"
    elif result == '0':
      print "Falsz"
