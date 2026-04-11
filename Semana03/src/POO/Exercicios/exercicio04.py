''' crie o atributo do tipo list participacoes na classe Projeto e implemente o 
método add_participacaoque recebe como parâmetro um objeto Participação e adiciona na lista. '''


class Projeto:
    def __init__(self, codigo, titulo, responsavel):

        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel

        self.participacoes = []

    @property
    def codigo(self): return self._codigo

    @codigo.setter
    def codigo(self, valor):
        try:
            self._codigo = int(valor)
        except (ValueError, TypeError):
            raise ValueError("O código do projeto deve ser um número inteiro.")

    @property
    def titulo(self): return self._titulo

    @titulo.setter
    def titulo(self, valor):
        if not valor or not str(valor).strip():
            raise ValueError("O título não pode ser vazio.")
        self._titulo = valor.strip()

    @property
    def responsavel(self): return self._responsavel

    @responsavel.setter
    def responsavel(self, valor):
        if not valor or not str(valor).strip():
            raise ValueError("O responsável não pode ser vazio.")
        self._responsavel = valor.strip()

    def add_participacao(self, participacao):

        from ex03 import Participacao

        if not isinstance(participacao, Participacao):
            raise TypeError(
                "O objeto deve ser uma instância da classe Participacao.")

        self.participacoes.append(participacao)

    @classmethod
    def from_string(cls, linha_csv):
        partes = linha_csv.split(',')
        if len(partes) != 3:
            raise ValueError("Formato de string inválido para Projeto.")
        return cls(partes[0].strip(), partes[1].strip(), partes[2].strip())

    def __eq__(self, outro):
        if not isinstance(outro, Projeto):
            return False
        return self.codigo == outro.codigo

    def __repr__(self):
        return f"Projeto(cod={self.codigo}, titulo='{self.titulo}', total_membros={len(self.participacoes)})"


meu_projeto = Projeto(101, "IA com Python", "Prof. Alan")

aluno_a = Aluno("SP01", "Alice", "alice@email.com")
aluno_b = Aluno("SP02", "Bob", "bob@email.com")

part1 = Participacao(1, "2025-01-01", "2025-12-31", aluno_a, meu_projeto)
part2 = Participacao(2, "2025-01-01", "2025-12-31", aluno_b, meu_projeto)

meu_projeto.add_participacao(part1)
meu_projeto.add_participacao(part2)

print(
    f"O projeto '{meu_projeto.titulo}' tem {len(meu_projeto.participacoes)} membros.")
for p in meu_projeto.participacoes:
    print(f"- Aluno: {p.aluno.nome}")
