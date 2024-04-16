from kivymd.uix.toolbar import MDTopAppBar


class AppBar(MDTopAppBar):
    def __init__(self):
        self.title = 'Meetee'

    def build(self):
        return self