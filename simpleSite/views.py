import re
import time

from django.http import JsonResponse
from django.shortcuts import render

MAX_REQUESTS = 5
TIME_PERIOD = 60
request_counts = {}


def validate_input(input_string):
    disallowed_pattern = r'[< >;:/\\\'{}[\]`~|"]'
    if re.search(disallowed_pattern, input_string):
        return False
    return True


def handle_submission(request):
    user_input = request.POST.get('name')
    current_time = int(time.time())
    user_identifier = request.META.get('REMOTE_ADDR')

    if user_identifier in request_counts and request_counts[user_identifier]["timestamp"] >= current_time - TIME_PERIOD:
        if request_counts[user_identifier]["count"] >= MAX_REQUESTS:
            return JsonResponse({'success': False, 'message': 'Too many requests. Please try again later.'})

    if validate_input(user_input):
        if user_identifier in request_counts and request_counts[user_identifier]["timestamp"] >= \
                current_time - TIME_PERIOD:
            request_counts[user_identifier]["count"] += 1
        else:
            request_counts[user_identifier] = {"count": 1, "timestamp": current_time}

        count = request_counts[user_identifier]["count"]
        return JsonResponse({'success': True, 'count': count})
    else:
        return JsonResponse({'success': False,
                             'message':
                                 'Invalid input. Please do not use these characters: < > ; : / \\ " { } [ ] ` ~ |'})


def index(request):
    if request.method == 'POST':
        return handle_submission(request)

    return render(request, 'index.html', {'message': '', 'count': 0})
