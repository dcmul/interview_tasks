from django.core.management.base import BaseCommand, CommandError
from datetime import datetime, timedelta
import argparse
from solution.main.tasks import save_meter_reading
import time
from random import random
# from polls.models import Question as Poll


def valid_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)

class Command(BaseCommand):
    help = 'Generates readings for particular Smart Meter on a particular day'

    def add_arguments(self, parser):
        parser.add_argument('meter_id', help="Smart Meter ID",  type=int)
        parser.add_argument("meter_date", 
                            help="The Start Date - format YYYY-MM-DD", 
                            # required=True, 
                            type=valid_date)

    def handle(self, *args, **options):

        print(options)
        try:
            reading_date = options['meter_date'];
            while True:
                time.sleep(5)
                print('.')
                save_meter_reading.delay(
                    meter_id=options['meter_id'],
                    meter_date=reading_date,
                    meter_reading = random()
                    )
                reading_date += timedelta(seconds=5)
        except KeyboardInterrupt:
            print("Press Ctrl-C to terminate")
            pass

        self.stdout.write(self.style.SUCCESS('Thats it'))

        # for poll_id in options['poll_ids']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))