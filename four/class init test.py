class Myclass:
    def __init__(self, qw):
        self.qw = qw

    def q(self):
        return print(self.qw)

    def __del__(self):
        print("바이")

Myclass('test').q()

