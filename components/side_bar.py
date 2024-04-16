from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationDrawerMenu

class SideBar:
    def build(self):
        drawer = MDNavigationDrawer(
            id="side_bar_drawer",
            radius=(0, 16, 16, 0),
            elevation=1
        )
        menu = MDNavigationDrawerMenu()
        drawer.add_widget(menu)
        return drawer