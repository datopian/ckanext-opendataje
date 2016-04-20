import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class OpendatajePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'opendataje')

        config_['licenses_group_url'] = '{0}/licenses.json'.format(
            config_['ckan.site_url'].rstrip('/'))
