import my_web_app.controllers.home_controller as home
import my_web_app.controllers.albums_controller as albums
import my_web_app.controllers.account_controller as account
import my_web_app.controllers.admin_controller as admin
import my_web_app.controllers.newsletter_controller as news
import my_web_app.controllers.vid_controller as videos
# import my_web_app.controllers.profile_controller as profile



def add_controller_routes(config, ctrl, prefix):
    config.add_handler(prefix + 'ctrl_index', '/' + prefix, handler=ctrl, action='index')
    config.add_handler(prefix + 'ctrl_index/', '/' + prefix + '/', handler=ctrl, action='index')
    config.add_handler(prefix + 'ctrl', '/' + prefix + '/{action}', handler=ctrl)
    config.add_handler(prefix + 'ctrl/', '/' + prefix + '/{action}/', handler=ctrl)
    config.add_handler(prefix + 'ctrl_id', '/' + prefix + '/{action}/{id}', handler=ctrl)


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    # config.add_route('home', '/')

    config.add_handler('root', '/', handler=home.HomeController, action='index')

    # config.add_handler('home_ctrl', '/home/{action}', handler=home.HomeController)
    # config.add_handler('home_ctrl/', '/home/{action}', handler=home.HomeController)
    # config.add_handler('home_ctrl_id', '/home/{action}', handler=home.HomeController)

    add_controller_routes(config, home.HomeController, 'home')
    add_controller_routes(config, albums.AlbumsController, 'albums')
    add_controller_routes(config, account.AccountController, 'account')
    add_controller_routes(config, admin.AdminController, 'admin')
    add_controller_routes(config, news.NewsletterController, 'newsletter')
    add_controller_routes(config, videos.VideosController, 'videos')
    # add_controller_routes(config, profile.ProfileController, 'profile')


