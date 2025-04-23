# Sistema de Sorteio de Rifa com Interface Gráfica

Este é um sistema simples e funcional para sorteio de rifas utilizando **Python** e **Tkinter**. Ideal para rifas de produtos como **perfumes masculinos ou femininos**, este sistema permite cadastro de participantes, sorteio automatizado e exibição dos resultados de forma visual e interativa.

## Funcionalidades

- Cadastro de participantes com nome e números escolhidos
- Validação automática:
  - Nomes só com letras
  - Números válidos entre 1 e 100
  - Números duplicados são bloqueados
- Permite nomes repetidos (João, João (2), etc.)
- Sorteio com **contagem regressiva animada**
- Exibição do número sorteado e dos vencedores
- Lista visual com todos os participantes e seus números
- Interface estilizada com cores e tamanhos de fonte diferenciados
- Sistema multithread: o sorteio não trava a interface

## Personalização Visual

- Fundo da janela em **cinza**
- Rótulos com fundo **branco** e texto em cores contrastantes como **roxo**, **preto** e **vermelho**
- Botões com cores distintas:
  - Adicionar: **roxo**
  - Sortear: **verde**
  - Sair: **vermelho**
- Fonte dos rótulos e botões em tamanho **24px**, ideal para eventos presenciais

## Tecnologias Utilizadas

- Python 3.x
- Tkinter (`tk` e `ttk`) — Interface Gráfica
- Threading — Execução assíncrona para não congelar a janela
- Random — Geração de número aleatório para sorteio

## Como Usar

1. Instale o Python (se ainda não estiver instalado).
2. Execute o arquivo principal:

   ```bash
   python Rifa_melhoria.py