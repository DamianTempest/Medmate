from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class PopupWithThreeButtonsApp(App):
    def build(self):
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Button to trigger popup
        show_popup_button = Button(text="Show Popup", size_hint=(None, None), size=(200, 50))
        show_popup_button.bind(on_release=self.show_popup)
        
        # Add button to layout
        main_layout.add_widget(show_popup_button)
        
        return main_layout
    
    def show_popup(self, instance):
        # Popup content layout
        popup_content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Add a message
        popup_content.add_widget(Label(text="Choose an option:"))
        
        # Add buttons
        button_layout = BoxLayout(orientation='horizontal', padding=10, spacing=10)
        button1 = Button(text="Option 1")
        button2 = Button(text="Option 2")
        button3 = Button(text="Close")
        
        # Bind actions to buttons
        button1.bind(on_release=lambda x: print("Option 1 clicked!"))
        button2.bind(on_release=lambda x: print("Option 2 clicked!"))
        button3.bind(on_release=self.close_popup)
        
        # Add buttons to the layout
        button_layout.add_widget(button1)
        button_layout.add_widget(button2)
        button_layout.add_widget(button3)
        popup_content.add_widget(button_layout)
        
        # Create Popup
        self.popup = Popup(
            title="Three Buttons Popup",
            content=popup_content,
            size_hint=(0.8, 0.4),
            auto_dismiss=False
        )
        
        # Open the popup
        self.popup.open()
    
    def close_popup(self, instance):
        # Dismiss the popup
        self.popup.dismiss()


# Run the app
if __name__ == "__main__":
    PopupWithThreeButtonsApp().run()
