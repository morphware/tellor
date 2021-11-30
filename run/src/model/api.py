#!/usr/bin/env python3

from ..mapper.local   import Local
from ..wrapper.remote import Remote


# TODO Cache calls
class API:

    def __init__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self,type_,value_,traceback_):
        pass

    # Local / stored calls
    def get_providers(self):
        with Local() as local:
            return local.get_providers()

    def get_services(self):
        with Local() as local:
            return local.get_services()

    def get_regions(self):
        with Local() as local:
            return local.get_regions()

    # Remote / not stored
    def get_products(self,provider,service,region):
        return Remote().get_products(provider,service,region)
