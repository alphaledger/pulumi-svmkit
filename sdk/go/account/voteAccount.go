// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package account

import (
	"context"
	"reflect"

	"errors"
	"github.com/abklabs/pulumi-svmkit/sdk/go/internal"
	"github.com/abklabs/pulumi-svmkit/sdk/go/solana"
	"github.com/abklabs/pulumi-svmkit/sdk/go/ssh"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type VoteAccount struct {
	pulumi.CustomResourceState

	AuthVoterPubkey      pulumi.StringPtrOutput           `pulumi:"authVoterPubkey"`
	CloseRecipientPubkey pulumi.StringPtrOutput           `pulumi:"closeRecipientPubkey"`
	Connection           ssh.ConnectionOutput             `pulumi:"connection"`
	KeyPairs             solana.VoteAccountKeyPairsOutput `pulumi:"keyPairs"`
}

// NewVoteAccount registers a new resource with the given unique name, arguments, and options.
func NewVoteAccount(ctx *pulumi.Context,
	name string, args *VoteAccountArgs, opts ...pulumi.ResourceOption) (*VoteAccount, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Connection == nil {
		return nil, errors.New("invalid value for required argument 'Connection'")
	}
	if args.KeyPairs == nil {
		return nil, errors.New("invalid value for required argument 'KeyPairs'")
	}
	args.Connection = args.Connection.ToConnectionOutput().ApplyT(func(v ssh.Connection) ssh.Connection { return *v.Defaults() }).(ssh.ConnectionOutput)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource VoteAccount
	err := ctx.RegisterResource("svmkit:account:VoteAccount", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVoteAccount gets an existing VoteAccount resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVoteAccount(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VoteAccountState, opts ...pulumi.ResourceOption) (*VoteAccount, error) {
	var resource VoteAccount
	err := ctx.ReadResource("svmkit:account:VoteAccount", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VoteAccount resources.
type voteAccountState struct {
}

type VoteAccountState struct {
}

func (VoteAccountState) ElementType() reflect.Type {
	return reflect.TypeOf((*voteAccountState)(nil)).Elem()
}

type voteAccountArgs struct {
	AuthVoterPubkey      *string                    `pulumi:"authVoterPubkey"`
	CloseRecipientPubkey *string                    `pulumi:"closeRecipientPubkey"`
	Connection           ssh.Connection             `pulumi:"connection"`
	KeyPairs             solana.VoteAccountKeyPairs `pulumi:"keyPairs"`
}

// The set of arguments for constructing a VoteAccount resource.
type VoteAccountArgs struct {
	AuthVoterPubkey      pulumi.StringPtrInput
	CloseRecipientPubkey pulumi.StringPtrInput
	Connection           ssh.ConnectionInput
	KeyPairs             solana.VoteAccountKeyPairsInput
}

func (VoteAccountArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*voteAccountArgs)(nil)).Elem()
}

type VoteAccountInput interface {
	pulumi.Input

	ToVoteAccountOutput() VoteAccountOutput
	ToVoteAccountOutputWithContext(ctx context.Context) VoteAccountOutput
}

func (*VoteAccount) ElementType() reflect.Type {
	return reflect.TypeOf((**VoteAccount)(nil)).Elem()
}

func (i *VoteAccount) ToVoteAccountOutput() VoteAccountOutput {
	return i.ToVoteAccountOutputWithContext(context.Background())
}

func (i *VoteAccount) ToVoteAccountOutputWithContext(ctx context.Context) VoteAccountOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VoteAccountOutput)
}

type VoteAccountOutput struct{ *pulumi.OutputState }

func (VoteAccountOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**VoteAccount)(nil)).Elem()
}

func (o VoteAccountOutput) ToVoteAccountOutput() VoteAccountOutput {
	return o
}

func (o VoteAccountOutput) ToVoteAccountOutputWithContext(ctx context.Context) VoteAccountOutput {
	return o
}

func (o VoteAccountOutput) AuthVoterPubkey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VoteAccount) pulumi.StringPtrOutput { return v.AuthVoterPubkey }).(pulumi.StringPtrOutput)
}

func (o VoteAccountOutput) CloseRecipientPubkey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VoteAccount) pulumi.StringPtrOutput { return v.CloseRecipientPubkey }).(pulumi.StringPtrOutput)
}

func (o VoteAccountOutput) Connection() ssh.ConnectionOutput {
	return o.ApplyT(func(v *VoteAccount) ssh.ConnectionOutput { return v.Connection }).(ssh.ConnectionOutput)
}

func (o VoteAccountOutput) KeyPairs() solana.VoteAccountKeyPairsOutput {
	return o.ApplyT(func(v *VoteAccount) solana.VoteAccountKeyPairsOutput { return v.KeyPairs }).(solana.VoteAccountKeyPairsOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VoteAccountInput)(nil)).Elem(), &VoteAccount{})
	pulumi.RegisterOutputType(VoteAccountOutput{})
}
