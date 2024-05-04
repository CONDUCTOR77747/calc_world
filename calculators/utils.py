from datetime import datetime
from .models import Solution

def encode_slashes(url):
    return url.replace('/', 'slash')


def decode_slashes(url):
    return url.replace('slash', '/')


def save_solution(request):
    current_url = request.build_absolute_uri()
    current_datetime = datetime.now().isoformat(sep=" ", timespec="seconds")
    solution = Solution.objects.create(time=current_datetime, URL=current_url)
    solution.save()