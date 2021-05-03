from flask import Blueprint,render_template,request,flash,redirect,url_for
from wordgenerator import wordGenerator
from databasefunc import Url,databaseController, getUrl

myapp = Blueprint('myapp',__name__,static_folder='static',template_folder='templates')


@myapp.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        requesturl = request.form.get('url')
        while True:
            shortedurl = wordGenerator()
            if databaseController(shortedurl):
                break
        if 'http' not in requesturl:
            requesturl = f'https://{requesturl}'
        Url(url=requesturl,shortedUrl = shortedurl).save()
        message = f'{request.url_root}/{shortedurl}'
        flash(message)
    return render_template('index.html')



@myapp.route('/admin/')
def admin():
    data = Url.objects
    urldata = getUrl(data)
    return render_template('admin.html',urldata = urldata)



@myapp.route('/<shortedurl>')
def shortedurl(shortedurl):
    try:
        data = Url.objects.get(shortedUrl = shortedurl)
        responseUrl = data.url
        return redirect(responseUrl, code=302)
    except:
        return 'Bir problemle karşılaştık...'
    



@myapp.route('/delete/<url>')
def delete(url):
    Url.objects.get(shortedUrl=url).delete()
    return redirect(url_for('myapp.admin'))