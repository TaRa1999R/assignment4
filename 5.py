print (" 🚫 REMOVE REPEATED SENTENCES FROM A LIST 🚫 ")
print (" Enter 'done' to see the result ")
print (" Enter numbers as input ")

first = []
second = []

while True :
    vurudi = input (" Please enter the input : ")

    if vurudi == "done" :
        break

    else :
        vurudi = int ( vurudi )
        first.append ( vurudi )

for sentence in first :
    if sentence not in second :
        second.append ( sentence )

print (" Your entered list is : ", first )
print (" New list is :", second)