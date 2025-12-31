''' crie uma classe Projeto que deve ter como atributos o  codigo (número inteiro 
que representa o código do projeto), titulo e responsável (nome do professor responsável 
pelo projeto). Deve ser possível construir um objeto projeto a partir da string codigo, 
titulo,responsavel ex: 1,Laboratório de Desenvolvimento de Software,Pedro Gomes . 
Nenhum dos atributos pode ser vazio ou nulos (utilizar propriedades). Dois projetos podem 
ser considerados iguais caso tenham o mesmo codigo. '''


class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor is None:
            raise ValueError("O código do projeto não pode ser nulo.")
        try:
            self._codigo = int(valor)
        except ValueError:
            raise ValueError(
                "O código do projeto deve ser um número inteiro válido.")

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        if not valor or not str(valor).strip():
            raise ValueError("O título do projeto não pode ser vazio.")
        self._titulo = valor.strip()

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, valor):
        if not valor or not str(valor).strip():
            raise ValueError("O responsável pelo projeto não pode ser vazio.")
        self._responsavel = valor.strip()

    @classmethod
    def from_string(cls, linha_csv):
        partes = linha_csv.split(',')
        if len(partes) != 3:
            raise ValueError(
                "A string deve conter exatamente 3 campos: codigo, titulo e responsavel.")

        cod, tit, resp = partes
        return cls(cod.strip(), tit.strip(), resp.strip())

    def __eq__(self, outro):
        if not isinstance(outro, Projeto):
            return False
        return self.codigo == outro.codigo

    def __repr__(self):
        return f"Projeto(id={self.codigo}, titulo='{self.titulo}')"


try:
    p1 = Projeto.from_string("1,Laboratório de Software,Pedro Gomes")
    p2 = Projeto(1, "Outro Nome", "Outro Professor")

    print(f"Projeto 1: {p1}")
    print(f"Os projetos são iguais? {p1 == p2}")

except ValueError as e:
    print(f"Erro ao criar projeto: {e}")
