from django.shortcuts import render


# Create your views here.
def home(request):
    context = {
        'posts':[
            {
                'author': 'Jane Austin',
                'title':'Pride and prejudice',
                'date':'August 29,2018',
                'content':'Nobody can talk me out my  opinion.'
            },
            {
                'author': 'Shakespear',
                'title':'Othello',
                'date':'December 07,2014',
                'content':'Whats in  name. A rose would smell the same even if named otherwise.'
            }
        ],
        'title':'Blog Home'
    }
    return render(request,'blog/home.html',context)