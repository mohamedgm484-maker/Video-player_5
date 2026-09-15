from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.video import Video
from kivy.uix.popup import Popup
import os


class VideoPlayerApp(App):
    def build(self):
        self.title = "Video Player"
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)

        title = Label(text="Video Player", size_hint=(1, 0.1), font_size='24sp')
        root.add_widget(title)

        self.video = Video(state='stop')
        root.add_widget(self.video)

        controls = BoxLayout(size_hint=(1, 0.15), spacing=10)
        play_btn = Button(text="Play")
        pause_btn = Button(text="Pause")
        stop_btn = Button(text="Stop")

        play_btn.bind(on_press=self.play_video)
        pause_btn.bind(on_press=self.pause_video)
        stop_btn.bind(on_press=self.stop_video)

        controls.add_widget(play_btn)
        controls.add_widget(pause_btn)
        controls.add_widget(stop_btn)
        root.add_widget(controls)

        open_btn = Button(text="Open Video", size_hint=(1, 0.15))
        open_btn.bind(on_press=self.open_file)
        root.add_widget(open_btn)

        return root

    def play_video(self, *args):
        if self.video.source:
            self.video.state = 'play'

    def pause_video(self, *args):
        self.video.state = 'pause'

    def stop_video(self, *args):
        self.video.state = 'stop'

    def open_file(self, *args):
        content = BoxLayout(orientation='vertical')
        chooser = FileChooserListView(
            path=os.path.expanduser('~'),
            filters=['*.mp4', '*.mkv', '*.avi', '*.mov', '*.webm']
        )
        content.add_widget(chooser)

        btn_box = BoxLayout(size_hint=(1, 0.15), spacing=10)
        select_btn = Button(text="Select")
        cancel_btn = Button(text="Cancel")
        btn_box.add_widget(select_btn)
        btn_box.add_widget(cancel_btn)
        content.add_widget(btn_box)

        popup = Popup(title="Choose Video", content=content, size_hint=(0.95, 0.95))

        def select(instance):
            if chooser.selection:
                self.video.source = chooser.selection[0]
                self.video.state = 'play'
                popup.dismiss()

        select_btn.bind(on_press=select)
        cancel_btn.bind(on_press=popup.dismiss)
        popup.open()


if __name__ == "__main__":
    VideoPlayerApp().run()
