print (" 🔁 INVERS A LIST 🔁 ")
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


for i in range (len(first)-1, -1, -1 ) :
    second.append ( first[i] )

print (" Your entered list is : ", first )
print (" The inversed list is :", second)