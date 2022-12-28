from django.shortcuts import render
import json, logging
from datetime import datetime

# Create your views here.
#from blog.models import Post, Comment
#from .forms import CommentForm

logging.basicConfig(filename="opening_logs.log", encoding='utf-8', level=logging.INFO)

def door_opener(request):
    if request.method == "POST":
        # create a dictionatry from the request body
        req_body = json.loads(request.body)
        # check my request type
        if req_body['type'] == 'toggle':
            # log the movement
            crnt_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f")[:-3]
            log_str = "\ttoggle\t"+ crnt_time + "\t" +req_body['csrf']
            logging.info(log_str)
            
            print("toggling")
    return render(request, 'door_opener.html', {})