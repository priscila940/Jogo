import hashlib
import random
import time

class GlitchOut:
    def __init__(self):
        # 1. Configurações Físicas do Teclado (Estático para burlar hacks)
        self._CONTROLES_PADRAO = {
            "W": (0, -1),  # Cima
            "S": (0, 1),   # Baixo
            "A": (-1, 0),  # Esquerda
            "D": (1, 0)    # Direita
        }
        
        # 2. Arsenal de Armas da Arena
        self.ARSENAL = [
            {"nome": "Pistola de Plasma", "dano": 15, "alcance": "Longo"},
            {"nome": "Escopeta Desregulada", "dano": 35, "alcance": "Curto"},
            {"nome": "Espada de Laser", "dano": 25, "alcance": "Corpo a Corpo"},
            {"nome": "Lança-Granadas Instável", "dano": 50, "alcance": "Área"},
            {"nome": "Metralhadora de Choque", "dano": 10, "alcance": "Médio"}
        ]
        
        # 3. Estado Inicial do Round e Jogadores
        self._estado_caos_oculto = (1, 1) 
        self.arma_atual = self.ARSENAL[0]
        self.vida_jogador_1 = 100
        self.vida_jogador_2 = 100
        
        # Configuração de Tempo (1 minuto e 30 segundos = 90 segundos)
        self.DURACAO_ROUND = 90.0 
        self.tempo_inicio_round = time.time()
        
    def verificar_tempo_restante(self):
        """Retorna quanto tempo falta para a próxima mudança"""
        tempo_decorrido = time.time() - self.tempo_inicio_round
        tempo_restante = max(0.0, self.DURACAO_ROUND - tempo_decorrido)
        return tempo_restante

    def recalcular_caos_e_arsenal(self):
        """Zera o timer, muda as direções físicas e sorteia uma nova arma"""
        self.tempo_inicio_round = time.time() # Reinicia o relógio de 1:30
        
        # Gerador de semente com alta entropia
        semente = f"{time.time_ns()}{random.randint(0, 100000)}"
        hash_obj = hashlib.sha256(semente.encode())
        hash_val = int(hash_obj.hexdigest(), 16)
        
        # 1. Muda os controles físicos ocultos
        modos_caos = [(1, 1), (-1, -1), (-1, 1), (1, -1)]
        self._estado_caos_oculto = mod_caos_escolhido = modos_caos[hash_val % len(modos_caos)]
        
        # 2. Sorteia uma nova arma para todos os jogadores
        indice_arma = (hash_val >> 4) % len(self.ARSENAL) # Shift bit para variar o index
        self.arma_atual = self.ARSENAL[indice_arma]
        
        return mod_caos_escolhido, self.arma_atual

    def calcular_movimento(self, tecla_press):
        """Aplica o caos de movimento mantendo o input limpo contra cheats"""
        tecla_upper = tecla_press.upper()
        if tecla_upper not in self._CONTROLES_PADRAO:
            return (0, 0)
            
        vx, vy = self._CONTROLES_PADRAO[tecla_upper]
        mod_x, mod_y = self._estado_caos_oculto
        
        return (vx * mod_x, vy * mod_y)

    def aplicar_dano(self, alvo):
        """Aplica o dano da arma atual no HP do oponente selecionado"""
        dano = self.arma_atual["dano"]
        if alvo == 1:
            self.vida_jogador_1 = max(0, self.vida_jogador_1 - dano)
            return self.vida_jogador_1
        elif alvo == 2:
            self.vida_jogador_2 = max(0, self.vida_jogador_2 - dano)
            return self.vida_jogador_2
        return 100

    def detectar_macro(self, tempo_resposta):
        """Segurança anti-macro padrão de 5ms"""
        return tempo_resposta < 0.005
