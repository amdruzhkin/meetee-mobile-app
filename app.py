from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer, MDNavigationDrawerMenu
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivymd.uix.toolbar import MDTopAppBar

Window.size = (375, 667)


class ScreenOne(MDScreen):
    def build(self):
        self.add_widget(MDLabel(text='Screen 1', halgin='center'))
        return self


class ScreenTwo(MDScreen):
    def build(self):
        self.add_widget(MDLabel(text='Screen 2', halgin='center'))
        return self


class Meetee(MDApp):
    def __init__(self, **kwargs):
        super(Meetee, self).__init__(**kwargs)
        self.side_bar_drawer = None

    def build(self):
        screen = MDScreen()
        screen.name = 'Meetee'

        # region SideBar
        side_bar_layout = MDNavigationLayout()
        self.side_bar_drawer = MDNavigationDrawer(
            id="side_bar_drawer",
            radius=(0, 16, 16, 0),
            elevation=1)

        side_bar_menu = MDNavigationDrawerMenu()
        self.side_bar_drawer.add_widget(side_bar_menu)
        side_bar_layout.add_widget(self.side_bar_drawer)

        # endregion

        # region TopAppBar
        top_bar = MDTopAppBar()
        top_bar.title = 'Meetee'
        top_bar.pos_hint = {'top': 1}
        top_bar.elevation = 1
        top_bar.anchor_title = 'left'
        top_bar.left_action_items = [['menu', self.show_side_bar]]

        # endregion

        screen_manager = ScreenManager()
        screen_manager.add_widget(MDScreen(MDLabel(text='Screen 1', halign="center"), name='Main'))
        screen_manager.add_widget(MDScreen(MDLabel(text='Screen 2', halign="center"), name='Other'))
        screen_manager.current = 'Other'

        screen.add_widget(screen_manager)
        screen.add_widget(top_bar)
        screen.add_widget(side_bar_layout)

        return screen

    def show_side_bar(self, *args):
        self.side_bar_drawer.set_state('open')


Meetee().run()
