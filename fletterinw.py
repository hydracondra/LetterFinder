destletter=input("Enter the writing that you want to find a letter")
fletter=input("Enter the letter you would like to find")
cfletter=input("Enter the capital version of the letter")
toplam=0
toplam2=0
for lf in destletter:
    if lf==fletter:
        toplam=toplam+1
for lf in destletter:
    if lf==cfletter:
        toplam2=toplam2+1
ltoplam=toplam2+toplam
print("There is",ltoplam,cfletter,"('s)in this writing")

        
