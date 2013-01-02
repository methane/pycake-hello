from pycake.dispatcher import Dispatcher

application = Dispatcher()
application.scan_package("app.controllers")

if __name__ == '__main__':
    application.run()
