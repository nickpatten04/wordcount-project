from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    word_dict = {}

    for word in wordlist:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    sorted_words = sorted(word_dict.items(), key= lambda tup: tup[1], reverse=True)

    final_sort = ['Word: {} - Count: {}'.format(x,y) for x,y in sorted_words]

    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),'final_sort':final_sort})

def about(request):
    return render(request,'about.html')
