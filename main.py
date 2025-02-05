from cachorro import Cachorro
from cavalo import Cavalo

cachorro = Cachorro("Rex", "Labrador")
cavalo = Cavalo('romenia','Mangalarga')

print(cachorro.emitir_som())
print(cachorro)
cachorro.correr()

print(cavalo.emitir_som())
print(cavalo)
cavalo.correr()