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


class V1EndpointConditions(object):
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
        'ready': 'bool',
        'serving': 'bool',
        'terminating': 'bool'
    }

    attribute_map = {
        'ready': 'ready',
        'serving': 'serving',
        'terminating': 'terminating'
    }

    def __init__(self, ready=None, serving=None, terminating=None, local_vars_configuration=None):  # noqa: E501
        """V1EndpointConditions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ready = None
        self._serving = None
        self._terminating = None
        self.discriminator = None

        if ready is not None:
            self.ready = ready
        if serving is not None:
            self.serving = serving
        if terminating is not None:
            self.terminating = terminating

    @property
    def ready(self):
        """Gets the ready of this V1EndpointConditions.  # noqa: E501

        ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should interpret this unknown state as ready. For compatibility reasons, ready should never be \"true\" for terminating endpoints, except when the normal readiness behavior is being explicitly overridden, for example when the associated Service has set the publishNotReadyAddresses flag.  # noqa: E501

        :return: The ready of this V1EndpointConditions.  # noqa: E501
        :rtype: bool
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        """Sets the ready of this V1EndpointConditions.

        ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should interpret this unknown state as ready. For compatibility reasons, ready should never be \"true\" for terminating endpoints, except when the normal readiness behavior is being explicitly overridden, for example when the associated Service has set the publishNotReadyAddresses flag.  # noqa: E501

        :param ready: The ready of this V1EndpointConditions.  # noqa: E501
        :type: bool
        """

        self._ready = ready

    @property
    def serving(self):
        """Gets the serving of this V1EndpointConditions.  # noqa: E501

        serving is identical to ready except that it is set regardless of the terminating state of endpoints. This condition should be set to true for a ready endpoint that is terminating. If nil, consumers should defer to the ready condition.  # noqa: E501

        :return: The serving of this V1EndpointConditions.  # noqa: E501
        :rtype: bool
        """
        return self._serving

    @serving.setter
    def serving(self, serving):
        """Sets the serving of this V1EndpointConditions.

        serving is identical to ready except that it is set regardless of the terminating state of endpoints. This condition should be set to true for a ready endpoint that is terminating. If nil, consumers should defer to the ready condition.  # noqa: E501

        :param serving: The serving of this V1EndpointConditions.  # noqa: E501
        :type: bool
        """

        self._serving = serving

    @property
    def terminating(self):
        """Gets the terminating of this V1EndpointConditions.  # noqa: E501

        terminating indicates that this endpoint is terminating. A nil value indicates an unknown state. Consumers should interpret this unknown state to mean that the endpoint is not terminating.  # noqa: E501

        :return: The terminating of this V1EndpointConditions.  # noqa: E501
        :rtype: bool
        """
        return self._terminating

    @terminating.setter
    def terminating(self, terminating):
        """Sets the terminating of this V1EndpointConditions.

        terminating indicates that this endpoint is terminating. A nil value indicates an unknown state. Consumers should interpret this unknown state to mean that the endpoint is not terminating.  # noqa: E501

        :param terminating: The terminating of this V1EndpointConditions.  # noqa: E501
        :type: bool
        """

        self._terminating = terminating

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
        if not isinstance(other, V1EndpointConditions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1EndpointConditions):
            return True

        return self.to_dict() != other.to_dict()
