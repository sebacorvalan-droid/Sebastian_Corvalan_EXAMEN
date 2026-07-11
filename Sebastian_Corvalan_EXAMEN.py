productos_iniciales = {

  'M001': ['Alimento Premium', 'comida', 'DogPlus', 10.0, True, False],

  'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8.0, False, False],

  'M003': ['Snack Dental', 'snack', 'BiteJoy', 1.0, True, True],

  'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],

  'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],

  'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2.0, False, False]

}



stock_inicial = {

  'M001': [32990, 12],

  'M002': [9990, 0],

  'M003': [5490, 25],

  'M004': [7990, 5],

  'M005': [11990, 7],

  'M006': [24990, 3]

}



def leer_opcion():

  try:

    opcion = int(input("Ingrese opción: "))

    if 1 <= opcion <= 6:

      return opcion

    print("Debe seleccionar una opción válida") 

    return None

  except ValueError:

    print("Debe seleccionar una opción válida") 

    return None





def buscar_codigo(codigo, dicc_productos):

  return codigo.strip().upper() in dicc_productos



def unidades_categoria(categoria, dicc_productos, dicc_stock):

  total_unidades = 0

  categoria_buscar = categoria.strip().lower()

  

  for cod, datos in dicc_productos.items():

    if datos[1].lower() == categoria_buscar:

      if cod in dicc_stock:

        total_unidades += dicc_stock[cod][1]

        

  print(f"El total de unidades disponibles es: {total_unidades}") 



def busqueda_precio(p_min, p_max, dicc_productos, dicc_stock):

  resultados = []

  

  for cod, datos_stock in dicc_stock.items():

    precio = datos_stock[0]

    unidades = datos_stock[1]

    

    if p_min <= precio <= p_max and unidades > 0: 

      if cod in dicc_productos:

        nombre = dicc_productos[cod][0]

        resultados.append(f"{nombre}--{cod}") 

        

  if resultados:

    resultados.sort()

    print(f"Los productos encontrados son: {resultados}") 

  else:

    print("No hay productos en ese rango de precios.") 



def actualizar_precio(codigo, nuevo_precio, dicc_productos, dicc_stock):

  cod_upper = codigo.strip().upper()

  if buscar_codigo(cod_upper, dicc_productos):

    dicc_stock[cod_upper][0] = nuevo_precio 

    return True

  return False





def validar_codigo(codigo, dicc_productos):

  cod_limpio = codigo.strip().upper()

  if not cod_limpio:

    return False

  if buscar_codigo(cod_limpio, dicc_productos):

    return False

  return True



def validar_texto(texto):

  return bool(texto.strip())



def validar_peso(peso_str):

  try:

    return float(peso_str) > 0

  except ValueError:

    return False



def validar_booleano(opcion_str):

  return opcion_str.strip().lower() in ['s', 'n']



def validar_precio_val(precio_str):

  try:

    return int(precio_str) > 0

  except ValueError:

    return False



def validar_unidades(unidades_str):

  try:

    return int(unidades_str) >= 0

  except ValueError:

    return False



def agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades, dicc_productos, dicc_stock):

  cod_upper = codigo.strip().upper()

  if buscar_codigo(cod_upper, dicc_productos): 

    return False

  



  bool_importado = (es_importado.strip().lower() == 's')

  bool_cachorro = (es_para_cachorro.strip().lower() == 's')

  



  dicc_productos[cod_upper] = [nombre.strip(), categoria.strip(), marca.strip(), float(peso_kg), bool_importado, bool_cachorro]

  dicc_stock[cod_upper] = [int(precio), int(unidades)]

  return True







def eliminar_producto(codigo, dicc_productos, dicc_stock):

  cod_upper = codigo.strip().upper()

  if buscar_codigo(cod_upper, dicc_productos): 

    dicc_productos.pop(cod_upper) 

    dicc_stock.pop(cod_upper) 

    return True

  return False





def mostrar_menu():

  print("\n========== MENÚ PRINCIPAL ==========")

  print("1. Unidades por categoría")

  print("2. Búsqueda de productos por rango de precio")

  print("3. Actualizar precio de producto")

  print("4. Agregar producto")

  print("5. Eliminar producto")

  print("6. Salir")

  print("=====================================")



def main():

  

  productos = productos_iniciales.copy()

  stock = stock_inicial.copy()

  

  while True: 

    mostrar_menu()

    opc = leer_opcion()

    

    if opc is None:

      continue

      

    if opc == 1:

      cat = input("Ingrese categoría a consultar: ")

      unidades_categoria(cat, productos, stock) 

      

    elif opc == 2:

      

      while True:

        try:

          p_min = int(input("Ingrese precio mínimo: "))

          p_max = int(input("Ingrese precio máximo: "))

          if p_min >= 0 and p_max >= 0 and p_min <= p_max:

            break

          else:

            print("Debe ingresar valores válidos (p_min <= p_max).")

        except ValueError:

          print("Debe ingresar valores enteros") 

      

      busqueda_precio(p_min, p_max, productos, stock)

      

    elif opc == 3:

      while True:

        cod = input("Ingrese código del producto: ")



        while True:

          try:

            n_precio = int(input("Ingrese nuevo precio: "))

            if n_precio > 0:

              break

            print("El precio debe ser un número entero mayor a cero.")

          except ValueError:

            print("Debe ingresar un valor entero.")

        

        

        if actualizar_precio(cod, n_precio, productos, stock):

          print("Precio actualizado") 

        else:

          print("El código no existe") 

          

        resp = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower() 

        if resp != 's': 

          break

          

    elif opc == 4:

      

      cod = input("Ingrese código del producto: ")

      nom = input("Ingrese nombre: ")

      cat = input("Ingrese categoría: ")

      mar = input("Ingrese marca: ")

      pes = input("Ingrese peso (kg): ")

      imp = input("¿Es importado? (s/n): ")

      cac = input("¿Es para cachorro? (s/n): ")

      pre = input("Ingrese precio: ")

      uni = input("Ingrese unidades: ")

      

      

      if not validar_codigo(cod, productos):

        print("Error: Código inválido o ya existente.") 
        
      elif not validar_texto(nom):

        print("Error: El nombre no puede estar vacío.") 
        

      elif not validar_texto(cat):

        print("Error: La categoría no puede estar vacía.") 
        

      elif not validar_texto(mar):

        print("Error: La marca no puede estar vacía.") 
        

      elif not validar_peso(pes):

        print("Error: El peso debe ser un número decimal mayor a cero.") 
        

      elif not validar_booleano(imp):

        print("Error: El campo importado debe ser 's' o 'n'.") 
        
      elif not validar_booleano(cac):

        print("Error: El campo cachorro debe ser 's' o 'n'.") 

        

      elif not validar_precio_val(pre):

        print("Error: El precio debe ser un entero mayor a cero.") 

      elif not validar_unidades(uni):

        print("Error: Las unidades deben ser un entero mayor o igual a cero.") 

      else:

        

        if agregar_producto(cod, nom, cat, mar, pes, imp, cac, pre, uni, productos, stock):

          print("Producto agregado")

        else:

          print("El código ya existe") 

          

    elif opc == 5:

      cod = input("Ingrese código del producto que desea eliminar: ")

      

      if eliminar_producto(cod, productos, stock):

        print("Producto eliminado") 
      else:

        print("El código no existe") 

        

    elif opc == 6:

      print("Programa finalizado.") 

      break





if __name__ == "__main__":

  main()

