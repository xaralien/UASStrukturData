import os
 
# Membuat class untuk List
class Node(object):
 
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
   
    # Mengambil data dari List
    def get_data(self):
        return self.data
   
    # Mengambil data berikutnya
    def get_next(self):
        return self.next_node
   
    # Menentukan data berikutnya
    def set_next(self, new_next):
        self.next_node = new_next
       
# Membuat class untuk Linked List
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
   
    # Menambah data baru
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
 
    # Menghitung panjang Linked List
    def size(self):
        current = self.head
        count = 0
        # Perulangan untuk menghitung data
        while current:
            count += 1
            current = current.get_next()
        return count
 
    # Mencari sebuah data pada list
    def search(self, data):
        current = self.head
        found = False
        # Perulangan mencari data yang dicari
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
               
        return found
 
    # Menghapus node
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Barang tidak ada")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
 
    # Menampilkan isi dari list
    def showData(self):
        os.system('cls')
        print ("Barang yang Terdaftar:")
        print ("Barang Terakhir -> Barang Pertama")
        current_node = self.head
        while current_node is not None:
            print ("     ->"),
            print (current_node.data),
            current_node.next_node.data if hasattr(current_node.next_node, "data") else None
           
            current_node = current_node.next_node
 
    # Main menu aplikasi
    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            os.system("cls")
            print("===============================")
            print("|  Menu aplikasi Gudang  |")
            print("===============================")
            print("1. Daftar Barang")
            print("2. Masukan Barang")
            print("3. Hapus Barang")
            print("4. Cari Barang")
            print("5. Total Barang di Gudang")
            print("6. Keluar")
            print("===============================")
            pilihan=str(input(("Silakan masukan pilihan anda: ")))
            if(pilihan=="1"):
                os.system("cls")
                self.showData()
                x = input("")
            elif(pilihan=="2"):
                os.system("cls")
                obj = str(input("Masukan Nama Barang yang ingin anda tambahkan: "))
                self.insert(obj)
            elif(pilihan=="3"):
                os.system("cls")
                obj = str(input("Masukan Nama Barang yang ingin anda dihapus: "))
                self.delete(obj)
                x = input("")
            elif(pilihan=="4"):
                os.system("cls")
                obj = str(input("Masukan Nama Barang yang ingin anda dicari: "))
                status = self.search(obj)
                if status == True:
                    print("Data ditemukan pada list")
                else:                  
                    print("Data tidak ditemukan")
                x = input("")
            elif(pilihan=="5"):
                os.system("cls")
                print("Jumlah Barang di Gudang adalah: "+str(self.size()))
                x = input("")
            elif(pilihan=="6"):
                break
            else:
                pilih="n"
 
if __name__ == "__main__":
    # execute only if run as a script
    l = LinkedList()
    l.mainmenu()