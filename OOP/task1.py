class Animal:
    def __init__(self, view: str, voice: str):
        self.view = view
        self.voice = voice
        print(f"view: {self.view}\n"
              f"voice: {self.voice}")

    def make_voice(self):
        print(self.voice)