 """Reflexão sobre o Uso de Depuradores em Python"""

 """O que você conseguiu enxergar no debugger que não ficava tão claro apenas 
executando o programa normalmente (sem depuração)?"""
#O debugger permite visualizar o estado internodo programa a cada passo. Enquanto a execução normal apenas mostra o "resultado final" (saída no terminal), o debugger revelou:""""
"""Fluxo de Controle:A forma exata como o Python 'pula' para dentro de uma função quando ela é chamada e como ele retorna ao ponto de origem após o 'return'."""
"""Inspeção de Variáveis: O valor exato das variáveis dentro do dicionário `aquario` antes mesmo de serem usadas no cálculo."""
"""Tipagem Dinâmica:A confirmação de que os dados inseridos via 'input()' chegam como strings e precisam ser convertidos para float antes de qualquer operação matemática."""



"""02 Em quais situações você acha mais prático usar o pdb pela linha de 
comando e em quais prefere o debugger visual do VS Code? """

"""Linha de Comando:É extremamente útil em ambientes onde não há interface gráfica, como servidores remotos (via SSH) ou quando se quer fazer uma verificação rápida e pontual em um script simples sem abrir uma IDE pesada. É "raiz" e universal.
Debugger VS Code:É preferível em projetos maiores e mais complexos. A interface visual permite ver todas as variáveis locais, globais e a "Pilha de Chamadas" (Call Stack) de uma só vez, além de permitir colocar 'breakpoints' apenas clicando ao lado do número da linha, o que é muito mais produtivo para depurações longas."""

"""03 Houve algum erro ou comportamento inesperado nos seus exercícios que 
você só percebeu por causa da depuração? Descreva brevemente."""

"""Sim. Um comportamento comum observado foi a **precisão decimal**. Ao executar o cálculo do volume, o Python pode retornar um número com muitas casas decimais (ex: `3.15403...`). Sem a depuração, você só vê o print final; com a depuração, você percebe o valor exato que está sendo passado de uma função para outra (como da função `volume` para a `potencia_termostato`), o que ajuda a decidir se é necessário usar arredondamentos (como a função `round()`) para evitar erros de propagação em cálculos financeiros ou científicos."""