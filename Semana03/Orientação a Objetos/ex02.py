"""crie uma classe Projeto que deve ter como atributos o  codigo (número inteiro que representa o código do projeto), titulo e responsável (nome do professor responsável pelo projeto). Deve ser possível construir um objeto projeto a partir da string codigo, titulo,responsavel ex: 1,Laboratório de Desenvolvimento de Software,Pedro Gomes . Nenhum dos atributos pode ser vazio ou nulos (utilizar propriedades). Dois projetos podem ser considerados iguais caso tenham o mesmo codigo."""
class Projeto:
    def __init__(self, codigo, titulo: str, responsavel: str):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel

    @classmethod
    def from_string(cls, dados_projeto: str):
        try:
            codigo_str, titulo, responsavel = [dado.strip() for dado in dados_projeto.split(',')]
        except ValueError:
            raise ValueError("A string de entrada deve estar no formato 'codigo,titulo,responsavel'")
        return cls(codigo_str, titulo, responsavel)

    @property
    def codigo(self) -> int:
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor is None:
            raise ValueError("O código não pode ser nulo.")

        try:
            valor_int = int(valor)
        except (ValueError, TypeError):
            raise ValueError("O código deve ser um número inteiro válido.")

        self._codigo = valor_int

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("O título não pode ser nulo ou vazio.")
        self._titulo = valor

    @property
    def responsavel(self) -> str:
        return self._responsavel

    @responsavel.setter
    def responsavel(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("O nome do responsável não pode ser nulo ou vazio.")
        self._responsavel = valor

    def __repr__(self) -> str:
        return f"Projeto(codigo={self.codigo}, titulo='{self.titulo}', responsavel='{self.responsavel}')"

    def __str__(self) -> str:
        return f"Projeto: '{self.titulo}' (Cód: {self.codigo}, Responsável: {self.responsavel})"

    def __eq__(self, outro) -> bool:
        if not isinstance(outro, Projeto):
            return NotImplemented
        return self.codigo == outro.codigo

    def __hash__(self) -> int:
        return hash(self.codigo)

if __name__ == "__main__":
    print("--- Criando com o construtor padrão ---")
    proj1 = Projeto(101, "Sistema de Recomendação com IA", "Prof. Ada Lovelace")
    print(proj1)
    print(repr(proj1))
    print("-" * 20)

    print("--- Criando a partir de uma string ---")
    string_projeto = " 205 , Análise de Redes Sociais, Prof. Alan Turing "
    proj2 = Projeto.from_string(string_projeto)
    print(proj2)
    print(repr(proj2))
    print("-" * 20)

    print("--- Verificando a igualdade ---")
    proj3 = Projeto(101, "IA para Detecção de Fraudes", "Prof. Grace Hopper")

    if proj1 == proj3:
        print(f"Projeto 1 e Projeto 3 são considerados iguais (mesmo código {proj1.codigo}).")
    else:
        print("Projeto 1 e Projeto 3 são diferentes.")

    if proj1 == proj2:
        print("Projeto 1 e Projeto 2 são iguais.")
    else:
        print(f"Projeto 1 e Projeto 2 são diferentes (códigos {proj1.codigo} e {proj2.codigo}).")
    print("-" * 20)

    projetos_unicos = {proj1, proj2, proj3}
    print(f"Adicionamos 3 projetos, mas o set contém {len(projetos_unicos)} projetos únicos.")
    print(projetos_unicos)
    print("-" * 20)

    print("--- Testando as validações ---")
    try:
        proj_invalido = Projeto("abc", "Título Válido", "Responsável Válido")
    except ValueError as e:
        print(f"Erro ao criar projeto com código inválido: {e}")

    try:
        proj_invalido = Projeto(999, "   ", "Responsável Válido")
    except ValueError as e:
        print(f"Erro ao criar projeto com título vazio: {e}")

    try:
        proj_invalido_str = Projeto.from_string("303,Título Válido,")
    except ValueError as e:
        print(f"Erro ao criar projeto com responsável vazio (from_string): {e}")