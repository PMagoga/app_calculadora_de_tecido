from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput


class telas(ScreenManager):
    
    def resultado(self):
        comprimento = int(self.ids.id_comprimento.text)
        largura = int(self.ids.id_largura.text)
        tecido_usado = comprimento * largura
        tecido_usado_metro = float((tecido_usado) / 1000)
        custo_tecido = float(self.ids.id_custo_metro.text)
        custo_tecido_metro = float(tecido_usado_metro * custo_tecido)
        acessorios = float(self.ids.id_adicionais.text)
        custo_total = round(custo_tecido_metro + acessorios, 2)
        resultado = str(custo_total)
        self.ids.id_total.text = f'O custo total da peça foi de R$ {resultado}'
    ...

class CalcTecidoApp(MDApp):
    ...


CalcTecidoApp().run()