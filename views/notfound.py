from pyramid.view import notfound_view_config

from my_web_app.controllers.home_controller import HomeController


@notfound_view_config(renderer='my_web_app:templates/404.pt')
def notfound_view(request):
    request.response.status = 404
    view = HomeController(request)
    return {'view': view}
