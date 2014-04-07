#from app import app
#app.debug = True
#app.run(host = '0.0.0.0')

from app import app, sock, views
from threading import Thread

#Thread(target=views.background_thread).start()
sock.run(app, host='0.0.0.0')


