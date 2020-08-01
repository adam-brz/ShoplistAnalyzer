from kivy.event import EventDispatcher

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class AppEventDispatcher(EventDispatcher, metaclass=SingletonMeta):
    def __init__(self, **kwargs):
        self.register_event_type('on_generate')
        self.register_event_type('on_clear')
        self.register_event_type('on_options')
        self.register_event_type('on_results')

        super(AppEventDispatcher, self).__init__(**kwargs)

    def on_generate(self, *args):
        pass

    def on_clear(self, *args):
        pass

    def on_options(self, *args):
        pass

    def on_results(self, *args):
        pass