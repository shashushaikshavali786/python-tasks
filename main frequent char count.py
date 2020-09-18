value = input("please_enter_a_string: ")
count ={}
for x in value:
    if x in count.keys():
        count[x]+=1
    else:
        count[x]=1

print(count)
