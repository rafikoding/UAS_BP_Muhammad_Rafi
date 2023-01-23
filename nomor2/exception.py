try:
    a = int(input('masukkan angka a '))
    b = int(input('masukkan angka b '))
    print('hasil a*b adalah',a*b)
except Exception as err:
    print(err)
