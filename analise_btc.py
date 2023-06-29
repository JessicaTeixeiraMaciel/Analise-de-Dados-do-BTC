import csv
from datetime import datetime

# Função para ler os dados do arquivo CSV e retornar um dicionário
def ler_dados_csv():
    dados = {}

    with open('btc_usd.csv', 'r') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            data = datetime.strptime(linha['Date'], '%Y-%m-%d').strftime('%d/%m/%Y')
            abertura = f"${float(linha['Open']):,.2f}"
            alta = f"${float(linha['High']):,.2f}"
            baixa = f"${float(linha['Low']):,.2f}"
            fechamento = f"${float(linha['Close']):,.2f}"
            ajustado = f"${float(linha['Adj Close']):,.2f}"
            volume = f"{int(linha['Volume']):,d}"

            dados[data] = {
                'Open': abertura,
                'High': alta,
                'Low': baixa,
                'Close': fechamento,
                'Adj Close': ajustado,
                'Volume': volume
            }

    return dados

# Função para calcular a taxa de variação
def calcular_variacao(maximo, minimo):
    variacao = ((maximo - minimo) / minimo) * 100
    return round(variacao, 2)

# Função para formatar valores monetários
def formatar_moeda(valor):
    return f"${valor:,.2f}"

# Função para exibir o menu inicial
def exibir_menu_inicial():
    print("\033[92m" + "\033[1m" + "-------------------------------------------------------------------------------------------")
    print("                                 Análise de Dados do BTC")
    print("-------------------------------------------------------------------------------------------" + "\033[0m")
    print("Este programa realiza análises e consultas dos dados históricos do BTC.")


# Função para exibir o menu de opções
def exibir_menu_opcoes(data_inicial, data_final):
    print("\033[1m" + "Periodo da consulta:", data_inicial.strftime("%d/%m/%Y"), "a", data_final.strftime("%d/%m/%Y") + "\033[0m")
    print()
    print("O que você gostaria de fazer?")
    print()
    print("\033[92m" + "1 - Alterar período da consulta")
    print("2 - Consultar lista de dados do período")
    print("3 - Consultar recordes de valores do período")
    print("4 - Calcular médias de valores do período")
    print("0 - Sair" + "\033[0m")
    print()

# Função para obter a opção selecionada pelo usuário
def obter_opcao():
    while True:
        try:
            opcao = int(input("Digite o número da opção desejada: "))
            if opcao in [1, 2, 3, 4, 0]:
                return opcao
            else:
                print("\033[1;31mOpção inválida. Digite novamente.\033[0m")
        except ValueError:
            print("\033[1;31mOpção inválida. Digite novamente.\033[0m")
    

# Função para obter a nova data inicial
def obter_nova_data_inicial(dados, data_inicial, data_final):
    print()
    print("Escolha uma data entre",data_inicial.strftime("%d/%m/%Y"),"e",data_final.strftime("%d/%m/%Y"))

    while True:
        nova_data_inicial = input("Digite a nova data inicial (DD/MM/AAAA): ")
        if nova_data_inicial in dados:
            return nova_data_inicial
        else:
            print("\033[1;31mData inválida. Digite novamente.\033[0m")

# Função para obter a nova data final
def obter_nova_data_final(dados, nova_data_inicial, data_final):
    print("Escolha uma data entre",nova_data_inicial,"e",data_final.strftime("%d/%m/%Y"))
    print()

    while True:
        nova_data_final = input("Digite a nova data final (DD/MM/AAAA): ")
        if nova_data_final in dados and nova_data_final >= nova_data_inicial:
            return nova_data_final
        else:
            print("\033[1;31mData inválida. Digite novamente.\033[0m")

# Função para exibir a lista de dados do período selecionado
def exibir_lista_dados(dados):
    print("--- Resultado ---")
    print()

    print("A sua pesquisa retornou", len(dados), "resultados.")
    print()

    for i, (data, registro) in enumerate(dados.items(), start=1):
        print(f"{i}. {data} => Abertura: {registro['Open']} | Fechamento: {registro['Close']} | Max.: {registro['High']} | Min.: {registro['Low']} | Vol.: {registro['Volume']} | Variação: {calcular_variacao(float(registro['High'].replace('$','').replace(',', '')), float(registro['Low'].replace('$','').replace(',', '')))}%")
    print()

# Função para exibir os recordes de valores do período selecionado
def exibir_recordes_valores(dados):
    print("--- Recordes de Valores ---")
    print()

    # Menor preço de abertura
    menor_abertura = min(dados.items(), key=lambda x: float(x[1]['Open'].replace('$','').replace(',', '')))
    print("PREÇO DE ABERTURA")
    print("Menor:", menor_abertura[0], "=> Abertura:", menor_abertura[1]['Open'], "| Fechamento:", menor_abertura[1]['Close'], "| Max.:", menor_abertura[1]['High'], "| Min.:", menor_abertura[1]['Low'], "| Vol.:", menor_abertura[1]['Volume'], "| Variação:", calcular_variacao(float(menor_abertura[1]['High'].replace('$','').replace(',', '')), float(menor_abertura[1]['Low'].replace('$','').replace(',', ''))), "%")

    # Maior preço de abertura
    maior_abertura = max(dados.items(), key=lambda x: float(x[1]['Open'].replace('$','').replace(',', '')))
    print("Maior:", maior_abertura[0], "=> Abertura:", maior_abertura[1]['Open'], "| Fechamento:", maior_abertura[1]['Close'], "| Max.:", maior_abertura[1]['High'], "| Min.:", maior_abertura[1]['Low'], "| Vol.:", maior_abertura[1]['Volume'], "| Variação:", calcular_variacao(float(maior_abertura[1]['High'].replace('$','').replace(',', '')), float(maior_abertura[1]['Low'].replace('$','').replace(',', ''))), "%")
    print()

    # Menor preço de fechamento
    menor_fechamento = min(dados.items(), key=lambda x: float(x[1]['Close'].replace('$','').replace(',', '')))
    print("PREÇO DE FECHAMENTO")
    print("Menor:", menor_fechamento[0], "=> Abertura:", menor_fechamento[1]['Open'], "| Fechamento:", menor_fechamento[1]['Close'], "| Max.:", menor_fechamento[1]['High'], "| Min.:", menor_fechamento[1]['Low'], "| Vol.:", menor_fechamento[1]['Volume'], "| Variação:", calcular_variacao(float(menor_fechamento[1]['High'].replace('$','').replace(',', '')), float(menor_fechamento[1]['Low'].replace('$','').replace(',', ''))), "%")

    # Maior preço de fechamento
    maior_fechamento = max(dados.items(), key=lambda x: float(x[1]['Close'].replace('$','').replace(',', '')))
    print("Maior:", maior_fechamento[0], "=> Abertura:", maior_fechamento[1]['Open'], "| Fechamento:", maior_fechamento[1]['Close'], "| Max.:", maior_fechamento[1]['High'], "| Min.:", maior_fechamento[1]['Low'], "| Vol.:", maior_fechamento[1]['Volume'], "| Variação:", calcular_variacao(float(maior_fechamento[1]['High'].replace('$','').replace(',', '')), float(maior_fechamento[1]['Low'].replace('$','').replace(',', ''))), "%")
    print()

    # Menor preço global
    menor_global = min(dados.items(), key=lambda x: float(x[1]['Low'].replace('$','').replace(',', '')))
    print("PREÇO GLOBAL")
    print("Menor:", menor_global[0], "=> Abertura:", menor_global[1]['Open'], "| Fechamento:", menor_global[1]['Close'], "| Max.:", menor_global[1]['High'], "| Min.:", menor_global[1]['Low'], "| Vol.:", menor_global[1]['Volume'], "| Variação:", calcular_variacao(float(menor_global[1]['High'].replace('$','').replace(',', '')), float(menor_global[1]['Low'].replace('$','').replace(',', ''))), "%")

    # Maior preço global
    maior_global = max(dados.items(), key=lambda x: float(x[1]['High'].replace('$','').replace(',', '')))
    print("Maior:", maior_global[0], "=> Abertura:", maior_global[1]['Open'], "| Fechamento:", maior_global[1]['Close'], "| Max.:", maior_global[1]['High'], "| Min.:", maior_global[1]['Low'], "| Vol.:", maior_global[1]['Volume'], "| Variação:", calcular_variacao(float(maior_global[1]['High'].replace('$','').replace(',', '')), float(maior_global[1]['Low'].replace('$','').replace(',', ''))), "%")
    print()

    # Menor volume
    menor_volume = min(dados.items(), key=lambda x: int(x[1]['Volume'].replace(',', '')))
    print("VOLUME")
    print("Menor:", menor_volume[0], "=> Abertura:", menor_volume[1]['Open'], "| Fechamento:", menor_volume[1]['Close'], "| Max.:", menor_volume[1]['High'], "| Min.:", menor_volume[1]['Low'], "| Vol.:", menor_volume[1]['Volume'], "| Variação:", calcular_variacao(float(menor_volume[1]['High'].replace('$','').replace(',', '')), float(menor_volume[1]['Low'].replace('$','').replace(',', ''))), "%")

    # Maior volume
    maior_volume = max(dados.items(), key=lambda x: int(x[1]['Volume'].replace(',', '')))
    print("Maior:", maior_volume[0], "=> Abertura:", maior_volume[1]['Open'], "| Fechamento:", maior_volume[1]['Close'], "| Max.:", maior_volume[1]['High'], "| Min.:", maior_volume[1]['Low'], "| Vol.:", maior_volume[1]['Volume'], "| Variação:", calcular_variacao(float(maior_volume[1]['High'].replace('$','').replace(',', '')), float(maior_volume[1]['Low'].replace('$','').replace(',', ''))), "%")
    print()

# Função para calcular as médias de valores do período selecionado
def calcular_medias_valores(dados):
    print("--- Médias de Valores ---")
    print()

    aberturas = [float(registro['Open'].replace('$','').replace(',', '')) for registro in dados.values()]
    media_aberturas = sum(aberturas) / len(aberturas)
    print("Média de Preços de Abertura:", formatar_moeda(media_aberturas))

    fechamentos = [float(registro['Close'].replace('$','').replace(',', '')) for registro in dados.values()]
    media_fechamentos = sum(fechamentos) / len(fechamentos)
    print("Média de Preços de Fechamento:", formatar_moeda(media_fechamentos))

    maximos = [float(registro['High'].replace('$','').replace(',', '')) for registro in dados.values()]
    media_maximos = sum(maximos) / len(maximos)
    print("Média de Preços Máximos:", formatar_moeda(media_maximos))

    minimos = [float(registro['Low'].replace('$','').replace(',', '')) for registro in dados.values()]
    media_minimos = sum(minimos) / len(minimos)
    print("Média de Preços Mínimos:", formatar_moeda(media_minimos))

    volumes = [int(registro['Volume'].replace(',', '')) for registro in dados.values()]
    media_volumes = sum(volumes) / len(volumes)
    print("Média de Volumes:", f"{int(media_volumes):,d}")

    print()

# Função principal
def main():
    dados = ler_dados_csv()
    data_inicial = datetime.strptime(min(dados.keys()), '%d/%m/%Y').date()
    data_final = datetime.strptime(max(dados.keys()), '%d/%m/%Y').date()

    exibir_menu_inicial()

    while True:
        exibir_menu_opcoes(data_inicial, data_final)
        opcao = obter_opcao()

        if opcao == 1:
            nova_data_inicial = obter_nova_data_inicial(dados, data_inicial, data_final)
            nova_data_final = obter_nova_data_final(dados, nova_data_inicial, data_final)
            data_inicial = datetime.strptime(nova_data_inicial, '%d/%m/%Y').date()
            data_final = datetime.strptime(nova_data_final, '%d/%m/%Y').date()

        elif opcao == 2:
            dados_periodo = {data: registro for data, registro in dados.items() if data_inicial <= datetime.strptime(data, '%d/%m/%Y').date() <= data_final}
            exibir_lista_dados(dados_periodo)

        elif opcao == 3:
            dados_periodo = {data: registro for data, registro in dados.items() if data_inicial <= datetime.strptime(data, '%d/%m/%Y').date() <= data_final}
            exibir_recordes_valores(dados_periodo)

        elif opcao == 4:
            dados_periodo = {data: registro for data, registro in dados.items() if data_inicial <= datetime.strptime(data, '%d/%m/%Y').date() <= data_final}
            calcular_medias_valores(dados_periodo)

        elif opcao == 0:
            print("Encerrando o programa...")
            break

if __name__ == '__main__':
    main()
