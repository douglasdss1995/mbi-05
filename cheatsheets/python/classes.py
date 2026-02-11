# Classe básica
class Pessoa:
    pass


# Criando objeto (instância)
pessoa1 = Pessoa()


# Classe com atributos e métodos
class Pessoa:
    # Construtor (__init__)
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo de instância
        self.idade = idade

    # Método de instância
    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos"

    def fazer_aniversario(self):
        self.idade += 1


# Criando objetos
pessoa1 = Pessoa("João", 35)
pessoa2 = Pessoa("Maria", 28)

print(pessoa1.apresentar())  # "Olá, meu nome é João..."
pessoa1.fazer_aniversario()
print(pessoa1.idade)  # 36


# Atributos de classe (compartilhados por todas instâncias)
class Funcionario:
    # Atributo de classe
    empresa = "FPFTech"
    total_funcionarios = 0

    def __init__(self, nome, salario):
        self.nome = nome  # Atributo de instância
        self.salario = salario
        Funcionario.total_funcionarios += 1


# Todos compartilham o mesmo valor
func1 = Funcionario("João", 5500)
func2 = Funcionario("Maria", 6000)

print(Funcionario.empresa)  # "FPFTech"
print(Funcionario.total_funcionarios)  # 2


# Métodos especiais (dunder methods)
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    # Representação em string
    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"

    # Representação técnica
    def __repr__(self):
        return f"Produto('{self.nome}', {self.preco})"

    # Comparação
    def __eq__(self, outro):
        return self.preco == outro.preco

    def __lt__(self, outro):
        return self.preco < outro.preco

    # Operações matemáticas
    def __add__(self, outro):
        return self.preco + outro.preco


produto1 = Produto("Mouse", 50.00)
produto2 = Produto("Teclado", 150.00)

print(produto1)  # "Mouse - R$ 50.00"
print(repr(produto1))  # "Produto('Mouse', 50.0)"
print(produto1 == produto2)  # False
print(produto1 < produto2)  # True
print(produto1 + produto2)  # 200.0


# Encapsulamento (convenções Python)
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular  # Público
        self._saldo = saldo_inicial  # "Protegido" (por convenção)
        self.__senha = "1234"  # "Privado" (name mangling)

    # Getter
    def get_saldo(self):
        return self._saldo

    # Setter
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            return True
        return False


conta = ContaBancaria("João", 1000)
conta.depositar(500)
print(conta.get_saldo())  # 1500


# Property - forma pythônica de getters/setters
class Pessoa:
    def __init__(self, nome):
        self._nome = nome
        self._idade = 0

    @property
    def nome(self):
        """Getter"""
        return self._nome

    @nome.setter
    def nome(self, valor):
        """Setter"""
        if isinstance(valor, str) and len(valor) > 0:
            self._nome = valor
        else:
            raise ValueError("Nome inválido")

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor >= 0:
            self._idade = valor
        else:
            raise ValueError("Idade não pode ser negativa")


pessoa = Pessoa("João")
print(pessoa.nome)  # Usa getter
pessoa.nome = "João"  # Usa setter
pessoa.idade = 35  # Usa setter
# pessoa.idade = -5     # ValueError


# Métodos estáticos e de classe
class Matematica:
    PI = 3.14159

    @staticmethod
    def somar(a, b):
        """Não acessa self nem cls"""
        return a + b

    @classmethod
    def criar_circulo(cls, raio):
        """Acessa cls (a classe)"""
        area = cls.PI * raio**2
        return area


# Não precisa instanciar
resultado = Matematica.somar(5, 3)  # 8
area = Matematica.criar_circulo(10)


# Exemplo Django
class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    ativo = models.BooleanField(default=True)

    # Método de instância
    def ativar(self):
        self.ativo = True
        self.save()

    def desativar(self):
        self.ativo = False
        self.save()

    # Property
    @property
    def nome_completo(self):
        return f"{self.primeiro_nome} {self.sobrenome}"

    # Método de classe
    @classmethod
    def criar_admin(cls, email):
        return cls.objects.create(email=email, is_staff=True, is_superuser=True)

    # __str__ para representação
    def __str__(self):
        return self.nome
