import json

class OrganizadorDeTempo:
    def __init__(self, arquivo="agenda.json"):
        self.arquivo = arquivo
        self.carregar_agenda()

    def carregar_agenda(self):
        try:
            with open(self.arquivo, "r") as f:
                self.agenda = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.agenda = {}

    def salvar_agenda(self):
        with open(self.arquivo, "w") as f:
            json.dump(self.agenda, f, indent=4)

    def adicionar_evento(self, data, evento):
        if data in self.agenda:
            self.agenda[data].append(evento)
        else:
            self.agenda[data] = [evento]
        self.salvar_agenda()
        print(f"Evento '{evento}' adicionado em {data}.")

    def listar_eventos(self, data):
        eventos = self.agenda.get(data, [])
        if eventos:
            print(f"Eventos em {data}:")
            for i, evento in enumerate(eventos, 1):
                print(f"{i}. {evento}")
        else:
            print(f"Nenhum evento encontrado em {data}.")

    def remover_evento(self, data, indice):
        if data in self.agenda and 0 < indice <= len(self.agenda[data]):
            evento = self.agenda[data].pop(indice - 1)
            self.salvar_agenda()
            print(f"Evento '{evento}' removido de {data}.")
        else:
            print("Índice inválido ou data sem eventos.")

if __name__ == "__main__":
    organizador = OrganizadorDeTempo()
    while True:
        print("\n1. Adicionar evento")
        print("2. Listar eventos")
        print("3. Remover evento")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            data = input("Digite a data (AAAA-MM-DD): ")
            evento = input("Digite o evento: ")
            organizador.adicionar_evento(data, evento)
        elif opcao == "2":
            data = input("Digite a data (AAAA-MM-DD): ")
            organizador.listar_eventos(data)
        elif opcao == "3":
            data = input("Digite a data (AAAA-MM-DD): ")
            organizador.listar_eventos(data)
            indice = int(input("Digite o número do evento para remover: "))
            organizador.remover_evento(data, indice)
        elif opcao == "4":
            break
        else:
            print("Opção inválida, tente novamente.")
