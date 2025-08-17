"""crie uma classe Aluno que deve ter como atributos o prontuario, nome e email. Deve ser possível construir um objeto aluno a partir da string prontuario,nome,email ex: SP0101,João da Silva,joao@email.com . Nenhum dos atributos pode ser vazio ou nulos (utilizar propriedades). Dois alunos podem ser considerados iguais caso tenham o mesmo prontuário."""
class Aluno:
    def __init__(self, prontuario: str, nome: str, email: str):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

    @classmethod
    def from_string(cls, dados_aluno: str):
        try:
            prontuario, nome, email = [dado.strip() for dado in dados_aluno.split(',')]
        except ValueError:
            raise ValueError("A string de entrada deve estar no formato 'prontuario,nome,email'")

        return cls(prontuario, nome, email)


    @property
    def prontuario(self) -> str:
        return self._prontuario

    @prontuario.setter
    def prontuario(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("O prontuário não pode ser nulo ou vazio.")
        self._prontuario = valor

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("O nome não pode ser nulo ou vazio.")
        self._nome = valor


    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("O email não pode ser nulo ou vazio.")
        self._email = valor


    def __repr__(self) -> str:
        return f"Aluno(prontuario='{self.prontuario}', nome='{self.nome}', email='{self.email}')"

    def __str__(self) -> str:
        return f"Nome: {self.nome} (Prontuário: {self.prontuario})"

    def __eq__(self, outro) -> bool:
        if not isinstance(outro, Aluno):
            return NotImplemented
        return self.prontuario == outro.prontuario

    def __hash__(self) -> int:
        return hash(self.prontuario)

 if __name__ == "__main__":

        print("--- Criando com o construtor padrão ---")
        aluno1 = Aluno("SP3012345", "João da Silva", "joao.silva@email.com")
        print(aluno1)
        print(repr(aluno1))
        print("-" * 20)

        print("--- Criando a partir de uma string ---")
        string_aluno = "SP3054321, Maria Oliveira, maria.o@email.com"
        aluno2 = Aluno.from_string(string_aluno)
        print(aluno2)
        print(repr(aluno2))
        print("-" * 20)

        print("--- Verificando a igualdade ---")
        aluno3 = Aluno("SP3012345", "João S.", "joao.s@email.com")
        print(f"Aluno 1: {aluno1.nome}, Prontuário: {aluno1.prontuario}")
        print(f"Aluno 3: {aluno3.nome}, Prontuário: {aluno3.prontuario}")

        if aluno1 == aluno3:
            print("Aluno 1 e Aluno 3 são considerados iguais (mesmo prontuário).")
        else:
            print("Aluno 1 e Aluno 3 são diferentes.")

        if aluno1 == aluno2:
            print("Aluno 1 e Aluno 2 são iguais.")
        else:
            print("Aluno 1 e Aluno 2 são diferentes (prontuários diferentes).")
        print("-" * 20)

        print("--- Testando as validações ---")
        try:
            aluno_invalido = Aluno("", "Pedro", "pedro@email.com")
        except ValueError as e:
            print(f"Erro ao criar aluno com prontuário vazio: {e}")

        try:
            aluno_invalido_str = Aluno.from_string("SP99999,,email@valido.com")
        except ValueError as e:
            print(f"Erro ao criar aluno com nome vazio a partir de string: {e}")

        try:
            aluno1.email = "   "
        except ValueError as e:
            print(f"Erro ao tentar modificar o email para um valor inválido: {e}")

        print(f"Email do aluno1 permaneceu o mesmo: {aluno1.email}")