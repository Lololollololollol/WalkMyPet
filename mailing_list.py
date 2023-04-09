from my_web_app.services.mailinglist_service import MailingListService

#loading the mailchimp info to the running Pythong app
def includeme(config):
    settings = config.get_settings()
    mailchimp_api = settings.get('mailchimp_api')
    mailchimp_list_id = settings.get('mailchimp_list_id')

    MailingListService.global_init(mailchimp_api, mailchimp_list_id)
    print(len(MailingListService.mailchimp_list_id))




