from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDRoundFlatIconButton:
    text: "button 1"
    icon: "android"
    text_color: "white"
    halign: "center"
    valign: "center"


'''


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)


Example().run()
