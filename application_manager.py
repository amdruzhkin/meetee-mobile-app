class ApplicationManager:
    def __init__(self):
        self.host = 'https://meetee.ru/api'
        self.screen_manager = None

    def set_screen_manager(self, screen_manager):
        self.screen_manager = screen_manager


am = ApplicationManager()