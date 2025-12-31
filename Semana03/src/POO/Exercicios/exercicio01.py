'''crie uma classe Aluno que deve ter como atributos o prontuario, nome e email. 
Deve ser possível construir um objeto aluno a partir da string prontuario,nome,
email ex: SP0101,João da Silva,joao@email.com . Nenhum dos atributos pode ser vazio 
ou nulos (utilizar propriedades). Dois alunos podem ser considerados iguais caso 
tenham o mesmo prontuário.'''

class Aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email


    @property
    def prontuario(self):
        return self._prontuario

    @prontuario.setter
    def prontuario(self, valor):
        if not valor or not str(valor).strip():
            raise ValueError("O prontuário não pode ser vazio.")
        self._prontuario = valor.strip()

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor or not str(valor).strip():
            raise ValueError("O nome não pode ser vazio.")
        self._nome = valor.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if not valor or not str(valor).strip():
            raise ValueError("O email não pode ser vazio.")
        self._email = valor.strip()


    @classmethod
    def from_string(cls, linha_csv):
        partes = linha_csv.split(',')
        if len(partes) != 3:
            raise ValueError("A string deve conter exatamente 3 campos separados por vírgula.")
        
        p, n, e = partes
        return cls(p.strip(), n.strip(), e.strip())

   

    def __eq__(self, outro):
        if not isinstance(outro, Aluno):
            return False
        return self.prontuario == outro.prontuario

    def __hash__(self):
        return hash(self.prontuario)

    def __repr__(self):
        return f"Aluno(prontuario='{self.prontuario}', nome='{self.nome}')"
    

try:
    aluno1 = Aluno.from_string("SP0001, Maria Silva, maria@email.com")
    aluno2 = Aluno.from_string("SP0001, Maria da Silva, maria.silva@teste.com")
    print(f"Os alunos são iguais? {aluno1 == aluno2}") 
except ValueError as e:
    print(f"Erro de validação: {e}")