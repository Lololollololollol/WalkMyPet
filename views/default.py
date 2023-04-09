from pyramid.view import view_config

from my_web_app.infrastructure import static_cache


# @view_config(route_name='home', renderer='my_web_app:templates/mytemplate.pt')
# def my_view(request):
#     return {'project': 'My Web App',
#             'build_cache_id': static_cache.build_cache_id}


