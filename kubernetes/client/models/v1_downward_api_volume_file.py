# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.29
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


from kubernetes.client.configuration import Configuration


class V1DownwardAPIVolumeFile(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'field_ref': 'V1ObjectFieldSelector',
        'mode': 'int',
        'path': 'str',
        'resource_field_ref': 'V1ResourceFieldSelector'
    }

    attribute_map = {
        'field_ref': 'fieldRef',
        'mode': 'mode',
        'path': 'path',
        'resource_field_ref': 'resourceFieldRef'
    }

    def __init__(self, field_ref=None, mode=None, path=None, resource_field_ref=None, local_vars_configuration=None):  # noqa: E501
        """V1DownwardAPIVolumeFile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._field_ref = None
        self._mode = None
        self._path = None
        self._resource_field_ref = None
        self.discriminator = None

        if field_ref is not None:
            self.field_ref = field_ref
        if mode is not None:
            self.mode = mode
        self.path = path
        if resource_field_ref is not None:
            self.resource_field_ref = resource_field_ref

    @property
    def field_ref(self):
        """Gets the field_ref of this V1DownwardAPIVolumeFile.  # noqa: E501


        :return: The field_ref of this V1DownwardAPIVolumeFile.  # noqa: E501
        :rtype: V1ObjectFieldSelector
        """
        return self._field_ref

    @field_ref.setter
    def field_ref(self, field_ref):
        """Sets the field_ref of this V1DownwardAPIVolumeFile.


        :param field_ref: The field_ref of this V1DownwardAPIVolumeFile.  # noqa: E501
        :type: V1ObjectFieldSelector
        """

        self._field_ref = field_ref

    @property
    def mode(self):
        """Gets the mode of this V1DownwardAPIVolumeFile.  # noqa: E501

        Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.  # noqa: E501

        :return: The mode of this V1DownwardAPIVolumeFile.  # noqa: E501
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this V1DownwardAPIVolumeFile.

        Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.  # noqa: E501

        :param mode: The mode of this V1DownwardAPIVolumeFile.  # noqa: E501
        :type: int
        """

        self._mode = mode

    @property
    def path(self):
        """Gets the path of this V1DownwardAPIVolumeFile.  # noqa: E501

        Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'  # noqa: E501

        :return: The path of this V1DownwardAPIVolumeFile.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this V1DownwardAPIVolumeFile.

        Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'  # noqa: E501

        :param path: The path of this V1DownwardAPIVolumeFile.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def resource_field_ref(self):
        """Gets the resource_field_ref of this V1DownwardAPIVolumeFile.  # noqa: E501


        :return: The resource_field_ref of this V1DownwardAPIVolumeFile.  # noqa: E501
        :rtype: V1ResourceFieldSelector
        """
        return self._resource_field_ref

    @resource_field_ref.setter
    def resource_field_ref(self, resource_field_ref):
        """Sets the resource_field_ref of this V1DownwardAPIVolumeFile.


        :param resource_field_ref: The resource_field_ref of this V1DownwardAPIVolumeFile.  # noqa: E501
        :type: V1ResourceFieldSelector
        """

        self._resource_field_ref = resource_field_ref

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1DownwardAPIVolumeFile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1DownwardAPIVolumeFile):
            return True

        return self.to_dict() != other.to_dict()
