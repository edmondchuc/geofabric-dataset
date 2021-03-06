# -*- coding: utf-8 -*-
from geofabric.model.awradrainagedivision import AWRADrainageDivision
from geofabric.model.ldapi import GEOFClassRenderer, SchemaOrgRendererMixin
import geofabric._config as config


class AWRADrainageDivisionRenderer(SchemaOrgRendererMixin, GEOFClassRenderer):
    GEOF_CLASS = config.URI_AWRA_DRAINAGE_DIVISION_CLASS

    def __init__(self, request, identifier, views, *args,
                 default_view_token=None, **kwargs):
        _views = views or {}
        _uri = "".join([config.URI_AWRA_DRAINAGE_DIVISION_INSTANCE_BASE,
                        identifier])
        kwargs.setdefault('geof_template', 'class_awradrainagedivision.html')
        kwargs.setdefault('hyf_template', 'class_awradrainagedivision.html')
        super(AWRADrainageDivisionRenderer, self).__init__(
            request, _uri, _views, *args,
            default_view_token=default_view_token, **kwargs)
        self.identifier = identifier
        self.instance = AWRADrainageDivision(self.identifier)


