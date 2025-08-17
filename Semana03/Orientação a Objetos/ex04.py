"""crie o atributo do tipo list participacoesna classe Projeto e implemente o método add_participacaoque recebe como parâmetro um objeto Participação e adiciona na lista."""
from datetime import date
class Aluno:
    def __init__(self, prontuario: str, nome: str, email: str):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email
    @property
    def prontuario(self): return self._prontuario
    @prontuario.setter
    def prontuario(self, valor):
        if not valor or not valor.strip(): raise ValueError("O prontuário não pode ser nulo ou vazio.")
        self._prontuario = valor
    @property
    def nome(self): return self._nome
    @nome.setter
    def nome(self, valor):
        if not valor or not valor.strip(): raise ValueError("O nome não pode ser nulo ou vazio.")
        self._nome = valor
    @property
    def email(self): return self._email
    @email.setter
    def email(self, valor):
        if not valor or not valor.strip(): raise ValueError("O email não pode ser nulo ou vazio.")
        self._email = valor
    def __repr__(self):
        return f"Aluno(prontuario='{self.prontuario}', nome='{self.nome}')"
    def __eq__(self, outro):
        if not isinstance(outro, Aluno): return NotImplemented
        return self.prontuario == outro.prontuario
    def __hash__(self):
        return hash(self.prontuario)

class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno: Aluno, projeto: 'Projeto'):
        self.codigo = codigo
        self.aluno = aluno
        self.projeto = projeto
        self.data_inicio = data_inicio
        self.data_fim = data_fim
    @property
    def codigo(self): return self._codigo
    @codigo.setter
    def codigo(self, valor):
        if valor is None: raise ValueError("O código da participação não pode ser nulo.")
        try:
            self._codigo = int(valor)
        except (ValueError, TypeError):
            raise ValueError("O código da participação deve ser um número inteiro.")
    @property
    def data_inicio(self): return self._data_inicio
    @data_inicio.setter
    def data_inicio(self, valor):
        self._data_inicio = self._validar_e_converter_data(valor, "Data de início")
    @property
    def data_fim(self): return self._data_fim
    @data_fim.setter
    def data_fim(self, valor):
        data_convertida = self._validar_e_converter_data(valor, "Data de fim")
        if hasattr(self, '_data_inicio') and data_convertida < self.data_inicio:
            raise ValueError("A data de fim não pode ser anterior à data de início.")
        self._data_fim = data_convertida
    @property
    def aluno(self): return self._aluno
    @aluno.setter
    def aluno(self, valor: Aluno):
        if not isinstance(valor, Aluno): raise TypeError("O atributo 'aluno' deve ser uma instância da classe Aluno.")
        self._aluno = valor
    @property
    def projeto(self): return self._projeto
    @projeto.setter
    def projeto(self, valor: 'Projeto'):
        if not isinstance(valor, Projeto): raise TypeError("O atributo 'projeto' deve ser uma instância da classe Projeto.")
        self._projeto = valor
    def _validar_e_converter_data(self, valor_data, nome_campo: str) -> date:
        if isinstance(valor_data, date): return valor_data
        if isinstance(valor_data, str):
            try: return date.fromisoformat(valor_data)
            except ValueError: raise ValueError(f"{nome_campo} em formato de string deve ser 'AAAA-MM-DD'.")
        raise TypeError(f"{nome_campo} deve ser um objeto 'date' ou uma string 'AAAA-MM-DD'.")
    def __repr__(self):
        return f"Participacao(codigo={self.codigo}, aluno={self.aluno.nome}, projeto_cod={self.projeto.codigo})"
    def __eq__(self, outro):
        if not isinstance(outro, Participacao): return NotImplemented
        return self.codigo == outro.codigo
    def __hash__(self):
        return hash(self.codigo)

class Projeto:
    def __init__(self, codigo, titulo: str, responsavel: str):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        # NOVO ATRIBUTO: Inicializa a lista de participações vazia
        self.participacoes = []

    def add_participacao(self, participacao: Participacao):
        if not isinstance(participacao, Participacao):
            raise TypeError("O objeto a ser adicionado deve ser uma instância de Participacao.")

        if participacao.projeto is not self:
            raise ValueError("A participação não pertence a este projeto.")

        if participacao in self.participacoes:
            return  self.participacoes.append(participacao)

    @property
    def codigo(self): return self._codigo
    @codigo.setter
    def codigo(self, valor):
        if valor is None: raise ValueError("O código não pode ser nulo.")
        try: self._codigo = int(valor)
        except (ValueError, TypeError): raise ValueError("O código do projeto deve ser um número inteiro.")
    @property
    def titulo(self): return self._titulo
    @titulo.setter
    def titulo(self, valor):
        if not valor or not valor.strip(): raise ValueError("O título não pode ser nulo ou vazio.")
        self._titulo = valor
    @property
    def responsavel(self): return self._responsavel
    @responsavel.setter
    def responsavel(self, valor):
        if not valor or not valor.strip(): raise ValueError("O responsável não pode ser nulo ou vazio.")
        self._responsavel = valor
    def __repr__(self):
        return f"Projeto(codigo={self.codigo}, titulo='{self.titulo}')"
    def __eq__(self, outro):
        if not isinstance(outro, Projeto): return NotImplemented
        return self.codigo == outro.codigo
    def __hash__(self):
        return hash(self.codigo)

if __name__ == "__main__":
    aluno_carlos = Aluno("SP12345", "Carlos Drummond", "carlos.d@email.com")
    aluno_cecilia = Aluno("SP54321", "Cecília Meireles", "cecilia.m@email.com")

    proj_literatura = Projeto(101, "IA na Literatura", "Prof. Machado de Assis")
    proj_quantico = Projeto(202, "Computação Quântica", "Prof. Albert Einstein")


    part1 = Participacao(1, "2023-01-15", "2023-12-15", aluno_carlos, proj_literatura)
    part2 = Participacao(2, "2022-08-01", "2023-08-01", aluno_cecilia, proj_quantico)
    part3 = Participacao(3, "2023-03-01", "2023-09-30", aluno_cecilia, proj_literatura)

    print("--- Adicionando participações aos projetos ---")
    proj_literatura.add_participacao(part1)
    proj_literatura.add_participacao(part3)
    proj_quantico.add_participacao(part2)

    print(f"\nParticipações no projeto '{proj_literatura.titulo}':")
    for p in proj_literatura.participacoes:
        print(f"  -> Cód: {p.codigo}, Aluno: {p.aluno.nome}")

    print(f"\nParticipações no projeto '{proj_quantico.titulo}':")
    for p in proj_quantico.participacoes:
        print(f"  -> Cód: {p.codigo}, Aluno: {p.aluno.nome}")

