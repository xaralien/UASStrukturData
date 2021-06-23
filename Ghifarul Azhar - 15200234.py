# ghifarul azhar #
# 15200234 #

print("//=========================================================")
print("//                 Data Pembeli Baju                       ")
print("//=========================================================")
def queue():
    s = []
    return s
def enqueue (s,i):
    s.insert(0,i)
    return s
def dequeue (s):
    return s.pop()
def rear(s):
    return(s[0])
def front (s):
    return(s[len(s)-1])
def size (s):
    return len(s)
def IsEmpety(s):
    return s == []

def Ke2():
    s = queue()
    k = ''
    while True:
        banyak = int(input("Masukan Banyak Pembeli secara keseluruhan = "))
        for j in range(banyak):
            orang = input("Masukan Nama Pembeli ke %i yang masuk di antrian = " %(j+1))
            enqueue(s,orang)
        s.reverse()
        print("Data Nama Seluruh Pembeli Adalah : %s"%(s))
        s.reverse()
        o = input("Masukan Nama Pembeli yang dicari = ")
        ditemukan = "t"
        itung = 0
        while ditemukan=='t':
            if o == front(s):
                print("Congrats Pembeli Sudah Ditemukan")
                ditemukan = 'y'
                print("Pembeli berada pada antrian yang ke-",str(itung-1+2),"Dari Data Nama Seluruh Pembeli")
                print("Dengan Looping",str(itung-1+1),"Kali")
            elif o != front(s):
                masukan = dequeue(s)
                enqueue(s,Masukan)
                ditemukan = 't'
                s.reverse()
                print("Looping %i = %s "%(itung+1),s)
                s.reverse()
            itung+=1
            if itung > len(s):
                print("Maaf Nama yang Dimaksud Tidak Ada")
                print()
                print("Silahkan tambahkan nama jika ingin memesan dengan ketik (yes/no) dibawah ini ")
                ditemukan = "y"
        k = input("Apakah Masih ada yang dibantu? --Ketik (yes/no)-- ?")
        if k != 'yes':
            print("||=======================================================||")
            print("||==========================Thanks You===================||")
            print("||==================Data Pembeli Baju ===================||")
            print("||==================Ghifarul Azhar ======================||")
            print("||=======================================================||")
            break
        else:
            print("Ketik Nama yang ingin memesan ")


Ke2()



