n = int(input("escriba un numero: "))
A = [ ]#donde almanesara los primos

for i1 in range(2,n): #el iterito empieza del 2 potqwuedesde ahi hay primos 
  primo = True # aca difinimos q si es primo sea true
  for i in range(2,i1): #verifica si esprimo desde 2 hasta "i1-1" 
        if i1 % i == 0:# si es divisible por algun numero
          #si te preguntas porque divide solo 1 vez si los primos tienen dos divisores pues 
          # solo son divisibles entre 1 y si mismo y para que eso no vamos a tomar en cuenta al (1) por eso empiexa de el 2 
          # y no tomaremos en cuenta el si mismo osea el numero mismo por eso hasta (n-1),asi solo toma en cuneta si se dividen no entra y si no dividen entran
          primo = False
          break   
  if primo:
         A.append(i1)
         
print(A)
print("emma clara lazo layme")
#ejemplo n = 12 en el for i1=(2) in range(2,n) dice de 2 hasta 12: pero solo lo hara hasta el 11
# guardara los valores de 2 hasta 11
#  for i in range(2,i1) dice -> de 2 hasta 11 
# entonces  2 % 12 == 0: 0 si false:12%3 ==0: si 
# 12 % 4: si false: 12 %5: no true : 12 % 6 :si false: 12 %7= no true : 12 % 8 no  TRUE 
# 12  % 9 no true 12 % 10: no true : 12 % 11 : no true  