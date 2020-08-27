def timeConverter(seconds):                        #Buat function timeConverter dengan parameter seconds
    
    if seconds > 359999 or seconds<0:              #Condition pertama dimana seconds tidak boleh lebih dari 359999 dan tidak boleh negatif
        return 'Invalid input!'                    #Apabila terpenuhi maka akan terminasi function dan masuk ke nilai return
    
    elif not type(seconds)==int:                   #Condition kedua dimana harus int
        return ('Invalid input!')
    
    else:                                          #Bila semua condition tidak terpenuhi maka masuk ke formula konversi
        HH         = seconds // 3600               #HH adalah variabel untuk mengubah detik jadi jam
        MM_temp    = seconds % 3600                #MM_temp adalah variabel untuk menyimpan sisa bagi pada HH
        MM         = MM_temp // 60                 #MM adalah variabel untuk mengubah sisa bagi pada HH menjadi menit
        SS         = MM_temp % 60                  #SS adalah variabel untuk mengubah sisa bagi pada HH menjadi detik
      
        return "%02d:%02d:%02d" % (HH, MM, SS)     #terminasi function dan mencetak hasil, di kasih %02d supaya digitnya ada 2 (HH:MM:SS)
      

seconds= 3665
print(timeConverter(seconds)) 