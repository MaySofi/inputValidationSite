from django.shortcuts import render
import re
import time


MAX_REQUESTS = 5  # Maximum number of requests allowed
TIME_PERIOD = 60  # Time period in seconds
request_counts = {}


def validate_input(input_string):
    disallowed_pattern = r'[< >;:/\\\'{}[\]`~|"]'
    if re.search(disallowed_pattern, input_string):
        return False
    else:
        return True


def index(request):
    if request.method == 'POST':
        user_input = request.POST.get('name')
        current_time = int(time.time())
        user_identifier = request.META.get('REMOTE_ADDR')

        if user_identifier in request_counts and request_counts[user_identifier]["timestamp"] >= \
                current_time - TIME_PERIOD:
            if request_counts[user_identifier]["count"] >= MAX_REQUESTS:
                return render(request, 'error.html', {'message': 'Too many requests. Please try again later.'})

        if validate_input(user_input):
            if user_identifier in request_counts and request_counts[user_identifier]["timestamp"] >= \
                    current_time - TIME_PERIOD:
                request_counts[user_identifier]["count"] += 1
            else:
                request_counts[user_identifier] = {"count": 1, "timestamp": current_time}

            count = request_counts[user_identifier]["count"]
            return render(request, 'index.html', {'message': '', 'count': count})
        else:
            return render(request, 'error.html', {
                'message': 'Invalid input. Please do not use these characters: < > ; : / \\ \" { } [ ] ` ~ |'})

    return render(request, 'index.html', {'message': '', 'count': 0})
