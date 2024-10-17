lista= []
n=0
while True:
     n+=1
     filme = str(input(f"Diga o °{n} filme:"))
     lista.append(filme)

     if n==5:
          print("Os filmes escolhidos foram:")
          for i in enumerate(lista):
            print(f"{i}")
          break
        
