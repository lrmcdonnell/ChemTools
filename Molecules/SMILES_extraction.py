
#Extracting features from SMILES files


'''

Create output file

**Change Name Below**

'''




'''

Data from input file

**Change Name Below**

'''
input_file = 'Enamine_Diverse_smiles.txt'




#1. Hydroxamic Acids

def HA(file):
    output_file = open('HDAC2_Enamine_HydroxAcid.txt', 'w')
    #Hydroxamic acid SMILE motifs
    pattern = 'ONC(=O)'
    pattern2 = 'C(=O)NO'

    #open the input file, read the lines
    f = open(file, 'r')
    lines = f.readlines()

    #initialize counter for number of structures found
    num_structures = 0

    #for each line in the input file, ...
    for line in lines:
        #... check if each pattern is present within the line
        if pattern in line:
            #if pattern is present, write the line into the output file
            print("Pattern 1 found in line:", line.strip())
            output_file.write(line)
            #increment the counter for each structure that matches the pattern
            num_structures += 1

        #check other possible pattern
        if pattern2 in line:
            print("Pattern 2 found in line:", line.strip())
            output_file.write(line)
            num_structures +=1

    #Return the total number of structures found
    print(num_structures, 'hydroxamic acids found.')

    

        
#2. Carbonyl amine thing

def CarbAmThing(file):
    output_file = open('HDAC2_Enamine_CarbAmThing.txt', 'w')
    pattern = '2NC(=O)'
    pattern2 = '(=O)Nc2ccccc2N'
    pattern3 = '(=O)Nc2cc(ccc2N'
    f = open(file, 'r')

    lines = f.readlines()


    num_structures = 0

    for line in lines:
        #print(line)
        if pattern in line:
            print("Pattern 1 found in line:", line.strip())
            output_file.write(line)
            num_structures += 1
        if pattern2 in line:
            print("Pattern 2 found in line:", line.strip())
            output_file.write(line)
            num_structures +=1
        if pattern3 in line:
            print("Pattern 3 found in line:", line.strip())
            output_file.write(line)
            num_structures +=1

    print(num_structures, 'Carbonyl amine things found.')
    
#3. Amide Chain

def Amide(file):
    output_file = open('HDAC2_Enamine_AmideChain.txt', 'w')
    pattern = 'CC(=O)NCCC'
    pattern2 = 'CCCNC(=O)C'

    f = open(file, 'r')

    lines = f.readlines()

    num_structures = 0

    for line in lines:
        if pattern in line:
            print("Pattern 1 found in line:", line.strip())
            output_file.write(line)
            num_structures += 1
        if pattern2 in line:
            print("Pattern 2 found in line:", line.strip())
            output_file.write(line)
            num_structures +=1

    print(num_structures, 'Amide Chain things found.')

#4. Geminal Diol

def diol(file):
    output_file = open('HDAC2_Enamine_GemDiol.txt', 'w')
    pattern = 'C(O)(O)C'

    f = open(file, 'r')

    lines = f.readlines()

    num_structures = 0

    for line in lines:
        if pattern in line:
            print("Pattern 1 found in line:", line.strip())
            output_file.write(line)
            num_structures += 1

    print(num_structures, 'Geminal diols found.')
    
            
HA(input_file)
CarbAmThing(input_file)
Amide(input_file)
diol(input_file)
