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
from .. import solana as _solana
from .. import ssh as _ssh

__all__ = ['VoteAccountArgs', 'VoteAccount']

@pulumi.input_type
class VoteAccountArgs:
    def __init__(__self__, *,
                 connection: pulumi.Input['_ssh.ConnectionArgs'],
                 key_pairs: pulumi.Input['_solana.VoteAccountKeyPairsArgs'],
                 auth_voter_pubkey: Optional[pulumi.Input[str]] = None,
                 close_recipient_pubkey: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VoteAccount resource.
        """
        pulumi.set(__self__, "connection", connection)
        pulumi.set(__self__, "key_pairs", key_pairs)
        if auth_voter_pubkey is not None:
            pulumi.set(__self__, "auth_voter_pubkey", auth_voter_pubkey)
        if close_recipient_pubkey is not None:
            pulumi.set(__self__, "close_recipient_pubkey", close_recipient_pubkey)

    @property
    @pulumi.getter
    def connection(self) -> pulumi.Input['_ssh.ConnectionArgs']:
        return pulumi.get(self, "connection")

    @connection.setter
    def connection(self, value: pulumi.Input['_ssh.ConnectionArgs']):
        pulumi.set(self, "connection", value)

    @property
    @pulumi.getter(name="keyPairs")
    def key_pairs(self) -> pulumi.Input['_solana.VoteAccountKeyPairsArgs']:
        return pulumi.get(self, "key_pairs")

    @key_pairs.setter
    def key_pairs(self, value: pulumi.Input['_solana.VoteAccountKeyPairsArgs']):
        pulumi.set(self, "key_pairs", value)

    @property
    @pulumi.getter(name="authVoterPubkey")
    def auth_voter_pubkey(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "auth_voter_pubkey")

    @auth_voter_pubkey.setter
    def auth_voter_pubkey(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_voter_pubkey", value)

    @property
    @pulumi.getter(name="closeRecipientPubkey")
    def close_recipient_pubkey(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "close_recipient_pubkey")

    @close_recipient_pubkey.setter
    def close_recipient_pubkey(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "close_recipient_pubkey", value)


class VoteAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_voter_pubkey: Optional[pulumi.Input[str]] = None,
                 close_recipient_pubkey: Optional[pulumi.Input[str]] = None,
                 connection: Optional[pulumi.Input[Union['_ssh.ConnectionArgs', '_ssh.ConnectionArgsDict']]] = None,
                 key_pairs: Optional[pulumi.Input[Union['_solana.VoteAccountKeyPairsArgs', '_solana.VoteAccountKeyPairsArgsDict']]] = None,
                 __props__=None):
        """
        Create a VoteAccount resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VoteAccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a VoteAccount resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param VoteAccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VoteAccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_voter_pubkey: Optional[pulumi.Input[str]] = None,
                 close_recipient_pubkey: Optional[pulumi.Input[str]] = None,
                 connection: Optional[pulumi.Input[Union['_ssh.ConnectionArgs', '_ssh.ConnectionArgsDict']]] = None,
                 key_pairs: Optional[pulumi.Input[Union['_solana.VoteAccountKeyPairsArgs', '_solana.VoteAccountKeyPairsArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VoteAccountArgs.__new__(VoteAccountArgs)

            __props__.__dict__["auth_voter_pubkey"] = auth_voter_pubkey
            __props__.__dict__["close_recipient_pubkey"] = close_recipient_pubkey
            if connection is None and not opts.urn:
                raise TypeError("Missing required property 'connection'")
            __props__.__dict__["connection"] = connection
            if key_pairs is None and not opts.urn:
                raise TypeError("Missing required property 'key_pairs'")
            __props__.__dict__["key_pairs"] = key_pairs
        super(VoteAccount, __self__).__init__(
            'svmkit:account:VoteAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VoteAccount':
        """
        Get an existing VoteAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VoteAccountArgs.__new__(VoteAccountArgs)

        __props__.__dict__["auth_voter_pubkey"] = None
        __props__.__dict__["close_recipient_pubkey"] = None
        __props__.__dict__["connection"] = None
        __props__.__dict__["key_pairs"] = None
        return VoteAccount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authVoterPubkey")
    def auth_voter_pubkey(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "auth_voter_pubkey")

    @property
    @pulumi.getter(name="closeRecipientPubkey")
    def close_recipient_pubkey(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "close_recipient_pubkey")

    @property
    @pulumi.getter
    def connection(self) -> pulumi.Output['_ssh.outputs.Connection']:
        return pulumi.get(self, "connection")

    @property
    @pulumi.getter(name="keyPairs")
    def key_pairs(self) -> pulumi.Output['_solana.outputs.VoteAccountKeyPairs']:
        return pulumi.get(self, "key_pairs")
