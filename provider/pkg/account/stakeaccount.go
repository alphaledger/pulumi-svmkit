package account

import (
	"context"

	"github.com/abklabs/pulumi-svmkit/pkg/svm"
	"github.com/abklabs/pulumi-svmkit/pkg/utils"
	"github.com/abklabs/svmkit/pkg/solana"
)

type StakeAccount struct{}

type StakeAccountArgs struct {
	svm.ValidatorArgs
	solana.StakeAccount
}

type StakeAccountState struct {
	StakeAccountArgs
}

func (StakeAccount) Create(ctx context.Context, name string, input StakeAccountArgs, preview bool) (string, StakeAccountState, error) {
	state := StakeAccountState{StakeAccountArgs: input}

	if preview {
		return name, state, nil
	}

	client := input.StakeAccount

	command := client.Create()

	if err := utils.RunnerHelper(ctx, input.Connection, command); err != nil {
		return "", StakeAccountState{}, err
	}

	return name, state, nil
}

func (StakeAccount) Update(ctx context.Context, name string, old StakeAccountState, new StakeAccountArgs, preview bool) (StakeAccountState, error) {
	if preview {
		return StakeAccountState{StakeAccountArgs: new}, nil
	}

	old.StakeAccountArgs = new

	return old, nil
}