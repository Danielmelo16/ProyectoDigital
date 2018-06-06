from difflib import SequenceMatcher

x=0
for n in range(0, 1880):
    with open('prueba.txt') as file_1,open('zop'+str(n)+'.txt') as file_2:
        file1_data = file_1.read()
        file2_data = file_2.read()
        similarity_ratio = SequenceMatcher(None,file1_data,file2_data).ratio()
        if x < similarity_ratio:
            x=similarity_ratio
        file_1.close()
        file_2.close()

print("")
print("")
print("")
print(str(x*100)+"% de plagio")
if (x*100 >  60):
    print ("Pongalo a perder")
if (x*100 < 35):
    print ("Esta bien")