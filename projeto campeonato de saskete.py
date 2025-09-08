import time

times = {}

def animar(texto, tempo=0.02):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(tempo)
    print()

def cabecalho(texto):
    print("\n" + "=" * 40)
    print(f"🏀 {texto.upper()} 🏀".center(40))
    print("=" * 40)

def cadastrar_times():
    cabecalho("Cadastro de Times")
    qtd = int(input("Quantos times vão participar? "))
    for _ in range(qtd):
        nome = input("Nome do time: ")
        times[nome] = {
            "pontos": 0,
            "jogos": 0,
            "vitorias": 0,
            "derrotas": 0,
            "cestas_feitas": 0,
            "cestas_sofridas": 0
        }
    animar("Times cadastrados com sucesso! 📝")

def registrar_partida():
    cabecalho("Nova Partida")
    time1 = input("Nome do time 1: ")
    time2 = input("Nome do time 2: ")
    
    if time1 not in times or time2 not in times:
        print("❌ Um dos times não está cadastrado.")
        return

    pontos1 = int(input(f"Pontos do {time1}: "))
    pontos2 = int(input(f"Pontos do {time2}: "))

    # Atualizar cestas
    times[time1]["cestas_feitas"] += pontos1
    times[time1]["cestas_sofridas"] += pontos2
    times[time2]["cestas_feitas"] += pontos2
    times[time2]["cestas_sofridas"] += pontos1

    # Atualizar jogos
    times[time1]["jogos"] += 1
    times[time2]["jogos"] += 1

    # Resultado
    if pontos1 > pontos2:
        times[time1]["pontos"] += 2
        times[time1]["vitorias"] += 1
        times[time2]["derrotas"] += 1
        animar(f"\n🏆 {time1} venceu o jogo contra {time2}!\n")
    elif pontos2 > pontos1:
        times[time2]["pontos"] += 2
        times[time2]["vitorias"] += 1
        times[time1]["derrotas"] += 1
        animar(f"\n🏆 {time2} venceu o jogo contra {time1}!\n")
    else:
        animar("Empates não são permitidos no basquete. Resultado ignorado.")

def mostrar_classificacao():
    cabecalho("Classificação Atual")

    ranking = sorted(times.items(), key=lambda x: (x[1]["pontos"], x[1]["cestas_feitas"] - x[1]["cestas_sofridas"]), reverse=True)

    print(f"{'Pos':<4} {'Time':<15} {'Pts':<4} {'J':<3} {'V':<3} {'D':<3} {'+Pts':<6} {'-Pts':<6} {'Saldo':<6}")
    print("-" * 60)

    for pos, (nome, stats) in enumerate(ranking, start=1):
        saldo = stats["cestas_feitas"] - stats["cestas_sofridas"]
        print(f"{pos:<4} {nome:<15} {stats['pontos']:<4} {stats['jogos']:<3} {stats['vitorias']:<3} {stats['derrotas']:<3} "
              f"{stats['cestas_feitas']:<6} {stats['cestas_sofridas']:<6} {saldo:<6}")

def mostrar_campeao():
    cabecalho("Campeão do Campeonato")

    if not times:
        print("Nenhum time foi registrado.")
        return

    campeao = max(times.items(), key=lambda x: (x[1]["pontos"], x[1]["cestas_feitas"] - x[1]["cestas_sofridas"]))
    nome, stats = campeao
    animar(f"🏆 O grande campeão é: {nome.upper()} 🏆", 0.05)
    print(f"Vitórias: {stats['vitorias']} | Pontos: {stats['pontos']}")
    print("🎉 Parabéns ao time campeão! 🎉")

def menu():
    while True:
        cabecalho("Menu Principal")
        print("1. 📝 Cadastrar times")
        print("2. 🏀 Registrar partida")
        print("3. 📊 Mostrar classificação")
        print("4. 👑 Ver campeão")
        print("5. ❌ Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_times()
        elif opcao == "2":
            registrar_partida()
        elif opcao == "3":
            mostrar_classificacao()
        elif opcao == "4":
            mostrar_campeao()
        elif opcao == "5":
            animar("Saindo do campeonato... Até logo! 👋")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
