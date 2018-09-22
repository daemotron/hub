import datetime
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils import timezone
from fse.stats import get_stat


def draw(request, username):
    # get image
    img = Image.open(os.path.join(os.path.dirname(__file__), 'static', 'stormrose-signature.png'))
    canvas = ImageDraw.Draw(img)
    font_user = ImageFont.truetype(os.path.join(os.path.dirname(__file__), 'fonts', 'Aileron-Light.otf'), 24)
    font_stat = ImageFont.truetype(os.path.join(os.path.dirname(__file__), 'fonts', 'Aileron-Regular.otf'), 11)
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
        canvas.text((53, 49), user.username, (0, 32, 91), font=font_user)
        canvas.text((53, 84), 'First Flight: {}'.format(user.userstat.first_flight.strftime('%b %Y')), (0, 32, 91), font=font_stat)
        canvas.text((183, 84), 'Flights: {}'.format(user.userstat.total_flights), (0, 32, 91),
                    font=font_stat)
        canvas.text((268, 84), 'Hours: {}'.format(user.userstat.total_hours), (0, 32, 91),
                    font=font_stat)
    response = HttpResponse(content_type="image/png")
    img.save(response, 'PNG')
    return response
