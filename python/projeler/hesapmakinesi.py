num1=int(input('1. sayıyı giriniz  ')) #buradaki int komutu tam sayı girilmesini sağlar
num2=int(input('2. sayıyı giriniz  '))#buradaki input değeri kullnıcıdan değer alır
op=input('işlemi seçiniz(+,-,*,/)  ')
if op=='*': #buradaki yazılan koşullar uygunsa altındaki kodu çalıştırır.
    print(num1, '*', num2,'=', num1*num2)
elif op=='+': #elif komutu değilse eğer anlamı katar.yani else if yazmak yerine komut yazmayı hızlandırır.
 print(num1, '+', num2,'=', num1+num2)
elif op == '-':
 print(num1, '-', num2, '=', num1-num2)
elif op=='/':
 print(num1,'/',num2,'=', num1/num2)
