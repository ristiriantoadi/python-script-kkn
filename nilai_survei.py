import pandas as pd  
df = pd.read_csv("Test Case KKN Malaka 3.csv",";")

emptydf = pd.DataFrame(columns=['Nama Lengkap Responden','Dusun','RT','Pernikahan',
                                                  'Umur','Jumlah Anggota Keluarga'])
dfHampirMiskin = emptydf
dfMiskin = emptydf
dfSangatMiskin = emptydf
dfMampu = emptydf

for i in range(df.shape[0]):
    row = df.iloc[i]
    # print(row)
    countKriteriaMiskin=0
    for j in list(df):
        # print(row[j])
        # if(j.lower() == 'Pendidikan Terakhir'.lower()):
        #     if(str(row[j]).lower() == 'Tidak Sekolah'.lower() or str(row[j]).lower() == 'Tidak Tamat SD/Tamat SD'.lower()):
        #         countKriteriaMiskin+=1
        # elif(j.lower() == 'luas bangunan (8m2/ orang)'.lower()):
        #     if(str(row[j]).lower() == 'kurang'.lower()):
        #         countKriteriaMiskin+=1
        # elif(j.lower() == 'dinding rumah'.lower()):
        #     if(str(row[j]).lower() == 'kayu kualitas rendah/bambu'.lower()
        #     or str(row[j]).lower() == 'dinding kondisi buruk (retak)'.lower()
        #     or str(row[j]).lower() == 'dinding tidak terplester'.lower()):
        #         countKriteriaMiskin+=1
        # elif(j.lower() == 'lantai'.lower()):
        #     if(str(row[j]).lower() == 'tanah'.lower() or str(row[j]).lower() == 'kayu'.lower()):
        #         countKriteriaMiskin+=1
        # elif(j.lower() == 'peneragan'.lower()):
        #     if(str(row[j]).lower() != 'listrik'.lower()):
        #         countKriteriaMiskin+=1
        # elif(j.lower() == 'sumber air bersih'.lower()):
        #     if(str(row[j]).lower() != 'pdam'.lower()):
        #         countKriteriaMiskin+=1
        # elif(j.lower() == 'fasilitas mck'.lower()):
        #     if(str(row[j]).lower() != 'didalam rumah'.lower()):
        #         countKriteriaMiskin+=1
        # elif(j.lower() == 'rutinitas makan'.lower()):
        #     if(str(row[j]).lower() != '3x sehari'.lower()):
        #         countKriteriaMiskin+=1
        # elif(j.lower() == 'konsumsi daging/telur/susu'.lower()):
        #     if(str(row[j]).lower() == '1x seminggu'.lower() or str(row[j]).lower() == 'tidak pernah'.lower()):
        #         countKriteriaMiskin+=1
        # elif(j.lower() == 'bahan bakar memasak'.lower()):
        #     if(str(row[j]).lower() != 'gas lpg'.lower()):
        #         countKriteriaMiskin+=1
        # elif(j.lower() == 'pembelian pakaian baru dalam 1 tahun'.lower()):
        #     if(str(row[j]).lower() == '1x setahun'.lower()):
        #         countKriteriaMiskin+=1
        # elif(j.lower() == 'biaya kesehatan'.lower()):
        #     if(str(row[j]).lower() == 'kartu bpjs (subsidi)'.lower()
        #     or str(row[j]).lower() == 'kis'.lower()
        #     or str(row[j]).lower() == 'tidak mampu bayar'.lower()):
        #         countKriteriaMiskin+=1
        # elif(j.lower() == 'penghasilan/bulan (utama)'.lower()):
        #     if(str(row[j]).lower() == 'Rp. 1.000 - Rp. 500.000'.lower()):
        #         countKriteriaMiskin+=1
        if(j.lower() == 'pendidikan terakhir'.lower()):#1
            if(str(row[j]).lower() == "Tidak Sekolah".lower() or str(row[j]).lower() == "Tidak Tamat SD/Tamat SD".lower()):
#                 print("tidak mampu")
                countKriteriaMiskin+=1
        elif(j.lower() == 'Luas bangunan (8m2/ orang)'.lower()):#2
            if(str(row[j]).lower() == 'Kurang'.lower()):
                countKriteriaMiskin+=1
        elif(j.lower()== 'Lantai'.lower()):#3
            if(str(row[j]).lower() == 'Tanah'.lower() or str(row[j]).lower() == 'kayu'.lower()):
                countKriteriaMiskin+=1
        elif(j.lower() == 'Dinding Rumah'.lower()):#4
            if(str(row[j]).lower() == 'kayu kualitas rendah/bambu'.lower() 
               or str(row[j]).lower() == 'dinding kondisi buruk (retak)'.lower()
              or str(row[j]).lower() == 'dinding tidak terplester'.lower()):
                countKriteriaMiskin+=1
        elif(j.lower() == 'fasilitas mck'.lower()):#5
            if(str(row[j]).lower() != 'didalam rumah'.lower()):
                countKriteriaMiskin+=1
        elif(j.lower() == 'peneragan'.lower()):#6
            if(str(row[j]).lower() != 'listrik'.lower()):
                countKriteriaMiskin+=1
        elif(j.lower() == 'sumber air bersih'.lower()):#7
            if(str(row[j]).lower() != 'PDAM'.lower()):
                countKriteriaMiskin+=1
        elif(j.lower() == 'bahan bakar memasak'.lower()):#8
            if(str(row[j]).lower() != 'gas lpg'.lower()):
                countKriteriaMiskin+=1
        elif(j.lower() == 'konsumsi daging/telur/susu'.lower()):#9
            if(str(row[j]).lower() == '1x seminggu'.lower() or str(row[j]).lower() == 'tidak pernah'.lower()):
                countKriteriaMiskin+=1
        elif(j.lower() == 'pembelian pakaian baru dalam 1 tahun'.lower()):#10
            if(str(row[j]).lower() == '1x setahun'):
                countKriteriaMiskin+=1
        elif(j.lower() == 'rutinitas makan'.lower()):#11
            if(str(row[j]).lower() == '1x sehari' or str(row[j]).lower() == '2x sehari'.lower()):
                countKriteriaMiskin+=1
        elif(j.lower() == 'biaya kesehatan'.lower()):#12
            if(str(row[j]).lower() == 'tidak mampu bayar'.lower()
              or str(row[j].lower() == 'kartu BPJS (subsidi)'.lower()
                    or str(row[j].lower() == 'kis'.lower()))):
                countKriteriaMiskin+=1
        elif(j.lower() == 'Penghasilan/bulan (Utama)'.lower()):#13
#             print(df[j][i])
            if(str(row[j]).lower() == 'Rp. 1.000 - Rp. 500.000'.lower()):
                countKriteriaMiskin+=1
        
    countKepemilikanBarang=0
    if(str(row['Kepemilikan barang pribadi/Tabungan lebih dari 500.000']).lower() == '1.0'):
        countKepemilikanBarang+=1
    if(str(row['Kepemilikan barang pribadi/Sepeda motor']).lower() == '1.0'):
        countKepemilikanBarang+=1
    if(str(row['Kepemilikan barang pribadi/Hewan ternak (Sapi/Kambing/Unggas)']).lower() == '1.0'):
        countKepemilikanBarang+=1
    if(str(row['Kepemilikan barang pribadi/Emas']).lower() == '1.0'):
        countKepemilikanBarang+=1

    if(countKepemilikanBarang<=1):
        countKriteriaMiskin+=1    
        
    print("Nama: ",row['Nama Lengkap Responden'])
    # print("Kepemilikan barang: ",countKepemilikanBarang)
    print("Kriteria Miskin: ",countKriteriaMiskin)
    if(countKriteriaMiskin<9 and countKriteriaMiskin>=6):
#         print("Hampir Miskin")
#         print(row[['Nama Lengkap Responden','Dusun','RT']])
        dfHampirMiskin= dfHampirMiskin.append(row[['Nama Lengkap Responden','Dusun','RT','Pernikahan',
                                                  'Umur','Jumlah Anggota Keluarga']])
        print("Kategori: Hampir miskin")
#         print(dfHampirMiskin)
    elif(countKriteriaMiskin<11 and countKriteriaMiskin>=9):
#         print("miskin")
        dfMiskin = dfMiskin.append(row[['Nama Lengkap Responden','Dusun','RT','Pernikahan',
                                                  'Umur','Jumlah Anggota Keluarga']])
        print("Kategori: Miskin")
    elif(countKriteriaMiskin>=12 and countKriteriaMiskin<14):
#         print("Sangat Miskin")
        dfSangatMiskin = dfSangatMiskin.append(row[['Nama Lengkap Responden','Dusun','RT','Pernikahan',
                                                  'Umur','Jumlah Anggota Keluarga']])
        print("Kategori: Sangat miskin")
    else:
        dfMampu = dfMampu.append(row[['Nama Lengkap Responden','Dusun','RT','Pernikahan',
                                                  'Umur','Jumlah Anggota Keluarga']])
        print("Kategori: Mampu")

dfHampirMiskin.to_csv('data hampir miskin.csv')
dfMiskin.to_csv('data miskin.csv')
dfSangatMiskin.to_csv('data sangat miskin.csv')
dfMampu.to_csv('data mampu.csv')
