
# Lists are ordered , change able , allows duplicates
marks = [92,50,60,35]
mixed =[5,"Taha",3.142,False]

# printing the list elements

print(marks[2]) #60
print(marks[-1]) # 35
print(marks[1:3])# [50 , 35]

# Modifying the list

marks.append(200) # add to end
marks.insert(0,500) # insert at index
print(marks[0])# now at index 0 it can print 500 because we update it by append
marks.remove(35) # remove by value
marks.pop() # remove  last
marks.pop(0) # remove by index


# useful

print(len(marks))  # length
print(sorted(marks))  # sorting
print(sum(marks))        # sum
print(max(marks))        # max value
marks.reverse()          # reverse in place
