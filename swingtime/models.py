import warnings
from datetime import datetime, date, timedelta
from dateutil import rrule

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from swingtime.conf import settings as swingtime_settings
from swingtime import base_models

__all__ = (
    'EventType',
    'Event',
    'Occurrence',
    'create_event'
)

if swingtime_settings.USE_CONCRETE_MODELS:

    class EventType(base_models.EventTypeBase):
        class Meta:
            app_label = 'swingtime'


    class Event(base_models.EventBase):
        class Meta:
            app_label = 'swingtime'


    class Occurrence(base_models.OccurrenceBase):
        class Meta:
            app_label = 'swingtime'


create_event = base_models.event_creation_factory(Event, EventType)
