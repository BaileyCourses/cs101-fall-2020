from cs101audio import *

from random import randrange

def main():

    sound = Audio()
    sound.open_audio_file("america_the_beautiful.wav")
    sound = sound[:20000]
    
    for i in range(0, len(sound), 1000):
        sound[i:i+250].play()
        print(i)
    
#     values = []
#     for _ in range(10000000):
#         values.append(randrange(1000))
#         
#     sum = 0
#     for value in values:
#         sum = sum + value
#     
#     print(sum / len(values))

#     college = "Hamilton"
#     lcollege = list(college)
#     
#     target = "H"
#     replacement = "C"
#     
#     loc = college.find(target)
#     
#     lcollege[loc] = replacement
#     
#     college = ""
#     for letter in lcollege[::-1]:
#         college = college + letter

#    college = ""
#    for i in range(len(lcollege)):
#        college = college + lcollege[i]
            
#     print(college)
#     print(lcollege)
#     print(type(college))
#     print(type(lcollege))
#     college = "My Hamilton"
#     lcollege = list(college)
#     
#     target = "H"
#     replacement = "C"
#     
#     loc = college.find(target)
#     
#     lcollege[loc] = replacement
#     college = college[:loc] + replacement + college[loc + 1:]
#     print(college)
#     print(lcollege)
    
if __name__ == "__main__":
    main()



























# sound = Audio()
# 
# sound.open_audio_file("america_the_beautiful.wav")
# sound[:3000].play()

#chunks = 100
#for i in range(0, len(sound), len(sound)//chunks):
#    print("Playing ", i)
#0    sound[i:i + len(sound) // chunks].play()
# 
#     strings = []
#     for i in range(10):
#         string = "I'm the string at index: " + str(i)
#         strings.append(string)
# 
#     strings = []
#     for i in range(25):
#         string = "At: " + str(i)
#         strings.append(string)
#     
#     print(strings)
#     
#     for i in range(len(strings)):
#         print(strings[i])
# 
#     for i in range(0, len(strings), 8):
#         print(strings[i])
# 
# #    for s in strings:
# #        print(s)
# 
#     return
# 
#     # Creating a large list of randomize numbers:
#     
#     values = []
#     
#     for _ in range(10000000):
#         value = randrange(100)
#         values.append(value)
#         
#         
#     # Accumulate the sum of the values:
# 
#     sum = 0
#     
#     for i in range(len(values)):
#         sum = sum + values[i]
#     
#     print("The sum of the values is:", sum)
#     print("The average of the values is:", sum / len(values))

    
