from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
from workflowengine.models.CustomUserModel import CustomUser

@task
def download(url, filename):
    """
    Download a page and save it to the BASEDIR directory
      url: the url to download
      filename: the filename used to save the url in BASEDIR
    """
    response = urllib.request.urlopen(url)
    data = response.read()
    with open(BASEDIR+"/"+filename,'wb') as file:
        file.write(data)
    file.close()

@task
def list():
    """ Return an array of all downloaded files """
    return CustomUser.objects.all()