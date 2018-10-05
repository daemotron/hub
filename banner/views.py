import datetime
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils import timezone
from fse.stats import get_stat


def draw(request, size, username):
    # get image
    sizes = {
        '500x100': {
            'font_user': 24,
            'font_stat': 11,
            'pos_user': (53, 49),
            'pos_ff': (53, 84),
            'pos_flights': (183, 84),
            'pos_hours': (268, 84)
        },
        '300x60': {
            'font_user': 14,
            'font_stat': 7,
            'pos_user': (31, 30),
            'pos_ff': (31, 49),
            'pos_flights': (113, 49),
            'pos_hours': (163, 49)
        }
    }
    if size not in sizes:
        size = '500x100'
    img = Image.open(os.path.join(os.path.dirname(__file__), 'static', 'stormrose-signature-{}.png'.format(size)))
    canvas = ImageDraw.Draw(img)
    font_user = ImageFont.truetype(os.path.join(os.path.dirname(__file__), 'fonts', 'Aileron-Light.otf'),
                                   sizes[size]['font_user'])
    font_stat = ImageFont.truetype(os.path.join(os.path.dirname(__file__), 'fonts', 'Aileron-Regular.otf'),
                                   sizes[size]['font_stat'])
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = None
    if user:
        if user.userstat.last_update < timezone.now() - datetime.timedelta(seconds=3600):
            data = get_stat(user.profile.key)
            if 'flights' in data:
                user.userstat.total_flights = data['flights']
            if 'Time_Flown' in data:
                user.userstat.total_hours = int(data['Time_Flown'].split(':')[0])
            user.userstat.save()
        canvas.text(sizes[size]['pos_user'], user.username, (0, 32, 91), font=font_user)
        canvas.text(sizes[size]['pos_ff'], 'First Flight: {}'.format(user.userstat.first_flight.strftime('%b %Y')),
                    (0, 32, 91), font=font_stat)
        canvas.text(sizes[size]['pos_flights'], 'Flights: {}'.format(user.userstat.total_flights), (0, 32, 91),
                    font=font_stat)
        canvas.text(sizes[size]['pos_hours'], 'Hours: {}'.format(user.userstat.total_hours), (0, 32, 91),
                    font=font_stat)
    response = HttpResponse(content_type="image/png")
    img.save(response, 'PNG')
    return response
