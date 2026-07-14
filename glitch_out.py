import hashlib
import random
import time

class GlitchOut:
    def __init__(self):
        # As teclas físicas NUNCA mudam. O macro do hacker fica cego.
        self._CONTROLES_PADRAO = {
            "W": (0, -1),  # Cima
            "S": (0, 1),   # Baixo
            "A": (-1, 0),  # Esquerda
            "D": (1, 0)    # Direita
        }
        
        # Estado do caos oculto (multiplicadores de eixo X e Y)
        self._estado_caos_oculto = (1, 1) 
        
    def embaralhar_caos(self):
        """Muda a lógica física do jogo usando entropia baseada em nanosegundos"""
        # Semente ultra precisa para evitar previsibilidade do hash
        semente = f"{time.time_ns()}{random.randint(0, 100000)}"
        hash_obj = hashlib.sha256(semente.encode())
        
        # Possibilidades de caos (Normal, Invertido Total, Invertido X, Invertido Y)
        modos_caos = [(1, 1), (-1, -1), (-1, 1), (1, -1)]
        indice_aleatorio = int(hash_obj.hexdigest(), 16) % len(modos_caos)
        
        self._estado_caos_oculto = modos_caos[indice_aleatorio]
        return indice_aleatorio
    
    def calcular_movimento(self, tecla_press):
        """Calcula o vetor de movimento aplicando o caos direto na física"""
        tecla_upper = tecla_press.upper()
        if tecla_upper not in self._CONTROLES_PADRAO:
            return (0, 0)
            
        # Pega o vetor original pretendido pelo hardware do jogador
        vx, vy = self._CONTROLES_PADRAO[tecla_upper]
        
        # Aplica os multiplicadores ocultos que o cheat não intercepta no teclado
        mod_x, mod_y = self._estado_caos_oculto
        
        return (vx * mod_x, vy * mod_y)
    
    def detectar_macro(self, tempo_resposta):
        """
        Analisa se o tempo de resposta condiz com reflexos humanos.
        Macros geralmente respondem instantaneamente (< 2ms).
        """
        if tempo_resposta < 0.005:  # Limite rigoroso de 5 milissegundos
            return True
        return False
