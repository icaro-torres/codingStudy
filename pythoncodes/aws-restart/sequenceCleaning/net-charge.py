# Python3.6
# Coding: utf-8
# Store human prepoinsulin in a variable called preproinsulin

preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Strore the remaining sequence elements of human insulin in variables:

lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  

# The functional insulin is a combination of the B and A chains, so we can concatenate them:

insulin = bInsulin + aInsulin

# Dictionary of pKa values for the amino acids in human insulin:

pKR = {'y': 10.07, 'c': 8.18, 'k': 10.53, 'h': 6.00, 'r': 12.48, 'd': 3.65, 'e': 4.25}

# Count the number of each amino acid in the functional insulin sequence:

seqCount = {x: float(insulin.count(x)) for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']}

# Calculate the net charge of the functional insulin sequence:

pH = 0

while (pH <= 14):
    netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values()))
    )

    # Print the pH and net charge, formatted to two decimal places
    print('{0:.2f}'.format(pH), netCharge)
    pH += 1