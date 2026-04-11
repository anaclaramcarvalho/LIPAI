''' crie uma classe Participacao que deve ter como atributos codigo, 
data inicio, data fim, aluno e o projeto associado.  '''


class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if not valor:
            raise ValueError("O código da participação não pode ser nulo.")
        self._codigo = valor

    @property
    def data_inicio(self):
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, valor):
        if not valor:
            raise ValueError("A data de início deve ser informada.")
        self._data_inicio = valor

    @property
    def data_fim(self):
        return self._data_fim

    @data_fim.setter
    def data_fim(self, valor):
        if not valor:
            raise ValueError("A data de fim deve ser informada.")
        self._data_fim = valor

    @property
    def aluno(self):
        return self._aluno

    @aluno.setter
    def aluno(self, valor):
        from ex01 import Aluno
        if not isinstance(valor, Aluno):
            raise TypeError(
                "O atributo aluno deve ser uma instância da classe Aluno.")
        self._aluno = valor

    @property
    def projeto(self):
        return self._projeto

    @projeto.setter
    def projeto(self, valor):
        from ex02 import Projeto
        if not isinstance(valor, Projeto):
            raise TypeError(
                "O atributo projeto deve ser uma instância da classe Projeto.")
        self._projeto = valor

    def __repr__(self):
        return (f"Participacao(id={self.codigo}, Aluno='{self.aluno.nome}', "
                f"Projeto='{self.projeto.titulo}')")


aluno_ex = Aluno("SP3001", "Ana Clara", "ana@ufu.br")
projeto_ex = Projeto(50, "IA na Educação", "Prof. Ricardo")

try:
    inscricao = Participacao(
        codigo=1001,
        data_inicio="2025-03-01",
        data_fim="2025-12-20",
        aluno=aluno_ex,
        projeto=projeto_ex
    )

    print("Participação registrada com sucesso!")
    print(inscricao)
    print(
        f"O aluno {inscricao.aluno.nome} está no projeto {inscricao.projeto.titulo}")

except (ValueError, TypeError) as e:
    print(f"Erro ao registrar participação: {e}")
