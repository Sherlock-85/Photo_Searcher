from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests

Builder.load_file('frontend.kv')

headers = {"User-agent": 'Mozilla/5.0'}

class FirstScreen(Screen):
    # Source property available for the image widget
    # Get user query from TextInput
    def get_image_link(self):
        query = self.manager.current_screen.ids.user_query.text
        # Get wikipedia page and the first element of the image urls
        page = wikipedia.page(query)
        image_link = page.images[0]
        return image_link

    def download_image(self):
        # To access the image link, call the get_image_link method
        #Download the image
        req = requests.get(self.get_image_link(), headers=headers)
        imagepath = 'files/image.jpg'
        with open(imagepath, 'wb') as file:
            file.write(req.content)
        return imagepath

    def set_image(self):
        # Set the image in the image widget

        self.manager.current_screen.ids.img.source = self.download_image()

class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
