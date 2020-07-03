import random
from events import models as event_model
# python manage.py seed --mode=refresh

from django_seed import Seed
seeder = Seed.seeder()

seeder.add_entity(event_model.Event, 10)
inserted_pks = seeder.execute()