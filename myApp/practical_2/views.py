# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<b>Hello World</b><hr><br>practical_no.2  <br> batch:t4 <br> Team Member: <br> 1942207 : Vaibhav Bharat Sontakke <br> 1841059 : Shubham Yadav <br> !942104: Aniket Brahmankar ")
