for x in range(5):
    print ("iteration no {} in for loop".format(x))
else:
    print ("else block in loop")
print ("Out of loop")



# Here else wont print beacuse loop dint completed successfully
for x in range(5):
   if(x==3):
       break
else:
    print ("else block in loop")
print ("Out of loop")