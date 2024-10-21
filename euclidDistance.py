#d = √(x₂-x₁)²+(y₂-y₁)² 
# Göreviniz:
#Python'da fonksiyonlar ve döngüler kavramlarını kullanarak, aşağıdaki işlemleri gerçekleştiren bir program yazmanız gerekmektedir:

#Noktaların Tanımlanması:
#‘points’ adında bir liste oluşturun. Bu liste, 2D uzaydaki noktaları temsil eden demetler (tuple) içermelidir. Örneğin, ‘(x, y)’ noktası bir demet ‘(x, y)’ olarak temsil edilecektir.
points = [(1, 2), (4, 6), (5, 7), (8, 9), (10, 10)]

#Öklid Mesafesi İçin Bir Fonksiyon Yazma:
#‘euclideanDistance’ adında bir fonksiyon tanımlayın. Bu fonksiyon, iki demet (her biri bir noktayı temsil eder) almalı ve bu iki nokta arasındaki Öklid mesafesini döndürmelidir.
#Not: Eğer daha zorlayıcı bir görevlendirme istiyorsanız herhangi bir kütüphane ve modül kullanmadan da yapabilrsiniz.
def euclideanDistance(p1,p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5
#Mesafelerin Hesaplanması:
#Bir döngü kullanarak, ‘points’ listesindeki her nokta çifti arasındaki Öklid mesafesini hesaplayın. Bu mesafeleri ‘distances’ adında başka bir listede saklayın.
distance = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance.append(euclideanDistance(p1= points[i],p2=points[j]))
#Minimum Mesafenin Bulunması:
minDistance = min(distance)
#‘distances’ listesinden minimum mesafeyi bulun ve yazdırın.
print("Minumum mesafeli noktalar arası mesafe",minDistance)
print("Noktalar arası Mesafeler",distance)


