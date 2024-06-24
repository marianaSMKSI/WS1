import random
import math
# Masukkan nombor
lower=int(input("Masukkan No terkecil :"))
# Masukkan nombor
upper=int(input("Masukkan No Terbesar:"))
x=random.randint(lower,upper)
print("\n\tAnda hanya",round(math.log(upper-lower+1,2)),"berpeluang memilih nombor !\n")
#Tetapan nombor pilihan
count=0
#Untuk Pengiraan nombor minimum

while count<math.log(upper - lower +1,2):
    count += 1
    guess=int(input("Sila Pilih Nombor :"))

if x == guess:
    print("TAHNIAH ANDA BERJAYA",count,"CUBA")
    
elif x>guess:
        print("ANDA MEMILIH NOMBOR KECIL!")
elif x<guess:
        print("ANDA MEMILIH NOMBOR BESAR!")
if count >=math.log(upper-lower+1,2):
        print("\nNOMBOR ADALAH %d"%x)
        print("\tCUBA LAGI!")
