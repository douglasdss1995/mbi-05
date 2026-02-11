# Classe base (pai/superclasse)
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, sou {self.nome}"


# Classe derivada (filha/subclasse)
class Funcionario(Pessoa):
    def __init__(self, nome, idade, matricula, salario):
        super().__init__(nome, idade)  # Chama construtor da classe pai
        self.matricula = matricula
        self.salario = salario

    def trabalhar(self):
        return f"{self.nome} está trabalhando"


# Funcionário herda tudo de Pessoa
func = Funcionario("João", 35, 10001, 5500)
print(func.apresentar())  # Método herdado
print(func.trabalhar())  # Método próprio


# Sobrescrita de métodos (Override)
class Gerente(Funcionario):
    def __init__(self, nome, idade, matricula, salario, departamento):
        super().__init__(nome, idade, matricula, salario)
        self.departamento = departamento

    # Sobrescreve o método da classe pai
    def apresentar(self):
        # Pode chamar o método original
        apresentacao_base = super().apresentar()
        return f"{apresentacao_base} e sou gerente do {self.departamento}"

    def aprovar_despesa(self, valor):
        return f"Despesa de R$ {valor} aprovada"


gerente = Gerente("Maria", 40, 20001, 8000, "TI")
print(gerente.apresentar())  # Usa versão sobrescrita


# Herança múltipla
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        pass


class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando"


class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando"


class Morcego(Mamifero, Ave):  # Herança múltipla
    def emitir_som(self):
        return "Chirp!"


morcego = Morcego("Batman")
print(morcego.amamentar())  # De Mamifero
print(morcego.voar())  # De Ave
print(morcego.emitir_som())  # Próprio

# Verificando tipo e herança
print(isinstance(gerente, Gerente))  # True
print(isinstance(gerente, Funcionario))  # True
print(isinstance(gerente, Pessoa))  # True
print(issubclass(Gerente, Funcionario))  # True
print(issubclass(Gerente, Pessoa))  # True

# Classes abstratas (ABC - Abstract Base Class)
from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        """Método que DEVE ser implementado pelas subclasses"""
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass


class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)


# Não pode instanciar classe abstrata
# forma = FormaGeometrica()  # ERRO!

# Pode instanciar subclasse que implementa métodos
retangulo = Retangulo(10, 5)
print(retangulo.calcular_area())  # 50


# Exemplo Django - Herança de Models
class TimeStampedModel(models.Model):
    """Model abstrato com timestamps"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Não cria tabela no banco


class Produto(TimeStampedModel):
    """Herda created_at e updated_at"""

    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)


class Categoria(TimeStampedModel):
    """Também herda os timestamps"""

    nome = models.CharField(max_length=100)


# Herança com ViewSets
from rest_framework import viewsets


class BaseViewSet(viewsets.ModelViewSet):
    """ViewSet base com comportamento padrão"""

    def perform_create(self, serializer):
        # Adiciona user automaticamente
        serializer.save(created_by=self.request.user)


class ProdutoViewSet(BaseViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    # Herda perform_create


class CategoriaViewSet(BaseViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    # Também herda perform_create
