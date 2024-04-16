import requests
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton, MDRaisedButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from application_manager import am

class SignInScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.email_field = MDTextField(
            hint_text="E-mail",
            mode="rectangle",
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            size_hint_x=0.8
        )
        self.password_field = MDTextField(
            hint_text="Пароль",
            mode="rectangle",
            password=True,
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint_x=0.8
        )
        self.sign_in_button = MDRectangleFlatButton(
            text="Войти",
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            size_hint=(0.8, 0.0),
            on_release=self.sign_in_handler
        )
        self.sign_up_button = MDFlatButton(
            text="У меня еще нет аккаунта",
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            on_release=self.sign_up_handler,
            size_hint=(0.8, 0.0),
        )
        self.add_widget(self.email_field)
        self.add_widget(self.password_field)
        self.add_widget(self.sign_in_button)
        self.add_widget(self.sign_up_button)

    def sign_in_handler(self, instance):
        email = self.email_field.text
        password = self.password_field.text

        response = requests.get(am.host + '/login', params={'email': email, 'password': password})
        print(response.cookies.get_dict())

        print(f"Sign-in attempted with email: {email} and password: {password}")

    def sign_up_handler(self, instance):
        am.screen_manager.current = "sign_up_screen"