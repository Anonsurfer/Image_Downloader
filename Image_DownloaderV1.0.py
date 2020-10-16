import random
import urllib.request
def download_web_image():
    url = input("Enter the Url: ")
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)
    print("The Image was downloaded !")
    print("The Image was named {}".format(full_name))
download_web_image()