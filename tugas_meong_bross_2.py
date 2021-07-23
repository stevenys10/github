banyak_perintah = int(input("Banyak perintah: "))
koordinat = [0,0]
koordinat_2 = [(0,0)] #2 dimension #challenge
command = ["U","S","T","B","HOME"]
for i in range(banyak_perintah):
    buffer = input("Masukkan perintah: ")
    if buffer in command:
        if buffer == "U":
            koordinat[1] +=1
            koordinat_2.append((koordinat_2[i][0],koordinat_2[i][1]+1))
        elif buffer == "S":
            koordinat[1] -=1
            koordinat_2.append((koordinat_2[i][0],koordinat_2[i][1]-1))
        elif buffer == "T":
            koordinat[0] +=1
            koordinat_2.append((koordinat_2[i][0]+1,koordinat_2[i][1]))
        elif buffer == "B":
            koordinat[0] -=1
            koordinat_2.append((koordinat_2[i][0]-1,koordinat_2[i][1]))
        else:
            break

print("Karakter Meong Brosss berada di koordinat ("+ str(koordinat[0])
            +","+str(koordinat[1])+")")
print("\nJalur yang ditempuh meong bross adalah", end = " ")
counter = 0
for i in range(len(koordinat_2)):
    print(koordinat_2[i], end = " ")
    if i == len(koordinat_2)-1:
        break
    print("-")
    counter+=1