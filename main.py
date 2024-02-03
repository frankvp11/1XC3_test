from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
# import requests
# import json
from kivy.network.urlrequest import UrlRequest
interface = Builder.load_string('''
#:import facade plyer.spatialorientation

<SpOrientationInterface>:
    facade: facade
    orientation: 'vertical'
    padding: '20dp'
    spacing: '10dp'

    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                id: enable_button
                text: 'Enable Sensor'
                disabled: False
                on_release:
                    root.enable_listener()
                    disable_button.disabled = not disable_button.disabled
                    enable_button.disabled = not enable_button.disabled
            Button:
                id: disable_button
                text: 'Disable Sensor'
                disabled: True
                on_release:
                    root.disable_listener()
                    disable_button.disabled = not disable_button.disabled
                    enable_button.disabled = not enable_button.disabled
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'Azimuth: ' + str(root.azimuth * (180 / 3.1415926535)) + ' degrees'
            Label:
                text: 'Pitch: ' + str(root.pitch * (180 / 3.1415926535)) + ' degrees'
            Label:
                text: 'Roll: ' + str(root.roll * (180 / 3.1415926535)) + ' degrees'

''')


class SpOrientationInterface(BoxLayout):

    pitch = NumericProperty(0)
    azimuth = NumericProperty(0)
    roll = NumericProperty(0)

    facade = ObjectProperty()

    def enable_listener(self):
        self.facade.enable_listener()
        Clock.schedule_interval(self.get_orientation, 1 / 20.)

    def disable_listener(self):
        self.facade.disable_listener()
        Clock.unschedule(self.get_orientation)

    def get_orientation(self, dt):
        if self.facade.orientation != (None, None, None):
            self.azimuth, self.pitch, self.roll = self.facade.orientation

    def send_orientation_data(self):
        data = {
            "azimuth": self.azimuth,
            "pitch": self.pitch,
            "roll": self.roll
        }

        # Modify the URL to match your server's address
        url = "http://127.0.0.1:5000/update_orientation"
        # headers = {'Content-Type': 'application/json'}
        request=  UrlRequest(url, req_body=data, req_headers={'Content-Type': 'application/json'})
        
        # try:
        #     response = requests.post(url, data=json.dumps(data), headers=headers)
        #     if response.status_code == 200:
        #         print("Data sent successfully.")
        #     else:
        #         print(f"Failed to send data. Status code: {response.status_code}")
        # except Exception as e:
        #     print(f"Error during request: {e}")


class SpOrientationTestApp(App):
    def build(self):
        interface = SpOrientationInterface()
        Clock.schedule_interval(interface.send_orientation_data, 2)

        return interface


if __name__ == "__main__":
    SpOrientationTestApp().run()