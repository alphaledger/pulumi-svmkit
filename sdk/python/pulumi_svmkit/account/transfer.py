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
from .. import ssh as _ssh

__all__ = ['TransferArgs', 'Transfer']

@pulumi.input_type
class TransferArgs:
    def __init__(__self__, *,
                 amount: pulumi.Input[float],
                 connection: pulumi.Input['_ssh.ConnectionArgs'],
                 payer_key_pair: pulumi.Input[str],
                 recipient_pubkey: pulumi.Input[str],
                 allow_unfunded_recipient: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Transfer resource.
        """
        pulumi.set(__self__, "amount", amount)
        pulumi.set(__self__, "connection", connection)
        pulumi.set(__self__, "payer_key_pair", payer_key_pair)
        pulumi.set(__self__, "recipient_pubkey", recipient_pubkey)
        if allow_unfunded_recipient is not None:
            pulumi.set(__self__, "allow_unfunded_recipient", allow_unfunded_recipient)

    @property
    @pulumi.getter
    def amount(self) -> pulumi.Input[float]:
        return pulumi.get(self, "amount")

    @amount.setter
    def amount(self, value: pulumi.Input[float]):
        pulumi.set(self, "amount", value)

    @property
    @pulumi.getter
    def connection(self) -> pulumi.Input['_ssh.ConnectionArgs']:
        return pulumi.get(self, "connection")

    @connection.setter
    def connection(self, value: pulumi.Input['_ssh.ConnectionArgs']):
        pulumi.set(self, "connection", value)

    @property
    @pulumi.getter(name="payerKeyPair")
    def payer_key_pair(self) -> pulumi.Input[str]:
        return pulumi.get(self, "payer_key_pair")

    @payer_key_pair.setter
    def payer_key_pair(self, value: pulumi.Input[str]):
        pulumi.set(self, "payer_key_pair", value)

    @property
    @pulumi.getter(name="recipientPubkey")
    def recipient_pubkey(self) -> pulumi.Input[str]:
        return pulumi.get(self, "recipient_pubkey")

    @recipient_pubkey.setter
    def recipient_pubkey(self, value: pulumi.Input[str]):
        pulumi.set(self, "recipient_pubkey", value)

    @property
    @pulumi.getter(name="allowUnfundedRecipient")
    def allow_unfunded_recipient(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "allow_unfunded_recipient")

    @allow_unfunded_recipient.setter
    def allow_unfunded_recipient(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_unfunded_recipient", value)


class Transfer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_unfunded_recipient: Optional[pulumi.Input[bool]] = None,
                 amount: Optional[pulumi.Input[float]] = None,
                 connection: Optional[pulumi.Input[Union['_ssh.ConnectionArgs', '_ssh.ConnectionArgsDict']]] = None,
                 payer_key_pair: Optional[pulumi.Input[str]] = None,
                 recipient_pubkey: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Transfer resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TransferArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Transfer resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param TransferArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TransferArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_unfunded_recipient: Optional[pulumi.Input[bool]] = None,
                 amount: Optional[pulumi.Input[float]] = None,
                 connection: Optional[pulumi.Input[Union['_ssh.ConnectionArgs', '_ssh.ConnectionArgsDict']]] = None,
                 payer_key_pair: Optional[pulumi.Input[str]] = None,
                 recipient_pubkey: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TransferArgs.__new__(TransferArgs)

            __props__.__dict__["allow_unfunded_recipient"] = allow_unfunded_recipient
            if amount is None and not opts.urn:
                raise TypeError("Missing required property 'amount'")
            __props__.__dict__["amount"] = amount
            if connection is None and not opts.urn:
                raise TypeError("Missing required property 'connection'")
            __props__.__dict__["connection"] = connection
            if payer_key_pair is None and not opts.urn:
                raise TypeError("Missing required property 'payer_key_pair'")
            __props__.__dict__["payer_key_pair"] = None if payer_key_pair is None else pulumi.Output.secret(payer_key_pair)
            if recipient_pubkey is None and not opts.urn:
                raise TypeError("Missing required property 'recipient_pubkey'")
            __props__.__dict__["recipient_pubkey"] = recipient_pubkey
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["payerKeyPair"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Transfer, __self__).__init__(
            'svmkit:account:Transfer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Transfer':
        """
        Get an existing Transfer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TransferArgs.__new__(TransferArgs)

        __props__.__dict__["allow_unfunded_recipient"] = None
        __props__.__dict__["amount"] = None
        __props__.__dict__["connection"] = None
        __props__.__dict__["payer_key_pair"] = None
        __props__.__dict__["recipient_pubkey"] = None
        return Transfer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowUnfundedRecipient")
    def allow_unfunded_recipient(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "allow_unfunded_recipient")

    @property
    @pulumi.getter
    def amount(self) -> pulumi.Output[float]:
        return pulumi.get(self, "amount")

    @property
    @pulumi.getter
    def connection(self) -> pulumi.Output['_ssh.outputs.Connection']:
        return pulumi.get(self, "connection")

    @property
    @pulumi.getter(name="payerKeyPair")
    def payer_key_pair(self) -> pulumi.Output[str]:
        return pulumi.get(self, "payer_key_pair")

    @property
    @pulumi.getter(name="recipientPubkey")
    def recipient_pubkey(self) -> pulumi.Output[str]:
        return pulumi.get(self, "recipient_pubkey")

