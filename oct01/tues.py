#from matplotlib import pyplot as plt

def start():
    values = inputMany("Enter a number: ")
    print(values)
#    if yes("Do you want to continue? "):
#        print("Continuing...")
#    else:
#        print("Aborting!")    

def inputMany(prompt):
    result = []
    answer = input(prompt)
    while answer != "":
        result.append(answer)
        answer = input(prompt)
    
    return result       

def yes(prompt):
    answer = input(prompt)
    
    #while answer != "yes" and answer != "no":
    while not (answer.lower() == "yes" or answer.lower() == "no"):
        print('Please answer "yes" or "no"')
        answer = input(prompt)    
    
    # The answer must be yes, or no

    if answer == "yes":
        return True
    else:
        return False
     
if __name__ == "__main__":
    start()