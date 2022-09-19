"""
CP1404_chuanjiequ practical
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

class dynamiclabels(App):
    entry_text = StringProperty()

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.list_name = ["Carl","Micharl","Morgen"]

    def build(self):
        self.title = " list name"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.list_name:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)






dynamiclabels().run()

