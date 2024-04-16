from kivymd.uix.toolbar import MDTopAppBar

class TopAppBar(MDTopAppBar):
    def __init__(self, drawer, **kwargs):
        super().__init__(**kwargs)
        self.drawer = drawer  # Store the drawer instance
        self.title = 'Meetee'
        self.pos_hint = {'top': 1}
        self.elevation = 1
        self.anchor_title = 'left'
        self.left_action_items = [['menu', self.toggle_drawer]]

    def toggle_drawer(self, *args):
        self.drawer.set_state('open')  # Use the stored drawer instance