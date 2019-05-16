from django.shortcuts import render

# Create your views here.
def home(request):
    calls = [
        { 
            'category':'pickup',
            'description': 'pickup please',
            'store': "초원",
            'caller': 1,
            'created_on': "2019-02-18 10:00:12",
        },
        { 
            'category':'leaking',
            'description': 'Still leaking !',
            'store': "오글보글",
            'caller': 2,
            'created_on': "2019-02-18 10:00:12",
        },
        { 
            'category':'pickup',
            'description': 'pickup please',
            'store': "Chown",
            'caller': 3,
            'created_on': "2019-02-18 10:00:12",
        },

    ]

    parameter = {
        'calls': calls, 
    }
    return render( request, 'home/home.html', parameter)

def about(request):
    return render( request, 'home/about.html', {'title':'About'})

