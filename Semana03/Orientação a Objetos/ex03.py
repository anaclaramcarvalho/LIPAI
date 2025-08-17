"""crie uma classe Participacao que deve ter como atributos codigo, data inicio, data fim, aluno e o projeto associado. """
class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno: Aluno, projeto: Projeto):
        self.codigo = codigo
        self.aluno = aluno
        self.projeto = projeto
        # As datas são atribuídas por último para permitir a validação cruzada
        self.data_inicio = data_inicio
        self.data_fim = data_fim

    @property
    def codigo(self) -> int:
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor is None: raise ValueError("O código da participação não pode ser nulo.")
        try:
            self._codigo = int(valor)
        except (ValueError, TypeError):
            raise ValueError("O código da participação deve ser um número inteiro.")

    @property
    def data_inicio(self) -> date:
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, valor):
        self._data_inicio = self._validar_e_converter_data(valor, "Data de início")

    @property
    def data_fim(self) -> date:
        return self._data_fim

    @data_fim.setter
    def data_fim(self, valor):
        data_convertida = self._validar_e_converter_data(valor, "Data de fim")
        if hasattr(self, '_data_inicio') and data_convertida < self.data_inicio:
            raise ValueError("A data de fim não pode ser anterior à data de início.")
        self._data_fim = data_convertida

    @property
    def aluno(self) -> Aluno:
        return self._aluno

    @aluno.setter
    def aluno(self, valor: Aluno):
        if not isinstance(valor, Aluno):
            raise TypeError("O atributo 'aluno' deve ser uma instância da classe Aluno.")
        self._aluno = valor

    @property
    def projeto(self) -> Projeto:
        return self._projeto

    @projeto.setter
    def projeto(self, valor: Projeto):
        if not isinstance(valor, Projeto):
            raise TypeError("O atributo 'projeto' deve ser uma instância da classe Projeto.")
        self._projeto = valor

    def _validar_e_converter_data(self, valor_data, nome_campo: str) -> date:
        if isinstance(valor_data, date):
            return valor_data
        if isinstance(valor_data, str):
            try:
                return date.fromisoformat(valor_data)
            except ValueError:
                raise ValueError(f"{nome_campo} em formato de string deve ser 'AAAA-MM-DD'.")
        raise TypeError(f"{nome_campo} deve ser um objeto 'date' ou uma string 'AAAA-MM-DD'.")

    def __repr__(self) -> str:
        return (f"Participacao(codigo={self.codigo}, "
                f"data_inicio='{self.data_inicio}', data_fim='{self.data_fim}', "
                f"aluno={repr(self.aluno)}, projeto={repr(self.projeto)})")

    def __str__(self) -> str:
        return (f"Participação (Cód: {self.codigo}): {self.aluno.nome} no projeto "
                f"'{self.projeto.titulo}' de {self.data_inicio.strftime('%d/%m/%Y')} "
                f"a {self.data_fim.strftime('%d/%m/%Y')}.")

    def __eq__(self, outro) -> bool:
        if not isinstance(outro, Participacao):
            return NotImplemented
        return self.codigo == outro.codigo

    def __hash__(self) -> int:
        return hash(self.codigo)