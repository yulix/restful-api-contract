from contract.api.config import project


def make_safe_id(idstr):
    """Make safe ID attribute used in HTML.

    The following characters are escaped in strings:

    -   ``/``
    -   ``<``
    -   ``>``

    """

    rv = idstr\
        .replace(u'/', u'-')\
        .replace(u'<', u'') \
        .replace(u">", u'')

    return rv


class EndPoint(object):
    def __init__(self, url, method, ctx, endpoint_path):
        self.url = url
        self.method = method
        self.ctx = ctx
        self.path = endpoint_path
        self.html_id = make_safe_id(method + url)


class Group(object):
    def __init__(self, data_dict):
        self.__dict__.update(data_dict)
        self.urls = []

    def add_url(self, url, method, ctx, endpoint_path):
        self.urls.append(
            EndPoint(url, method, ctx, endpoint_path))


class Document(object):
    def __init__(self, app):
        self.app = app
        app.doc = self
        self.project = project
        self._group_dict = {}
        self._endpoints_dict = {}
        for group in project['groups']:
            new_group = Group(group)
            self._group_dict[new_group.name] = new_group
        self.groups = self._group_dict.values()

    def add_to_group(self, url, method, endpoint_path):
        ctx = self._endpoints_dict.get(endpoint_path, None)
        if not ctx:
            return
        for name, group in self._group_dict.items():
            if url.startswith(group.url_prefix):
                group.add_url(url, method, ctx, endpoint_path)

    def add_endpoint(self, ctx, endpoint_path):
        self._endpoints_dict[endpoint_path] = ctx

    def parse(self):
        for item in self.app.url_map.iter_rules():
            a = {}
            a['method'] = (item.methods - set(['HEAD', 'OPTIONS'])).pop()
            a['endpoint_path'] = item.endpoint
            a['url'] = item.rule
            self.add_to_group(**a)
