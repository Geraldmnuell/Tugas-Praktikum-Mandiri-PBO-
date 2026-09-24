"""
Pertama kita membuat CLass Employee terlebih dahulu sebagai identitas data karyawan
"""
class Employee:
    def __init__(self, nama, jabatan, gaji):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji

# Ini merupakan Class utama untuk melakukan proses instruksi tugas
class Company:
    def __init__(self):
        self.__employees = [] # Enkapsulasi untuk array data karyawan

    def inputData_karyawan(self, employee):
        if isinstance(employee, Employee): # Fungsi untuk memvalidasi input objek sebelum di masukkan ke dalam list
            self.__employees.append(employee)
            print("Data karyawan berhasil di tambahkan")
        else:
            print("Objek bukan employee")
            
    # Membuat private method (only called in class)
    def __calculate_payroll(self):
        total = 0

        for employee in self.__employees:
            total += employee.gaji

        return total

    def tampilkanKaryawan(self):
        print("<----- DATA KARYAWAN ----->")

        for employee in self.__employees:
            print("Nama     : ", employee.nama)
            print("Jabatan  : ", employee.jabatan)
            print("Gaji     : ", employee.gaji)
            print("-----------------------")

    def tampilkanTotal_gaji(self):
        total = self.__calculate_payroll()
        print(f"Total gaji karyawan : {total}\n")

employee1 = Employee("Gerald", "Full stack", 7000000)
employee2 = Employee("Budi", "Web Dev", 6000000)
employee3 = Employee("Siti", "UI/UX", 8000000)

company = Company()
company.inputData_karyawan(employee1)
company.inputData_karyawan(employee2)
company.inputData_karyawan(employee3)

company.tampilkanKaryawan()
company.tampilkanTotal_gaji()
