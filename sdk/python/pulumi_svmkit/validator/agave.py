# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities
from .. import agave as _agave
from .. import ssh as _ssh

__all__ = ['AgaveArgs', 'Agave']

@pulumi.input_type
class AgaveArgs:
    def __init__(__self__, *,
                 connection: pulumi.Input['_ssh.ConnectionArgs'],
                 flags: pulumi.Input['_agave.FlagsArgs'],
                 key_pairs: pulumi.Input['_agave.KeyPairsArgs'],
                 version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Agave resource.
        """
        pulumi.set(__self__, "connection", connection)
        pulumi.set(__self__, "flags", flags)
        pulumi.set(__self__, "key_pairs", key_pairs)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def connection(self) -> pulumi.Input['_ssh.ConnectionArgs']:
        return pulumi.get(self, "connection")

    @connection.setter
    def connection(self, value: pulumi.Input['_ssh.ConnectionArgs']):
        pulumi.set(self, "connection", value)

    @property
    @pulumi.getter
    def flags(self) -> pulumi.Input['_agave.FlagsArgs']:
        return pulumi.get(self, "flags")

    @flags.setter
    def flags(self, value: pulumi.Input['_agave.FlagsArgs']):
        pulumi.set(self, "flags", value)

    @property
    @pulumi.getter(name="keyPairs")
    def key_pairs(self) -> pulumi.Input['_agave.KeyPairsArgs']:
        return pulumi.get(self, "key_pairs")

    @key_pairs.setter
    def key_pairs(self, value: pulumi.Input['_agave.KeyPairsArgs']):
        pulumi.set(self, "key_pairs", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class Agave(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection: Optional[pulumi.Input[Union['_ssh.ConnectionArgs', '_ssh.ConnectionArgsDict']]] = None,
                 flags: Optional[pulumi.Input[Union['_agave.FlagsArgs', '_agave.FlagsArgsDict']]] = None,
                 key_pairs: Optional[pulumi.Input[Union['_agave.KeyPairsArgs', '_agave.KeyPairsArgsDict']]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Agave resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AgaveArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Agave resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AgaveArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AgaveArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection: Optional[pulumi.Input[Union['_ssh.ConnectionArgs', '_ssh.ConnectionArgsDict']]] = None,
                 flags: Optional[pulumi.Input[Union['_agave.FlagsArgs', '_agave.FlagsArgsDict']]] = None,
                 key_pairs: Optional[pulumi.Input[Union['_agave.KeyPairsArgs', '_agave.KeyPairsArgsDict']]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AgaveArgs.__new__(AgaveArgs)

            if connection is None and not opts.urn:
                raise TypeError("Missing required property 'connection'")
            __props__.__dict__["connection"] = connection
            if flags is None and not opts.urn:
                raise TypeError("Missing required property 'flags'")
            __props__.__dict__["flags"] = flags
            if key_pairs is None and not opts.urn:
                raise TypeError("Missing required property 'key_pairs'")
            __props__.__dict__["key_pairs"] = key_pairs
            __props__.__dict__["version"] = version
        super(Agave, __self__).__init__(
            'svmkit:validator:Agave',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Agave':
        """
        Get an existing Agave resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AgaveArgs.__new__(AgaveArgs)

        __props__.__dict__["connection"] = None
        __props__.__dict__["flags"] = None
        __props__.__dict__["key_pairs"] = None
        __props__.__dict__["version"] = None
        return Agave(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def connection(self) -> pulumi.Output['_ssh.outputs.Connection']:
        return pulumi.get(self, "connection")

    @property
    @pulumi.getter
    def flags(self) -> pulumi.Output['_agave.outputs.Flags']:
        return pulumi.get(self, "flags")

    @property
    @pulumi.getter(name="keyPairs")
    def key_pairs(self) -> pulumi.Output['_agave.outputs.KeyPairs']:
        return pulumi.get(self, "key_pairs")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "version")

