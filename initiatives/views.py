from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'initiatives/initiatives_home.html',
                  {'title': 'Home',
                   'subheading': 'This is home.',
                  })

def init_01(request):
    return render(request, 'initiatives/init_01.html',
                  {'title': 'initiative_01',
                   'subheading': 'initiative 1 page',
                  })

def init_02(request):
    return render(request, 'initiatives/init_02.html',
                  {'title': 'initiative_02',
                   'subheading': 'initiative 2 page',
                  })

