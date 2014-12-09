import ckan.plugins as p
import ckan.plugins.toolkit as tk

def create_gcc_vocab():
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    try:
        data = {'id': 'keywords'}
        tk.get_action('vocabulary_show')(context, data)
    except tk.ObjectNotFound:
        data = {'name': 'keywords'}
        vocab = tk.get_action('vocabulary_create')(context, data)
        for tag in (u'Politics and Public Safety', u'Economics',
                    u'Health', u'Social Questions', u'Environment',
                    u'Geography', u'Education', u'Culture and Religion',
                    u'Demography and population', u'Transport',
                    u'Transportation'):
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            tk.get_action('tag_create')(context, data)

def gcc_vocab():
    create_gcc_vocab()
    try:
        tag_list = tk.get_action('tag_list')
        gcc_codes = tag_list(data_dict={'vocabulary_id': 'keywords'})
        return gcc_codes
    except tk.ObjectNotFound:
        return None

class ExampleIDatasetFormPlugin(p.SingletonPlugin, tk.DefaultDatasetForm):
    p.implements(p.IDatasetForm)
    p.implements(p.IConfigurer)
    p.implements(p.ITemplateHelpers)

    def _modify_package_schema(self, schema):
        schema.update({
        #dcat schema
            'identifier': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'contactPoint': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'landingPage': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'issued': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'modified': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'language': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'spatial': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'temporal': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'accrualPeriodicity': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')]
        })
        #'publisher': publisher_schema(),
        schema.update({
            'keyword': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'distribution': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')]
        })
        #schema.update({
        #   'theme': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')]
        #})
        schema.update({
            'definition': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')]
        })
        # ignore default schema (not already ingored)
        schema.update({
            'name': [tk.get_validator('ignore_missing')]
        })
        # set tags schema
        schema.update({
            'theme': [
                tk.get_validator('ignore_missing'),
                tk.get_converter('convert_to_tags')('gcc_codes')
            ]
        })
        #set custom resource schema
        schema['resources'].update({
            'title': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'issued': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'modified': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'license': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'rights': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'accessURL': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'downloadURL': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'mediaType': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'format': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'byteSize': [tk.get_validator('ignore_missing')]
        })
        return schema

    def create_package_schema(self):
        # let's grab the default schema in our plugin
        schema = super(ExampleIDatasetFormPlugin, self).create_package_schema()
        #our custom field
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(ExampleIDatasetFormPlugin, self).update_package_schema()
        #our custom field
        schema = self._modify_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(ExampleIDatasetFormPlugin, self).show_package_schema()
        schema.update({
                #dcat schema
            'identifier': [tk.get_validator('ignore_missing'), tk.get_converter('convert_from_extras')]
        })
        schema.update({
            'title': [tk.get_validator('ignore_missing')]
        })
        schema.update({
            'contactPoint': [tk.get_validator('ignore_missing'), tk.get_converter('convert_from_extras')]
        })
        schema.update({
            'description': [tk.get_validator('ignore_missing'), tk.get_converter('convert_from_extras')]
        })
        schema.update({
            'landingPage': [tk.get_validator('ignore_missing'), tk.get_converter('convert_from_extras')]
        })
        schema.update({
            'issued': [tk.get_validator('ignore_missing'), tk.get_converter('convert_from_extras')]
        })
        schema.update({
            'modified': [tk.get_validator('ignore_missing'), tk.get_converter('convert_from_extras')]
        })
        schema.update({
            'language': [tk.get_validator('ignore_missing'), tk.get_converter('convert_from_extras')]
        })
        schema.update({
            'spatial': [tk.get_validator('ignore_missing'), tk.get_converter('convert_from_extras')]
        })
        schema.update({
            'temporal': [tk.get_validator('ignore_missing'), tk.get_converter('convert_from_extras')]
        })
        schema.update({
            'accrualPeriodicity': [tk.get_validator('ignore_missing'), tk.get_converter('convert_from_extras')]
        })
        #'publisher': publisher_schema(),
        schema.update({
            'keyword': [tk.get_validator('ignore_missing'), tk.get_converter('convert_from_extras')]
        })
        schema.update({
            'distribution': [tk.get_validator('ignore_missing'), tk.get_converter('convert_from_extras')]
        })
        #schema.update({
        #   'theme': [tk.get_validator('ignore_missing'), tk.get_converter('convert_from_extras')]
        #})
        schema.update({
            'definition': [tk.get_validator('ignore_missing'), tk.get_converter('convert_from_extras')]
        })
        # ignore default schema (not already ingored)
        schema.update({
            'name': [tk.get_validator('ignore_missing')]
        })
        schema['tags']['__extras'].append(tk.get_converter('free_tags_only'))
        schema.update({
            'theme': [
                tk.get_converter('convert_from_tags')('gcc_codes'),
                tk.get_validator('ignore_missing')]
        })
        #set custom resource schema
        schema['resources'].update({
            'title': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'description': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'issued': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'modified': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'license': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'rights': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'accessURL': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'downloadURL': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'mediaType': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'format': [tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'byteSize': [tk.get_validator('ignore_missing')]
        })
        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')

    def get_helpers(self):
        return {'gcc_codes': gcc_codes}
