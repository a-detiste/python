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


class V1CustomResourceDefinitionStatus(object):
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
        'accepted_names': 'V1CustomResourceDefinitionNames',
        'conditions': 'list[V1CustomResourceDefinitionCondition]',
        'stored_versions': 'list[str]'
    }

    attribute_map = {
        'accepted_names': 'acceptedNames',
        'conditions': 'conditions',
        'stored_versions': 'storedVersions'
    }

    def __init__(self, accepted_names=None, conditions=None, stored_versions=None, local_vars_configuration=None):  # noqa: E501
        """V1CustomResourceDefinitionStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._accepted_names = None
        self._conditions = None
        self._stored_versions = None
        self.discriminator = None

        if accepted_names is not None:
            self.accepted_names = accepted_names
        if conditions is not None:
            self.conditions = conditions
        if stored_versions is not None:
            self.stored_versions = stored_versions

    @property
    def accepted_names(self):
        """Gets the accepted_names of this V1CustomResourceDefinitionStatus.  # noqa: E501


        :return: The accepted_names of this V1CustomResourceDefinitionStatus.  # noqa: E501
        :rtype: V1CustomResourceDefinitionNames
        """
        return self._accepted_names

    @accepted_names.setter
    def accepted_names(self, accepted_names):
        """Sets the accepted_names of this V1CustomResourceDefinitionStatus.


        :param accepted_names: The accepted_names of this V1CustomResourceDefinitionStatus.  # noqa: E501
        :type: V1CustomResourceDefinitionNames
        """

        self._accepted_names = accepted_names

    @property
    def conditions(self):
        """Gets the conditions of this V1CustomResourceDefinitionStatus.  # noqa: E501

        conditions indicate state for particular aspects of a CustomResourceDefinition  # noqa: E501

        :return: The conditions of this V1CustomResourceDefinitionStatus.  # noqa: E501
        :rtype: list[V1CustomResourceDefinitionCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1CustomResourceDefinitionStatus.

        conditions indicate state for particular aspects of a CustomResourceDefinition  # noqa: E501

        :param conditions: The conditions of this V1CustomResourceDefinitionStatus.  # noqa: E501
        :type: list[V1CustomResourceDefinitionCondition]
        """

        self._conditions = conditions

    @property
    def stored_versions(self):
        """Gets the stored_versions of this V1CustomResourceDefinitionStatus.  # noqa: E501

        storedVersions lists all versions of CustomResources that were ever persisted. Tracking these versions allows a migration path for stored versions in etcd. The field is mutable so a migration controller can finish a migration to another version (ensuring no old objects are left in storage), and then remove the rest of the versions from this list. Versions may not be removed from `spec.versions` while they exist in this list.  # noqa: E501

        :return: The stored_versions of this V1CustomResourceDefinitionStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._stored_versions

    @stored_versions.setter
    def stored_versions(self, stored_versions):
        """Sets the stored_versions of this V1CustomResourceDefinitionStatus.

        storedVersions lists all versions of CustomResources that were ever persisted. Tracking these versions allows a migration path for stored versions in etcd. The field is mutable so a migration controller can finish a migration to another version (ensuring no old objects are left in storage), and then remove the rest of the versions from this list. Versions may not be removed from `spec.versions` while they exist in this list.  # noqa: E501

        :param stored_versions: The stored_versions of this V1CustomResourceDefinitionStatus.  # noqa: E501
        :type: list[str]
        """

        self._stored_versions = stored_versions

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
        if not isinstance(other, V1CustomResourceDefinitionStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1CustomResourceDefinitionStatus):
            return True

        return self.to_dict() != other.to_dict()
