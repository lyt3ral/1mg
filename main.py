from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView



class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Example(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("conf.kv")

    def pressed(self):
        print("hello")

Example().run()