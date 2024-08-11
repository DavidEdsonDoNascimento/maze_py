from game_status import Statusgame


class Game:
    def __init__(self, map_path, instructions_path):
        self.map_path = map_path
        self.file = open(map_path, "r")
        self.lines_size = len(self.file.readline())
        self.content = self.file.read()
        self.columns_size = len(self.content.split("\n"))
        self.instructions_path = instructions_path
        self.file_instructions = open(instructions_path, "r")
        self.instructions = self.file_instructions.read()

    def show_presentation(self):
        print(f"""
        Olá, seja bem vindo aos Jogos Mortais:

        Tamanho do mapa: {self.lines_size} x {self.columns_size}

        """)

    def get_instructions(self):
        return self.instructions

    def show_instructions(self):
        print(self.get_instructions())
