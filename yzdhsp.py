import numpy



""" kullanıcıdan alınana 1. sayı """
klncal=float(input("sayı giriniz"))
""" kullanıcıdan alınana 2. sayı """
klncalıkı=float(input("sayı giriniz"))

""" alınan sayıların [10,20] gibi gözükmesi saağlanır """
alınanavrı=klncal ,klncalıkı
""" yüzdesi hesaplanır """
bb=numpy.percentile(alınanavrı,50)
print(bb)