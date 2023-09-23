'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members
    
    This function should remove all rows from currentMem containing 'no' 
    in the 'Active' column and appends them to exMem.
    '''
def cleanFiles(currentMem, exMem):
    # TODO: Open the currentMem file as in r+ mode
    miembros=[]
    with open(currentMem,'r+') as data:
        #TODO: Open the exMem file in a+ mode
        with open(exMem,'a+') as ex:
            #TODO: Read each member in the currentMem (1 member per row) file into a list.
            # Hint: Recall that the first line in the file is the header.
            members=data.readlines()
            data.seek(0)
            for line in members:
                list=line.split()
                if (list[-1] == "no"):
                    ex.write(line)
                else:
                    members.write(line)
    
            current.seek(0)
            for line in miembros:
                current.write(line)
        
            current.truncate()                
    
    pass # Remove this line when done implementation


# The code below is to help you view the files.
# Do not modify this code for this exercise.
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
                
