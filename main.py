class Empregado:
    def _init_(self, nome, salariobase):
      self.nome = nome  
      self.salariobase = salariobase
      
    def salario(self):
      return self.salariobase
      
class Gerente(Empregado):
    def salariobonus(self):
      total = self.salariobase * 1.4
      return f"O salario do gerente é: {total}"

class Vendedor(Empregado):
    def salariovend(self):
      comissao = self.salariobase * 1.15
      return f"O salario do vendedor é igual a: {comissao}"


x = int(input("Qual o salario base? "))

nicolas = Gerente("Nicolas",x)
joao = Vendedor("Joao",x)

print(f"O salario base é: {nicolas.salario()}")
print(nicolas.salariobonus())

print(f"\nO salario base é: {joao.salario()}")
print(joao.salariovend())