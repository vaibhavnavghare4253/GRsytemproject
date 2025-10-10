from django.apps import AppConfig

try:
    from suit.apps import DjangoSuitConfig
    class SuitConfig(DjangoSuitConfig):
        layout='vertical'
except ImportError:
    # django-suit not available, skip
    pass

class GrsystemConfig(AppConfig):
    name = 'GRsystem'
    
