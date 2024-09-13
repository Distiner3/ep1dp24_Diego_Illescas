class Continente:
    def __init__(self, codigoContinente, nombreContinente):
        self.codigoContinente = codigoContinente
        self.nombreContinente = nombreContinente

class Pais(Continente):
    def __init__(self, codigoContinente, nombreContinente, codigoPais, nombrePais):
        super().__init__(codigoContinente, nombreContinente)
        self.codigoPais = codigoPais
        self.nombrePais = nombrePais

class Empresa(Pais):
    def __init__(self, codigoContinente, nombreContinente, codigoPais, nombrePais, codigoEmpresa, nombreEmpresa, telefonoEmpresa):
        super().__init__(codigoContinente, nombreContinente, codigoPais, nombrePais)
        super().__init__(codigoContinente, nombreContinente, codigoPais, nombrePais)
        self.codigoEmpresa = codigoEmpresa
        self.nombreEmpresa = nombreEmpresa
        self.telefonoEmpresa = telefonoEmpresa

class Representante(Empresa):
    def __init__(self, codigoContinente, nombreContinente, codigoPais, nombrePais, codigoEmpresa, nombreEmpresa, telefonoEmpresa, codigoRepresentante, nombreRepresentante):
        super().__init__(codigoContinente, nombreContinente, codigoPais, nombrePais, codigoEmpresa, nombreEmpresa, telefonoEmpresa)
        self.codigoRepresentante = codigoRepresentante
        self.nombreRepresentante = nombreRepresentante

    def mostrar_informacion(self):
        print(f"Código Continente: {self.codigoContinente}, Nombre Continente: {self.nombreContinente}")
        print(f"Código País: {self.codigoPais}, Nombre País: {self.nombrePais}")
        print(f"Código Empresa: {self.codigoEmpresa}, Nombre Empresa: {self.nombreEmpresa}, Teléfono Empresa: {self.telefonoEmpresa}")
        print(f"Código Representante: {self.codigoRepresentante}, Nombre Representante: {self.nombreRepresentante}")
        print("-" * 50)

def main():
    registros = []
    num_registros = int(input("¿Cuántos registros desea ingresar? (minimo 2): "))

    if num_registros < 2:
        print("Debe ingresar al menos 2 registros.")
        return

    for i in range(num_registros):
        print(f"\nRegistro {i + 1}")
        codigoContinente = input("Ingrese el codigo del continente: ")
        nombreContinente = input("Ingrese el nombre del continente: ")
        codigoPais = input("Ingrese el codigo del pais: ")
        nombrePais = input("Ingrese el nombre del pais: ")
        codigoEmpresa = input("Ingrese el codigo de la empresa: ")
        nombreEmpresa = input("Ingrese el nombre de la empresa: ")
        telefonoEmpresa = input("Ingrese el telefono de la empresa: ")
        codigoRepresentante = input("Ingrese el codigo del representante: ")
        nombreRepresentante = input("Ingrese el nombre del representante: ")

        representante = Representante(codigoContinente, nombreContinente, codigoPais, nombrePais, codigoEmpresa, nombreEmpresa, telefonoEmpresa, codigoRepresentante, nombreRepresentante)
        registros.append(representante)

    print("\nInformación de los registros ingresados:")
    for representante in registros:
        representante.mostrar_informacion()

if __name__ == "__main__":
    main()

















        
        
