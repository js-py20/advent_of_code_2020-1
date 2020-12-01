#puzzle input data stored as "input_1.txt"
# import input data
data_txt = open("input_1.txt", "r")
data_list = []
for line in data_txt:
    stripped_line = line.strip()
    data_list.append(stripped_line)
data_txt.close()
data = [ int(x) for x in data_list ]
#print(data)
#print(len(data)) = 200 numbers


#Part a
def part_a():
    a=0
    while a<= 199:
        i=a+1
        while i<=199:
            x = data[a]+data[i]
            if x == 2020:
                print("position a = " + str(a)+ ", position i = "+str(i))
                print(data[a])
                print(data[i])
                print("a+i =" + str(data[a]+data[i]))
                result = data[a]*data[i]
                print("a*i =  " + str(result))
                break
            else:
                None
            i+=1
        a+=1

part_a()           

#Part b
def part_b(): 
    z=0
    while z<=199:
        a=z+1
        while a<= 199:
            i=a+1
            while i<=199:
                x = data[z]+data[a]+data[i]
                if x == 2020:
                    print("position z = "+str(z)+", position a = "+str(a)+ ",  position b = "+str(i))
                    result = data[z]*data[a]*data[i]
                    print(data[z])
                    print(data[a])
                    print(data[i])
                    print("z+a+i =" + str(data[z]+data[a]+data[i]))
                    print("z*a*i = "+str(result))
                    break
                else:
                    None
                i+=1
            a+=1
        z+=1
part_b()
