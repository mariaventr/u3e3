class ManejadorPersona:
    def __init__(self):
        self.personas = []
    
    def agregar_persona(self, persona):
        self.personas.append(persona)
    
    def remover_persona(self, persona):
        self.personas.remove(persona)
