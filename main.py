import time
from glitch_out import GlitchOut

def formatar_tempo(segundos):
    minutos = int(segundos // 60)
    segs = int(segundos % 60)
    return f"{minutos:02d}:{segs:02d}"

def rodar_arena():
    print("=" * 60)
    print("      BEM-VINDO AO RINGUE - GLITCH OUT (100 HP)      ")
    print("=" * 60)
    
    jogo = GlitchOut()
    
    # Sorteia o primeiro set de controles e armas do Round 1
    jogo.recalcular_caos_e_arsenal()
    
    # Simulação do loop de batalha na arena grande
    print(f"\n🏟️ Arena Grande Gerada! Jogadores posicionados.")
    print(f"🔫 Arma Inicial: {jogo.arma_atual['nome']} (Dano: {jogo.arma_atual['dano']})")
    print(f"❤️ Jogador 1: {jogo.vida_jogador_1} HP | ❤️ Jogador 2: {jogo.vida_jogador_2} HP")
    print("-" * 60)

    # Vamos simular o tempo passando rápido para demonstrar a troca de 1:30
    print("\n[Simulação] O tempo está correndo na arena...")
    
    # Forçamos o relógio do sistema a fingir que se passaram 88 segundos (quase 1:30)
    jogo.tempo_inicio_round -= 88.0 
    
    # Mostra o relógio antes de virar
    tempo_restante = jogo.verificar_tempo_restante()
    print(f"⏱️ Tempo restante de round: {formatar_tempo(tempo_restante)} (Controles e armas prestes a mudar!)")
    
    # Jogador 1 atira no Jogador 2 logo antes da mudança
    print(f"\n💥 Jogador 1 acerta um tiro de {jogo.arma_atual['nome']}!")
    nova_vida_j2 = jogo.aplicar_dano(alvo=2)
    print(f"❤️ Jogador 2 agora tem: {nova_vida_j2} HP")

    # Espera 2 segundos para estourar o limite de 90 segundos (1:30)
    time.sleep(2)
    
    # Checa se o tempo acabou
    if jogo.verificar_tempo_restante() <= 0:
        print("\n⚡ [CURTO-CIRCUITO!] Se passaram 1:30! EMBARALHANDO...")
        _, nova_arma = jogo.recalcular_caos_e_arsenal()
        
        print(f"🆕 Nova arma equipada para todos: {nova_arma['nome']} (Dano: {nova_arma['dano']})")
        
        # Testando o movimento após a mudança de 1:30
        vetor_w = jogo.calcular_movimento("W")
        print(f"🎮 Teclas remapeadas internamente! Apertar 'W' agora move para: {vetor_w}")
    
    # Jogador 2 contra-ataca com a nova arma!
    print(f"\n💥 Jogador 2 contra-ataca com a nova arma: {jogo.arma_atual['nome']}!")
    nova_vida_j1 = jogo.aplicar_dano(alvo=1)
    print(f"❤️ Jogador 1 agora tem: {nova_vida_j1} HP")
    
    print("\n" + "=" * 60)
    print("           SIMULAÇÃO DE ROUND CONCLUÍDA              ")
    print("=" * 60)

if __name__ == "__main__":
    rodar_arena()
