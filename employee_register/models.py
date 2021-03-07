#precisamos dos models para que system funcionam .
from django.db import models

# classe de modelo correspondente para posição de classe e temos que herdar o modelo de 
# classe correspondente dentro dela
class Position(models.Model):
    title = models.CharField(max_length=50)  # unico title de propriedade

    def __str__(self):
        return self.title

class Employee(models.Model):   # vamos herdar esta classe da classe de modelo, isso para termos o DJANGO
    # variavel para armazenar o nome completo,vamos especificar o tipo desta coluna para que possamos fazer esse modelo, 
    #o ponto pode sentir que a instância pode ser usada
    fullname = models.CharField(max_length=100) # nome completo
    emp_code = models.CharField(max_length=3) # temos o numero de celular 
    mobile= models.CharField(max_length=15) #
    position = models.ForeignKey(Position,on_delete=models.CASCADE) #finalmente temos a posição e temos que modificar o comprimento máximo
    
    # usar a relação de chave estrangeira e primeiro de tudo temos que especificar,
    # o modelo para a chave estrangeira de modo que seja a posição, finalmente, 
    # devemos especificar isso em delete, cada vez que excluir voltar pra list