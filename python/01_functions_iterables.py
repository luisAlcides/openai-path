#!/usr/bin/env python3
"""
Gestor interactivo de lista de compras
- Funciones pequeñas y con propósito
- Argumentos keyword-only con *
- *args y **kwargs
- enumerate
- Desempaquetado de iterables
"""

from typing import List, Tuple

Item = Tuple[str, float]  # (nombre, precio)


# 1) Función pequeña: validar y agregar (keyword-only con *)
def agregar_item(lista: List[Item], *, nombre: str, precio: float) -> None:
    if not nombre or not isinstance(nombre, str):
        raise ValueError("El nombre debe ser un string no vacío.")
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    lista.append((nombre.strip(), float(precio)))


# 2) Mostrar enumerado (enumerate) y desempaquetado
def mostrar_lista(lista: List[Item]) -> None:
    if not lista:
        print("📝 La lista está vacía.")
        return
    print("\n🛒 Lista de compras:")
    for i, (nombre, precio) in enumerate(lista, start=1):  # desempaquetado
        print(f"  {i}. {nombre} - ${precio:.2f}")
    print()


# 3) Calcular total con *args
def calcular_total(*precios: float) -> float:
    return sum(precios)


# 4) Resumen con **kwargs
def resumen_compra(**kwargs) -> None:
    print("\n📊 Resumen de compra")
    for clave, valor in kwargs.items():
        print(f"  {clave}: {valor}")
    print()


# 5) Utilidad: parsear entrada "nombre, precio"
def parsear_item(entrada: str) -> Item:
    # Formato esperado: Nombre, 12.34
    try:
        nombre, precio_txt = entrada.split(",", maxsplit=1)
        nombre = nombre.strip()
        precio = float(precio_txt.strip())
        return (nombre, precio)
    except Exception:
        raise ValueError("Formato inválido. Usa: Nombre, 12.34")


# 6) Eliminar por índice (otra función pequeña)
def eliminar_por_indice(lista: List[Item], indice_1base: int) -> Item:
    if indice_1base < 1 or indice_1base > len(lista):
        raise IndexError("Índice fuera de rango.")
    return lista.pop(indice_1base - 1)


def main() -> None:
    compras: List[Item] = []
    menu = """
==============================
 Gestor de Lista de Compras
==============================
[a] Agregar (formato: Nombre, 12.34)
[l] Listar
[e] Eliminar por número
[t] Total
[r] Resumen
[q] Salir
------------------------------
Elige una opción: """

    while True:
        opcion = input(menu).strip().lower()

        if opcion == "a":
            linea = input("Escribe el item (Nombre, 12.34): ").strip()
            try:
                nombre, precio = parsear_item(linea)  # desempaquetado
                # keyword-only en agregar_item (gracias al *)
                agregar_item(compras, nombre=nombre, precio=precio)
                print(f"✅ Agregado: {nombre} - ${precio:.2f}\n")
            except Exception as e:
                print(f"❌ {e}\n")

        elif opcion == "l":
            mostrar_lista(compras)

        elif opcion == "e":
            if not compras:
                print("No hay nada que eliminar.\n")
                continue
            mostrar_lista(compras)
            try:
                idx = int(input("Número a eliminar: ").strip())
                eliminado = eliminar_por_indice(compras, idx)
                print(f"🗑️ Eliminado: {eliminado[0]} - ${eliminado[1]:.2f}\n")
            except Exception as e:
                print(f"❌ {e}\n")

        elif opcion == "t":
            # *args con comprensión que extrae solo los precios
            total = calcular_total(*(precio for _, precio in compras))
            print(f"💰 Total: ${total:.2f}\n")

        elif opcion == "r":
            total = calcular_total(*(p for _, p in compras))
            # **kwargs para un diccionario de resumen flexible
            resumen_compra(Items=len(compras), Total=f"${total:.2f}")

        elif opcion == "q":
            print("👋 ¡Hasta la próxima!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.\n")


if __name__ == "__main__":
    main()
