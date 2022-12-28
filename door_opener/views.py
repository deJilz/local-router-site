from django.shortcuts import render
import json
from door_opener.models import doorCycles

# Create your views here.
#from blog.models import Post, Comment
#from .forms import CommentForm

def door_opener(request):
    if request.method == "POST":
        # create a dictionatry from the request body
        req_body = json.loads(request.body)
        # check my request type
        if req_body['type'] == 'toggle':
            # log the movement
            doorCycles(csrf=req_body['csrf']).save()
            # have the rasp pi toggle the garage
            
    return render(request, 'door_opener.html', {})