// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package account

import (
	"fmt"

	"github.com/abklabs/pulumi-svmkit/sdk/go/internal"
	"github.com/blang/semver"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "svmkit:account:StakeAccount":
		r = &StakeAccount{}
	case "svmkit:account:Transfer":
		r = &Transfer{}
	case "svmkit:account:VoteAccount":
		r = &VoteAccount{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

func init() {
	version, err := internal.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"svmkit",
		"account",
		&module{version},
	)
}