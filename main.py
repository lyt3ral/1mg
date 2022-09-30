from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.button import MDFloatingActionButton


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

KV = '''
MDScreen:
    md_bg_color: "#f7f2fa"

    MDBoxLayout:
        id: box
        spacing: "56dp"
        adaptive_size: True
        pos_hint: {"center_x": .5, "center_y": .5}
'''
class Example(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("conf.kv")

    def on_start(self):
        data = {
            "large": {},
        }
        for type_button in data.keys():
            self.root.ids.box.add_widget(
                MDFloatingActionButton(
                    icon="plus",
                    type=type_button,
                    theme_icon_color="Primary",
                )
            )

    def pressed(self):
        print("hello")

Example().run()
