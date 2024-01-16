# Task 1
print('='*10,"Task1","="*10)

customer_id = ['B818', 'A461', 'A092', 'A082', 'B341', 'A005', 'A092', 'A461',
               'B219', 'B904', 'A901', 'A083', 'B904', 'A092', 'B341', 'B821',
               'B341', 'B821', 'B904', 'B818', 'A901', 'A083', 'B818', 'A082',
               'B219', 'B219', 'A083', 'A901', 'A082', 'B341', 'B341', 'A083',
               'A082', 'B219', 'B439', 'A461', 'A005', 'A901', 'B341', 'A082',
               'A083', 'A461', 'A083', 'A901', 'A461', 'A083', 'A082', 'A083',
               'B341', 'A901', 'A082', 'A461', 'B219', 'A083', 'B818', 'B821',
               'A092', 'B341', 'A461', 'A092', 'A083', 'B821', 'A092']


data_set_for_unique_customer_id = set(customer_id) #untuk mengelompokkan id customer di dalam data customer_id
print(data_set_for_unique_customer_id)

count_of_unique_customer_ids = len(data_set_for_unique_customer_id) #menghitung jumlah data unique customer id berdasarkan pengemlompokan
print(count_of_unique_customer_ids)

print("There are ", count_of_unique_customer_ids, "unique customer ids in the customer list")

# Task 2
print('='*10,"Task2","="*10)

Data = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print("A = ", Data[3])
print("B = ",Data[6:10])
print("C = ",Data[-1:-11:-1])

# Task 3
print('='*10,"Task3","="*10)

provinsi = {'Nanggroe Aceh Darussalam': 'Aceh',
            'Sumatera Selatan': 'Palembang',
            'Kalimantan Barat': 'Pontianak',
            'Jawa Timur': 'Madiun',
            'Sulawesi Selatan': 'Makassar',
            'Maluku': 'Ambon'}


list_provinsi = list(provinsi) #melakukan pengemlompokan berdasarkan nilai kunci
print("A = ", list_provinsi)

provinsi.update({'Jawa Timur' : 'Surabaya'}) # menggunakan update untuk melakukan perubahan pada pyhton list yang tersedia (mengganti ataupun menambahkan)
print("B = ", provinsi['Jawa Timur'])


