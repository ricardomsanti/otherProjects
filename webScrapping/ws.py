#first imports
import os
import sys
from bs4 import BeautifulSoup as sp
import requests as r
import html5lib
import pandas as pd

  
  
def WebScan(hText):
    soup = sp(markup=hText, features="html5lib")
    return soup
    
    
    