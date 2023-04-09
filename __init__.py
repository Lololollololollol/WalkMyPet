from pyramid.config import Configurator


dev_mode = False

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_chameleon')
        config.include('pyramid_handlers')
        config.include('.routes')
        config.include('.db')
        config.include('.mailing_list')

        config.scan()
    return config.make_wsgi_app()


def init_mode(config):
    global dev_mode
    settings = config.get_settings()
    dev_mode = settings.get('mode') == 'dev'
    print('Running in {} mode.'.format('dev' if dev_mode else 'prod'))

