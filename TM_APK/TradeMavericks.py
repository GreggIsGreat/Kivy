import numpy as np
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.core.window import Window
import pickle
import warnings

# warnings.filterwarnings('ignore', category="FutureWarning")
warnings.filterwarnings('ignore', category=UserWarning)

Window.size = (400, 600)

kv = """

MDScreenManager:
    HomeScreen:
    Main:
    PipScreen:

<HomeScreen>:
    name:'menu'
    MDRectangleFlatIconButton:
        text: "WELCOME"
        icon: "distribute-horizontal-center"
        line_color: 0, 0, 0, 0
        pos_hint: {"center_x": .5, "center_y": .5}
        font_size: 25
        # font_name: "branda.ttf"

    MDIconButton:
        icon: "location-enter"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_press: 
            root.manager.current = 'tab'
            root.manager.transition.direction = "left"
    MDLabel:
        text: "REMEMBER TO ALWAYS BE HUMBLE!!"
        halign: "center"
        pos_hint: {'center_y': 0.1}
        font_size: 12


<Main>:
    name: 'tab'

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "TRADEMAVERICKS"
            anchor_title: 'center'
            right_action_items:
                [["distribute-horizontal-center", lambda x : app.set_screen('calc')]]


        MDTabs:
            id: tabs
            allow_stretch: 'True'
            on_tab_switch: root.on_tab_switch(*args)
        
            # NAS100
            Tab:
                title: "NAS100"
                MDGridLayout:
                    cols: 2
                    padding: dp(36)
                    spacing: dp(20)
                    MDTextField:
                        id: op
                        hint_text: "OPEN"
                        mode: "line"
                        pos_hint: {"center_x": .5, "center_y": .9}
                        size_hint_x: None
                        width: 150

                    MDTextField:
                        id: vl
                        hint_text: "VOLUME"
                        mode: "line"
                        pos_hint: {"center_x": .5, "center_y": .7}
                        size_hint_x: None
                        width: 150

                    MDTextField:
                        id: lo
                        hint_text: "LOW"
                        mode: "line"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        size_hint_x: None 
                        width: 150

                    MDTextField:
                        id: hi
                        hint_text: "HIGH"
                        mode: "line"
                        pos_hint: {"center_x": .5, "center_y": .3}
                        size_hint_x: None
                        width: 150
                        
                    MDRaisedButton:
                        text: "SUBMIT"
                        on_release:  
                            app.func()
                        
                
                MDCard:
                    size_hint: None, None
                    size: "325dp", "150dp"
                    pos_hint: {"center_x": .5, "center_y": .32}
                    radius: 5
                    MDLabel:
                        text: ""
                        id: put_txt_here
                        halign: 'center'
                        pos_hint: {"center_x": .5, "center_y": .6}
                        
    

                MDIconButton:
                    icon: "home"
                    icon_size: "40"
                    pos_hint: {"center_x": .8, "center_y": .1}
                    on_press:
                        root.manager.current = 'menu'
                        root.manager.transition.direction = "right"
                        
          
            # US30
            Tab:
                title: "US30"
                MDGridLayout:
                    cols: 2
                    padding: dp(36)
                    spacing: dp(20)
                    
                    MDTextField:
                        id: o
                        hint_text: "OPEN"
                        mode: "line"
                        pos_hint: {"center_x": .5, "center_y": .9}
                        size_hint_x: None
                        width: 150

                    MDTextField:
                        id: v
                        hint_text: "VOLUME"
                        mode: "line"
                        pos_hint: {"center_x": .5, "center_y": .7}
                        size_hint_x: None
                        width: 150

                    MDTextField:
                        id: l
                        hint_text: "LOW"
                        mode: "line"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        size_hint_x: None 
                        width: 150

                    MDTextField:
                        id: h
                        hint_text: "HIGH"
                        mode: "line"
                        pos_hint: {"center_x": .5, "center_y": .3}
                        size_hint_x: None
                        width: 150
                        
                    MDRaisedButton:
                        text: "SUBMIT"
                        on_release:  
                            app.us30()
                        
                MDCard:
                    size_hint: None, None
                    size: "325dp", "150dp"
                    pos_hint: {"center_x": .5, "center_y": .32}
                    radius: 5
                    MDLabel:
                        text: ""
                        id: put_us30
                        halign: 'center'
                        pos_hint: {"center_x": .5, "center_y": .6}


                MDIconButton:
                    icon: "home"
                    icon_size: "40"
                    pos_hint: {"center_x": .8, "center_y": .1}
                    on_press:
                        root.manager.current = 'menu'
                        root.manager.transition.direction = "right"
           
            # GER30
            Tab:
                title: "GER30"
                MDGridLayout:
                    cols: 2
                    padding: dp(36)
                    spacing: dp(20)
                     
                    MDTextField:
                        id: op_1
                        hint_text: "OPEN"
                        mode: "line"
                        pos_hint: {"center_x": .5, "center_y": .9}
                        size_hint_x: None
                        width: 150

                    MDTextField:
                        id: vol_1
                        hint_text: "VOLUME"
                        mode: "line"
                        pos_hint: {"center_x": .5, "center_y": .7}
                        size_hint_x: None
                        width: 150

                    MDTextField:
                        id: lo_1
                        hint_text: "LOW"
                        mode: "line"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        size_hint_x: None 
                        width: 150

                    MDTextField:
                        id: hi_1
                        hint_text: "HIGH"
                        mode: "line"
                        pos_hint: {"center_x": .5, "center_y": .3}
                        size_hint_x: None
                        width: 150
                    MDRaisedButton:
                        text: "SUBMIT"
                        on_release:  
                            app.ger30()
                            
                MDCard:
                    size_hint: None, None
                    size: "325dp", "150dp"
                    pos_hint: {"center_x": .5, "center_y": .32}
                    radius: 5
                    MDLabel:
                        text: ""
                        id: put_ger30
                        halign: 'center'
                        pos_hint: {"center_x": .5, "center_y": .6}


                MDIconButton:
                    icon: "home"
                    icon_size: "40"
                    pos_hint: {"center_x": .8, "center_y": .1}
                    on_press:
                        root.manager.current = 'menu'
                        root.manager.transition.direction = "right"

<PipScreen>:
    name: 'calc'
    MDBoxLayout:
        orientation: "vertical"
        
        MDTopAppBar:
            title: "Pip Calc"

        MDLabel:
            text: "Soon..."
            halign: "center"
        
        MDIconButton:
            icon: "keyboard-backspace"
            icon_size: "40"
            pos_hint: {"center_x": .1, "center_y": .1}
            on_press:
                root.manager.current = 'tab'
                root.manager.transition.direction = "right"
        

<Tab>:
    MDLabel:
        id: label
        halign: "center"

"""


class Tab(MDFloatLayout, MDTabsBase):
    pass


class HomeScreen(Screen):
    pass


class PipScreen(Screen):
    pass


class Main(Screen):
    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <main.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

    # instance_tab.ids.label.text = tab_text

    # 'Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green',
    # 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray'


class TM(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "LightBlue"
        self.icon = "logo.png"
        Builder.load_string(kv)

        sm = MDScreenManager()
        sm.add_widget(HomeScreen(name='menu'))
        sm.add_widget(Main(name='tab'))
        sm.add_widget(PipScreen(name='calc'))
        return sm

    def set_screen(self, calc):
        self.root.current = calc

        # For NAS100

    def my_func(self):
        open_p = self.root.get_screen("tab").ids.op.text
        volume = self.root.get_screen("tab").ids.vl.text
        hi = self.root.get_screen("tab").ids.hi.text
        lo = self.root.get_screen("tab").ids.lo.text
        model = pickle.load(open('ustech_model', 'rb'))
        input_dt = (open_p, volume, lo, hi)
        inpt_val = np.asarray(input_dt, dtype=float)
        reshape_vals = inpt_val.reshape(1, -1)
        anticipate = model.predict(reshape_vals)
        if inpt_val[0] < anticipate:
            self.root.get_screen("tab").ids.put_txt_here.text = f"Buy!! & TP:{anticipate.round(2)}"
        else:
            self.root.get_screen("tab").ids.put_txt_here.text = f"Sell!! & TP:{anticipate.round(2)}"

    def func(self):
        self.my_func()

    # For US30
    def my_us30(self):
        o = self.root.get_screen("tab").ids.o.text
        v = self.root.get_screen("tab").ids.v.text
        h = self.root.get_screen("tab").ids.h.text
        l = self.root.get_screen("tab").ids.l.text
        model = pickle.load(open('us30_model', 'rb'))
        input_dt = (o, v, h, l)
        inpt_val = np.asarray(input_dt, dtype=float)
        reshape_vals = inpt_val.reshape(1, -1)
        anticipate = model.predict(reshape_vals)
        if inpt_val[0] < anticipate:
            self.root.get_screen("tab").ids.put_us30.text = f"Buy!! & TP:{anticipate.round(2)}"
        else:
            self.root.get_screen("tab").ids.put_us30.text = f"Sell!! & TP:{anticipate.round(2)}"

    def us30(self):
        self.my_us30()

    #  For GER30
    def my_ger30(self):
        op_1 = self.root.get_screen("tab").ids.op_1.text
        vol_1 = self.root.get_screen("tab").ids.vol_1.text
        hi_1 = self.root.get_screen("tab").ids.hi_1.text
        lo_1 = self.root.get_screen("tab").ids.lo_1.text
        model = pickle.load(open('us30_model', 'rb'))
        input_dt = (op_1, vol_1, hi_1, lo_1)
        inpt_val = np.asarray(input_dt, dtype=float)
        reshape_vals = inpt_val.reshape(1, -1)
        anticipate = model.predict(reshape_vals)
        if inpt_val[0] < anticipate:
            self.root.get_screen("tab").ids.put_ger30.text = f"Buy!! & TP:{anticipate.round(2)}"
        else:
            self.root.get_screen("tab").ids.put_ger30.text = f"Sell!! & TP:{anticipate.round(2)}"

    def ger30(self):
        self.my_ger30()


TM().run()
