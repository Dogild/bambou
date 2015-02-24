# -*- coding: utf-8 -*-

from bambou import NURESTBasicUser, NURESTObject, NURESTSession

__all__ = ['Enterprise', 'NURESTUser', 'NUSession']


class NURESTUser(NURESTBasicUser):
    """ Defines a User """

    __rest_name__ = "me"

    def __init__(self):
        """ Creates a new user """

        super(NURESTUser, self).__init__()

        self.email = None
        self.firstname = None
        self.lastname = None
        self.enterprise_id = None
        self.enterprise_name = None
        self.role = None
        self.avatar_type = None
        self.avatar_data = None
        self.api_key_expiry = None

        self.expose_attribute(local_name='email', remote_name='email', attribute_type=str)
        self.expose_attribute(local_name='firstname', remote_name='firstName', attribute_type=str)
        self.expose_attribute(local_name='lastname', remote_name='lastName', attribute_type=str)
        self.expose_attribute(local_name='enterprise_id', remote_name='enterpriseID', attribute_type=str)
        self.expose_attribute(local_name='enterprise_name', remote_name='enterpriseName', attribute_type=str)
        self.expose_attribute(local_name='role', remote_name='role', attribute_type=str)
        self.expose_attribute(local_name='avatar_type', remote_name='avatarType', attribute_type=str)
        self.expose_attribute(local_name='avatar_data', remote_name='avatarData', attribute_type=str)
        self.expose_attribute(local_name='api_key_expiry', remote_name='APIKeyExpiry', attribute_type=str)

        # Overides from parents because rest name changed
        self.expose_attribute(local_name='username', remote_name='userName', attribute_type=str)  # TODO : Declare bug here
        self.expose_attribute(local_name='external_id', remote_name='externalId', attribute_type=str)  # TODO : Declare bug here

    @classmethod
    def is_resource_name_fixed(cls):
        """ Boolean to say if the resource name should be fixed. Default is False """

        return True

    def get_resource_url(self):
        """ Get resource complete url """

        name = self.__class__.rest_resource_name
        url = self.__class__.rest_base_url()
        return "%s/%s" % (url, name)

    def get_resource_url_for_child_type(self, nurest_object_type):
        """ Get the resource url for the nurest_object type """

        return "%s/%s" % (self.__class__.rest_base_url(), nurest_object_type.rest_resource_name)


class Enterprise(NURESTObject):
    """ Creates a enterprise object for tests """

    __rest_name__ = "enterprise"

    def __init__(self):
        """ Creates a new Enterprise """

        super(Enterprise, self).__init__()

        self.name = ''
        self.description = ''

        self.expose_attribute(local_name='name', remote_name='name', attribute_type=str)
        self.expose_attribute(local_name='description', remote_name='description', attribute_type=str)


# Override NURESTSession
class NUSession(NURESTSession):

    def create_rest_user(self):
        return NURESTUser()
