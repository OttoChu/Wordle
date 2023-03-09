f= open('tes.txt', 'r')
file = f.read()
# print(file)
file = file.splitlines()
# print(file)
# for each in file:
#     print (each)

for each in file:
    p = open('accepted.txt', 'a')
    each = each.upper()+'\n'
    print(each)
    p.write(each)
    p.close()