# Organizador de Tempo

## Descrição
O **Organizador de Tempo** é uma aplicação simples em Python para gerenciar eventos diários. Ele permite adicionar, listar e remover eventos armazenados em um arquivo JSON, garantindo a persistência dos dados.

## Funcionalidades
- Adicionar eventos a uma data específica
- Listar eventos cadastrados para uma data
- Remover eventos por índice
- Persistência de dados em um arquivo `agenda.json`

## Requisitos
- Python 3.x

## Como Usar
1. Clone este repositório ou copie o código-fonte.
2. Execute o script `organizador.py` no terminal:
   ```bash
   python organizador.py
   ```
3. Escolha uma das opções no menu interativo:
   - **1**: Adicionar um evento
   - **2**: Listar eventos de uma data
   - **3**: Remover um evento
   - **4**: Sair

## Exemplo de Uso
```bash
Escolha uma opção: 1
Digite a data (AAAA-MM-DD): 2025-02-24
Digite o evento: Reunião com a equipe
Evento 'Reunião com a equipe' adicionado em 2025-02-24.
```
```bash
Escolha uma opção: 2
Digite a data (AAAA-MM-DD): 2025-02-24
Eventos em 2025-02-24:
1. Reunião com a equipe
```
```bash
Escolha uma opção: 3
Digite a data (AAAA-MM-DD): 2025-02-24
Eventos em 2025-02-24:
1. Reunião com a equipe
Digite o número do evento para remover: 1
Evento 'Reunião com a equipe' removido de 2025-02-24.
```

## Estrutura do Projeto
```
organizador_de_tempo/
│── organizador.py  # Script principal
│── agenda.json      # Arquivo de armazenamento dos eventos
```

