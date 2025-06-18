from functools import reduce

#uses of MAP
number = [1,2,3]
duplicados = map(lambda x: x*2, number)
print(list(duplicados))

a  = [1,2,3]
b = [10,20,30]

suma_doble = map(lambda x , y : x + y, a, b)
print(list(suma_doble))

def capitalizar(s):
    return s.capitalize()
nombres = ['juan', 'jose', 'martin']
print(list(map(capitalizar, nombres)))

#uses of FILTER
nums = [1,2,3,4,5,6,7,8,9,10]
pares = filter(lambda x: x%2 == 0, nums)
print(list(pares))

strings = ['hola', '', 'adios' , '', 'si']
no_vacios = filter(bool, strings)
print(list(no_vacios))

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
personas = [Persona('Ana', 20), Persona('Juan', 17), Persona('Martin', 16)]
adultos = filter(lambda p: p.edad >= 18, personas)
print([p.nombre for p in adultos])


#uses for REDUCE
nums = [1, 2, 3, 4]
total = reduce(lambda acc, x: acc + x, nums)
print(total)

producto = reduce(lambda acc, x: acc * x, nums, 1)
print(producto)

pares1 = [('a', 1), ('b', 2), ('c',3)]
dic = reduce(lambda acc, kv: {**acc, kv[0]: kv[1]}, pares1, {})
print(dic)
