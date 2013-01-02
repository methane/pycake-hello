from app.controller import *  # NOQA


class Top(AppController):
    @GET
    def index(self):
        return "Hello World"
