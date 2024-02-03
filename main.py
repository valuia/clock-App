import webbrowser
import requirements
from kivy.clock import Clock
import kivy

kivy.require('2.0.0')  # Replace with your Kivy version if needed


class MYApp(requirements.MDApp):

    def __init__(self):
        super().__init__()
        self.horizontal_menu = None
        self.Menu = None
        self.Time_lbl = None
        self.header = None
        self.Date = None
        self.Daytime = None

    @staticmethod
    def add_animation(widget, x_axis, y_axis):
        ani = requirements.Animation(pos_hint={'x': x_axis, 'y': y_axis},
                                     duration=1
                                     )
        ani.start(widget)

    @staticmethod
    def cnvs(add):
        with add.canvas:
            requirements.Color(0, 0, 0, 0.9)
            requirements.RoundedRectangle(pos=[100, 300], size=[800, 300], radius=[20, 20])

    def update_clock(self, dt):
        # Get the current time
        now = requirements.datetime.now()
        current_time = now.strftime("%I:%M:%S")
        current_daytime = "AM" if now.hour < 12 else "PM"
        current_date = now.strftime("%d - %b - %Y")

        # Update the labels with the current time, daytime, and date
        self.Time_lbl.text = current_time
        self.Daytime.text = current_daytime
        self.Date.text = current_date

    def build(self):
        place = requirements.MDFloatLayout()
        self.cnvs(place)

        self.header = requirements.MDLabel(text='Clock',
                                           halign='center', valign='top',
                                           pos_hint={'center_x': 0.5, 'y': 0},
                                           theme_text_color='Custom',
                                           text_color=(0.1, 0.9, 0.5, 1),
                                           font_style='H4',
                                           font_name='Arial',
                                           font_size='100sp')
        self.Time_lbl = requirements.MDLabel(
            text='',
            halign='center', valign='top',
            pos_hint={'center_x': 0.5, 'y': -0.05},
            theme_text_color='Custom',
            text_color=(0.1, 0.5, 0.9, 1),
            font_style='H2',
            font_name='Arial',
            font_size='100sp'
        )
        self.Daytime = requirements.MDLabel(
            text='AM',
            halign='center', valign='top',
            pos_hint={'center_x': 0.8, 'y': 0.1},
            theme_text_color='Custom',
            text_color=(0.9, 0.5, 0.1, 1),
            font_style='H2',
            font_name='Arial',
            font_size='100sp'
        )
        self.Date = requirements.MDLabel(
            text='30 - july - 2023',
            halign='center', valign='top',
            pos_hint={'center_x': 0.2, 'y': 0.3},
            theme_text_color='Custom',
            text_color=(0.1, 0.5, 0.9, 1),
            font_style='H6',
            font_name='Arial',
            font_size='100sp'
        )
        self.Menu = requirements.MDIconButton(
            icon='menu',
            halign='left',
            valign='top',
            theme_text_color='Custom',
            icon_color=(0.7, 0.7, 0.7, 1),
            pos_hint={'y': 0.9250},
        )
        self.horizontal_menu = requirements.MDDropdownMenu(
            items=[
                {'text': 'Follow Me', 'viewclass': 'OneLineListItem',
                 'on_release': lambda x='Follow Me': self.menu_item_callback(x)},
                {'text': 'Settings', 'viewclass': 'OneLineListItem',
                 'on_release': lambda x='Settings': self.menu_item_callback(x)},
                {'text': 'About', 'viewclass': 'OneLineListItem',
                 'on_release': lambda x='About': self.menu_item_callback(x)},
            ],
            width_mult=4,
        )  # this is a menu button items

        # placing the widgets
        place.add_widget(self.header)
        self.add_animation(self.header, 0.5, 0.4)

        place.add_widget(self.Time_lbl)
        self.add_animation(self.Time_lbl, 0.5, 0.1)

        place.add_widget(self.Daytime)
        self.add_animation(self.Daytime, 0.8, (-1 / 20))

        place.add_widget(self.Date)
        self.add_animation(self.Date, 0.2, (-1 / 15))

        self.add_animation(self.header, 0.5, 0.250)

        place.add_widget(self.Menu)
        self.Menu.bind(on_release=lambda button: self.show_menu(button, 'horizontal'))

        Clock.schedule_interval(self.update_clock, 1)  # main clock calling with Clock

        return place

    def show_menu(self, button, menu_type):
        if menu_type == 'horizontal':

            self.horizontal_menu.caller = button
            self.horizontal_menu.open()
        else:
            pass

    def menu_item_callback(self, text):
        print(f"Selected: {text}")
        if hasattr(self, "horizontal_menu"):
            #self.horizontal_menu.dismiss()
            if text == 'Follow Me':
                webbrowser.open_new_tab('https://www.youtube.com/@Visible_Error')
            elif text == "Settings":
                pass
            elif text == "About":
                pass
        else:
            pass


if __name__ == '__main__':
    MYApp().run()
