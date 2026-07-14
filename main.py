import time
from glitch_out import GlitchOut

def rodar_demonstracao():
    print("=" * 45)
    print(" INICIANDO PROTÓTIPO: CONTROLE QUEBRADO ")
    print("=" * 45)
    
    # Inicializa o motor do jogo
    jogo = GlitchOut()
    
    # 1. Simulação de alteração de estados (Rodadas do Jogo)
    for rodada in range(1, 4):
        modo = jogo.embaralhar_caos()
        print(f"\n[Rodada {rodada}] Estado de caos alterado na memória (ID: {modo})")
        
        # O jogador pressiona 'W' em todas as rodadas
        vetor = jogo.calcular_movimento("W")
        print(f" > Jogador pressionou 'W' -> Vetor físico resultante: {vetor}")

    print("\n" + "=" * 45)
    print(" TESTANDO SISTEMA ANTI-CHEAT ")
    print("=" * 45)

    # 2. Simulação de Input Humano (Demora para reagir à mudança)
    print("\n[Simulação] Entrada de Jogador Humano:")
    inicio_humano = time.time()
    time.sleep(0.150) # Simula 150ms de tempo de reação humana
    tempo_humano = time.time() - inicio_humano
    
    if jogo.detectar_macro(tempo_humano):
        print(f"❌ ALERTA: Macro detectado! Tempo: {tempo_humano:.4f}s")
    else:
        print(f"✅ Input Humano Autenticado. Tempo de reação: {tempo_humano:.4f}s")

    # 3. Simulação de Input de Macro/Cheat (Resposta quase instantânea)
    print("\n[Simulação] Entrada de Script/Macro Externo:")
    inicio_cheat = time.time()
    # Sem delay substancial (o script responde direto via software)
    tempo_cheat = time.time() - inicio_cheat
    
    if jogo.detectar_macro(tempo_cheat):
        print(f"❌ ALERTA: Macro detectado! Movimento bloqueado. Tempo: {tempo_cheat:.6f}s")
    else:
        print(f"✅ Input Autenticado. Tempo: {tempo_cheat:.6f}s")
    print("=" * 45)

if __name__ == "__main__":
    rodar_demonstracao()
