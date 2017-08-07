nomi= ['Anna' , 'Andrea' , 'Federico' , 'Gianna' , 'Daniel']

materie = ['Italiano' , 'Matematica' , 'Latino' , 'Scienze' , 'Fisica' , 'Inglese' , 'Storia' , 'Arte' , 'Sport']


for i in nomi:

	print(nomi.index(i)+1 ,i)

nome = int(input("scrivi il numero dello studente "  ))

if nome < 6 and nome > 0:
   
   nome = nome - 1
   
   print('hai scelto' , nomi[nome] )

   for e in materie:
      
      print(materie.index(e)+1, e)
   
   materia = int(input('scrivi il numero della materia ' ))
   
   if materia < 10 and materia > 0:
     
     materia = materia -1
     
     print('hai scelto' , materie[materia])

   elif materia>9:
    
    print('il numero è troppo grande riprovare')
  
   else:
    
    print('il numero è troppo piccolo riprovare')

elif nome>5:
   print('il numero è troppo grande, riprovare')

else:
   print('il numero è troppo basso, riprovare')