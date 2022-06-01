import requests

def save_file(link, filename):
    r = requests.get(link, allow_redirects=True)
    open(filename,'wb').write(r.content)

save_file('https://raw.githubusercontent.com/MilSergach/lessons/master/LICENSE', 'license')