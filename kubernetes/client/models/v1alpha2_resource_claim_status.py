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


class V1alpha2ResourceClaimStatus(object):
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
        'allocation': 'V1alpha2AllocationResult',
        'deallocation_requested': 'bool',
        'driver_name': 'str',
        'reserved_for': 'list[V1alpha2ResourceClaimConsumerReference]'
    }

    attribute_map = {
        'allocation': 'allocation',
        'deallocation_requested': 'deallocationRequested',
        'driver_name': 'driverName',
        'reserved_for': 'reservedFor'
    }

    def __init__(self, allocation=None, deallocation_requested=None, driver_name=None, reserved_for=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha2ResourceClaimStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._allocation = None
        self._deallocation_requested = None
        self._driver_name = None
        self._reserved_for = None
        self.discriminator = None

        if allocation is not None:
            self.allocation = allocation
        if deallocation_requested is not None:
            self.deallocation_requested = deallocation_requested
        if driver_name is not None:
            self.driver_name = driver_name
        if reserved_for is not None:
            self.reserved_for = reserved_for

    @property
    def allocation(self):
        """Gets the allocation of this V1alpha2ResourceClaimStatus.  # noqa: E501


        :return: The allocation of this V1alpha2ResourceClaimStatus.  # noqa: E501
        :rtype: V1alpha2AllocationResult
        """
        return self._allocation

    @allocation.setter
    def allocation(self, allocation):
        """Sets the allocation of this V1alpha2ResourceClaimStatus.


        :param allocation: The allocation of this V1alpha2ResourceClaimStatus.  # noqa: E501
        :type: V1alpha2AllocationResult
        """

        self._allocation = allocation

    @property
    def deallocation_requested(self):
        """Gets the deallocation_requested of this V1alpha2ResourceClaimStatus.  # noqa: E501

        DeallocationRequested indicates that a ResourceClaim is to be deallocated.  The driver then must deallocate this claim and reset the field together with clearing the Allocation field.  While DeallocationRequested is set, no new consumers may be added to ReservedFor.  # noqa: E501

        :return: The deallocation_requested of this V1alpha2ResourceClaimStatus.  # noqa: E501
        :rtype: bool
        """
        return self._deallocation_requested

    @deallocation_requested.setter
    def deallocation_requested(self, deallocation_requested):
        """Sets the deallocation_requested of this V1alpha2ResourceClaimStatus.

        DeallocationRequested indicates that a ResourceClaim is to be deallocated.  The driver then must deallocate this claim and reset the field together with clearing the Allocation field.  While DeallocationRequested is set, no new consumers may be added to ReservedFor.  # noqa: E501

        :param deallocation_requested: The deallocation_requested of this V1alpha2ResourceClaimStatus.  # noqa: E501
        :type: bool
        """

        self._deallocation_requested = deallocation_requested

    @property
    def driver_name(self):
        """Gets the driver_name of this V1alpha2ResourceClaimStatus.  # noqa: E501

        DriverName is a copy of the driver name from the ResourceClass at the time when allocation started.  # noqa: E501

        :return: The driver_name of this V1alpha2ResourceClaimStatus.  # noqa: E501
        :rtype: str
        """
        return self._driver_name

    @driver_name.setter
    def driver_name(self, driver_name):
        """Sets the driver_name of this V1alpha2ResourceClaimStatus.

        DriverName is a copy of the driver name from the ResourceClass at the time when allocation started.  # noqa: E501

        :param driver_name: The driver_name of this V1alpha2ResourceClaimStatus.  # noqa: E501
        :type: str
        """

        self._driver_name = driver_name

    @property
    def reserved_for(self):
        """Gets the reserved_for of this V1alpha2ResourceClaimStatus.  # noqa: E501

        ReservedFor indicates which entities are currently allowed to use the claim. A Pod which references a ResourceClaim which is not reserved for that Pod will not be started.  There can be at most 32 such reservations. This may get increased in the future, but not reduced.  # noqa: E501

        :return: The reserved_for of this V1alpha2ResourceClaimStatus.  # noqa: E501
        :rtype: list[V1alpha2ResourceClaimConsumerReference]
        """
        return self._reserved_for

    @reserved_for.setter
    def reserved_for(self, reserved_for):
        """Sets the reserved_for of this V1alpha2ResourceClaimStatus.

        ReservedFor indicates which entities are currently allowed to use the claim. A Pod which references a ResourceClaim which is not reserved for that Pod will not be started.  There can be at most 32 such reservations. This may get increased in the future, but not reduced.  # noqa: E501

        :param reserved_for: The reserved_for of this V1alpha2ResourceClaimStatus.  # noqa: E501
        :type: list[V1alpha2ResourceClaimConsumerReference]
        """

        self._reserved_for = reserved_for

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
        if not isinstance(other, V1alpha2ResourceClaimStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha2ResourceClaimStatus):
            return True

        return self.to_dict() != other.to_dict()
