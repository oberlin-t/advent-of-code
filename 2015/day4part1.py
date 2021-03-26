import hashlib

inc = 0
zeros = 0

while zeros != 6:
    inc += 1;
    zeros = 0
    string = "yzbqklnj" + str(inc)
    result = hashlib.md5(string.encode())
    for i in range(6):
        if result.hexdigest()[i] == "0":
            zeros += 1
        if zeros == 6:
            print(inc)
            print(result.hexdigest())

        
