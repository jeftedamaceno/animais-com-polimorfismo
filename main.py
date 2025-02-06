from cachorro import Cachorro
from cavalo import Cavalo

cachorro = Cachorro("Rex", "Labrador", 10)
cavalo = Cavalo('romenia','Mangalarga', 200)

print(cachorro.emitir_som())
print(cachorro)
cachorro.comer()
cachorro.correr()
print("peso atual", cachorro.mostra_peso())

print(cavalo.emitir_som())
print(cavalo)
cavalo.comer()
cavalo.correr()
print("peso atual", cavalo.mostra_peso())