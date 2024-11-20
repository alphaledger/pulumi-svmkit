// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";

import * as utilities from "../utilities";

export namespace agave {
    export interface FlagsArgs {
        allowPrivateAddr?: pulumi.Input<boolean>;
        blockProductionMethod: pulumi.Input<string>;
        dynamicPortRange: pulumi.Input<string>;
        entryPoint?: pulumi.Input<pulumi.Input<string>[]>;
        expectedGenesisHash?: pulumi.Input<string>;
        extraFlags?: pulumi.Input<pulumi.Input<string>[]>;
        fullRpcAPI?: pulumi.Input<boolean>;
        fullSnapshotIntervalSlots: pulumi.Input<number>;
        gossipHost?: pulumi.Input<string>;
        gossipPort: pulumi.Input<number>;
        knownValidator?: pulumi.Input<pulumi.Input<string>[]>;
        limitLedgerSize: pulumi.Input<number>;
        noVoting?: pulumi.Input<boolean>;
        noWaitForVoteToStartLeader: pulumi.Input<boolean>;
        onlyKnownRPC: pulumi.Input<boolean>;
        privateRPC: pulumi.Input<boolean>;
        rpcBindAddress: pulumi.Input<string>;
        rpcPort: pulumi.Input<number>;
        tvuReceiveThreads?: pulumi.Input<number>;
        useSnapshotArchivesAtStartup: pulumi.Input<string>;
        walRecoveryMode: pulumi.Input<string>;
    }

    export interface KeyPairsArgs {
        identity: pulumi.Input<string>;
        voteAccount: pulumi.Input<string>;
    }

    export interface MetricsArgs {
        database: pulumi.Input<string>;
        password: pulumi.Input<string>;
        url: pulumi.Input<string>;
        user: pulumi.Input<string>;
    }
}

export namespace genesis {
    export interface PrimorialEntryArgs {
        lamports: pulumi.Input<string>;
        pubkey: pulumi.Input<string>;
    }
}

export namespace solana {
    export interface EnvironmentArgs {
        rpcURL: pulumi.Input<string>;
    }

    export interface GenesisFlagsArgs {
        clusterType?: pulumi.Input<string>;
        faucetLamports?: pulumi.Input<string>;
        faucetPubkey: pulumi.Input<string>;
        identityPubkey: pulumi.Input<string>;
        inflation?: pulumi.Input<string>;
        lamportsPerByteYear?: pulumi.Input<string>;
        ledgerPath: pulumi.Input<string>;
        slotPerEpoch?: pulumi.Input<string>;
        stakePubkey: pulumi.Input<string>;
        targetLamportsPerSignature?: pulumi.Input<string>;
        votePubkey: pulumi.Input<string>;
    }

    export interface StakeAccountKeyPairsArgs {
        stakeAccount: pulumi.Input<string>;
        voteAccount: pulumi.Input<string>;
    }

    export interface VoteAccountKeyPairsArgs {
        authWithdrawer: pulumi.Input<string>;
        identity: pulumi.Input<string>;
        voteAccount: pulumi.Input<string>;
    }
}

export namespace ssh {
    /**
     * Instructions for how to connect to a remote endpoint.
     */
    export interface ConnectionArgs {
        /**
         * SSH Agent socket path. Default to environment variable SSH_AUTH_SOCK if present.
         */
        agentSocketPath?: pulumi.Input<string>;
        /**
         * Max allowed errors on trying to dial the remote host. -1 set count to unlimited. Default value is 10.
         */
        dialErrorLimit?: pulumi.Input<number>;
        /**
         * The address of the resource to connect to.
         */
        host: pulumi.Input<string>;
        /**
         * The password we should use for the connection.
         */
        password?: pulumi.Input<string>;
        /**
         * Max number of seconds for each dial attempt. 0 implies no maximum. Default value is 15 seconds.
         */
        perDialTimeout?: pulumi.Input<number>;
        /**
         * The port to connect to. Defaults to 22.
         */
        port?: pulumi.Input<number>;
        /**
         * The contents of an SSH key to use for the connection. This takes preference over the password if provided.
         */
        privateKey?: pulumi.Input<string>;
        /**
         * The password to use in case the private key is encrypted.
         */
        privateKeyPassword?: pulumi.Input<string>;
        /**
         * The connection settings for the bastion/proxy host.
         */
        proxy?: pulumi.Input<inputs.ssh.ProxyConnectionArgs>;
        /**
         * The user that we should use for the connection.
         */
        user?: pulumi.Input<string>;
    }
    /**
     * connectionArgsProvideDefaults sets the appropriate defaults for ConnectionArgs
     */
    export function connectionArgsProvideDefaults(val: ConnectionArgs): ConnectionArgs {
        return {
            ...val,
            dialErrorLimit: (val.dialErrorLimit) ?? 10,
            perDialTimeout: (val.perDialTimeout) ?? 15,
            port: (val.port) ?? 22,
            proxy: (val.proxy ? pulumi.output(val.proxy).apply(inputs.ssh.proxyConnectionArgsProvideDefaults) : undefined),
            user: (val.user) ?? "root",
        };
    }

    /**
     * Instructions for how to connect to a remote endpoint via a bastion host.
     */
    export interface ProxyConnectionArgs {
        /**
         * SSH Agent socket path. Default to environment variable SSH_AUTH_SOCK if present.
         */
        agentSocketPath?: pulumi.Input<string>;
        /**
         * Max allowed errors on trying to dial the remote host. -1 set count to unlimited. Default value is 10.
         */
        dialErrorLimit?: pulumi.Input<number>;
        /**
         * The address of the bastion host to connect to.
         */
        host: pulumi.Input<string>;
        /**
         * The password we should use for the connection to the bastion host.
         */
        password?: pulumi.Input<string>;
        /**
         * Max number of seconds for each dial attempt. 0 implies no maximum. Default value is 15 seconds.
         */
        perDialTimeout?: pulumi.Input<number>;
        /**
         * The port of the bastion host to connect to.
         */
        port?: pulumi.Input<number>;
        /**
         * The contents of an SSH key to use for the connection. This takes preference over the password if provided.
         */
        privateKey?: pulumi.Input<string>;
        /**
         * The password to use in case the private key is encrypted.
         */
        privateKeyPassword?: pulumi.Input<string>;
        /**
         * The user that we should use for the connection to the bastion host.
         */
        user?: pulumi.Input<string>;
    }
    /**
     * proxyConnectionArgsProvideDefaults sets the appropriate defaults for ProxyConnectionArgs
     */
    export function proxyConnectionArgsProvideDefaults(val: ProxyConnectionArgs): ProxyConnectionArgs {
        return {
            ...val,
            dialErrorLimit: (val.dialErrorLimit) ?? 10,
            perDialTimeout: (val.perDialTimeout) ?? 15,
            port: (val.port) ?? 22,
            user: (val.user) ?? "root",
        };
    }
}
