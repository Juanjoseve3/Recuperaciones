# -*- coding: utf-8 -*-
"""Retos recuperación EDD.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zferEoeWLbtWnL0CjMkxwgSMOi6JOoKH
"""

#---------------------------------------------------------------------------#
#Excepción para manejar los posibles errores 
class Empty(Exception):
  def __init__(self, message):
    self.message = message

#---------------------------------------------------------------------------#
#Lista enlazada

class Nodo: 
  def __init__(self, valor, siguiente=None):
    self.valor = valor
    self.siguiente = siguiente
  
  def conseguir_valor(self):
    return self.valor

  def conseguir_siguiente(self):
    return self.siguiente
  
  def poner_siguiente(self, siguiente):
    self.siguiente = siguiente
  
class ListaEnlazada:
  def __init__(self, cabeza=None):
    self.cabeza = cabeza
    self.tamano = 0
    self.cola = None
    self.message = ""

  def poner_mensaje_excepcion(self, message):
    self.message = message

  def __len__(self):
    return self.tamano

  def conseguir_cola(self):
    try:
      if self.esta_vacia():
        raise Empty(self.message)
      else:
        return self.cola
    except Empty as e:
      print(e.message)

  def conseguir_cabeza(self):
    try:
      if self.esta_vacia():
        raise Empty(self.message)
      else:
        return self.cabeza
    except Empty as e:
      print(e.message)

  def poner_cabeza(self, e):
    e_node = Nodo(e)
    if(self.tamano == 0):
      self.cabeza = e_node 
      self.cola = e_node
    else:
      e_node.siguiente = self.cabeza
      self.cabeza = e_node
    self.tamano += 1 

  def agregar_cola(self, e):
    e_node = Nodo(e)
    if(self.tamano == 0):
      self.cabeza = e_node 
      self.cola = e_node
    else:
      self.cola.siguiente = e_node
      self.cola = e_node
    self.tamano += 1 

  def recorrer_lista(self):
    try:
      if(self.tamano == 0):
        raise Empty(self.message)
      else:
        nodo_actual = self.cabeza
        while(nodo_actual.conseguir_siguiente() is not None):
          print(nodo_actual.conseguir_valor(), end = ", ")
          nodo_actual = nodo_actual.conseguir_siguiente()
        print(nodo_actual.conseguir_valor())
    except Empty as e:
      print(e.message)

  def esta_vacia(self):
    return self.tamano == 0

  def eliminar_cabeza(self):
    try:
      if(self.esta_vacia()):
        raise Empty(self.message)
      else:
        del_el = self.cabeza
        self.cabeza = self.cabeza.conseguir_siguiente()
        self.tamano -= 1
        return del_el.conseguir_valor()
    except Empty as e:
      print(e.message)
    
  def eliminar_cola(self):
    try:
      if self.esta_vacia(): 
        raise Empty(self.message)
      elif(self.tamano == 1): 
        del_el = self.cabeza
        self.cabeza = None
        self.cola = None
        self.tamano -= 1
        return del_el.conseguir_valor()
      else:
        nodo_actual = self.cabeza
        while(nodo_actual.conseguir_siguiente().conseguir_siguiente() is not None):
          nodo_actual = nodo_actual.conseguir_siguiente()

        del_el = nodo_actual.conseguir_siguiente() 
        self.cola = nodo_actual 
        self.tamano -= 1 
        self.cola.poner_siguiente(None)
        
        return del_el.conseguir_valor()

    except Empty as e: 
      print(e.message)
#---------------------------------------------------------------------------#
#Pila con lista enlazada
class PilaEnlazada:
  def __init__(self):
    self.stack = ListaEnlazada() 
    self.stack.poner_mensaje_excepcion("Pila vacía")

  def push(self, e):
    self.stack.agregar_cola(e)
  
  def pop(self):
    return self.stack.eliminar_cola() 

  def imprimir_pila(self):
    self.stack.recorrer_lista()

  def conseguir_tamano(self):
    return len(self.stack)

  def esta_vacia(self):
    return len(self.stack) == 0 

  def conseguir_tope(self):
    top = self.stack.conseguir_cola()
    if(top):
      return top.conseguir_valor()


#---------------------------------------------------------------------------#
#Cola con lista enlazada
class ColaEnlazada:
  def __init__(self):
    self.queue = ListaEnlazada() 
    self.queue.poner_mensaje_excepcion("Cola vacía")

  def enqueue(self, e):
    self.queue.agregar_cola(e)
  
  def dequeue(self):
    return self.queue.eliminar_cabeza() 

  def imprimir_cola(self):
    self.queue.recorrer_lista()

  def conseguir_tamano(self):
    return len(self.queue)

  def esta_vacia(self):
    return len(self.queue) == 0 

  def conseguir_frente(self):
    frente = self.queue.conseguir_cabeza()
    if(frente):
      return frente.conseguir_valor()

print()
print("Lista Enlazada")
print()

ll = ListaEnlazada()
ll.poner_mensaje_excepcion("Lista enlazada vacía")
ll.poner_cabeza(5)
ll.recorrer_lista()
ll.poner_cabeza(6)
ll.recorrer_lista()
ll.poner_cabeza(7)
ll.recorrer_lista()
ll.agregar_cola(8)
ll.recorrer_lista()

print()
print("Pila con lista enlazada")
print()

s = PilaEnlazada()
s.conseguir_tope()
s.push(5)
s.push(6)
s.imprimir_pila()
print(f"eliminado: {s.pop()}")
s.imprimir_pila()
print("pop ", s.pop())
print("tamaño ", s.conseguir_tamano())
s.pop()
s.pop()
s.conseguir_tope()
s.push(10)
s.conseguir_tope()

print()
print("Cola con lista enlazada")
print()

q = ColaEnlazada()
q.conseguir_frente()
q.enqueue(5)
q.enqueue(6)
q.imprimir_cola()
print(f"eliminado: {q.dequeue()}")
q.imprimir_cola()
print("dequeue ", q.dequeue())
print("tamaño ", q.conseguir_tamano())
q.dequeue()
q.dequeue()
q.conseguir_frente()
q.enqueue(10)
q.conseguir_frente()