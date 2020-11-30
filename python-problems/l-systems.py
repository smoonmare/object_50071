rules = {}

rules['A'] = 'A[B]'
rules['B'] = 'B[C]'
rules['C'] = 'C[A]'
axiom = 'AB'


def applyRule(input):
    output = ""
    for rule, result in rules.items():  # applying the rule by checking the current char against it
        if (input == rule):
            output = result 
            break
        else:
            output = input  # else ( no rule set ) output = the current char -> no rule was applied
    return output


def processString(oldStr):
    newstr = ""
    for character in oldStr:
        newstr = newstr + applyRule(character)  # build the new string
    return newstr


def createSystem(numIters, axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):  # iterate with appling the rules
        endString = processString(startString)
        startString = endString
        print("N="+str(i+2)+" " + endString)
    return endString

print("N=1 AB")
createSystem(3, axiom)