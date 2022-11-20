from django.shortcuts import render


def request_with_params(request):
    context = {
        'name': request.GET.get('name', 'Test') + '!',
        'message': request.GET.get('message', 'Example') + '!'
    }
    return render(request, 'example/request_with_params.html', context)
