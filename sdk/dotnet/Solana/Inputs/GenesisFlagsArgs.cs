// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ABKLabs.Svmkit.Solana.Inputs
{

    public sealed class GenesisFlagsArgs : global::Pulumi.ResourceArgs
    {
        [Input("clusterType")]
        public Input<string>? ClusterType { get; set; }

        [Input("faucetLamports")]
        public Input<string>? FaucetLamports { get; set; }

        [Input("faucetPubkey", required: true)]
        public Input<string> FaucetPubkey { get; set; } = null!;

        [Input("identityPubkey", required: true)]
        public Input<string> IdentityPubkey { get; set; } = null!;

        [Input("inflation")]
        public Input<string>? Inflation { get; set; }

        [Input("lamportsPerByteYear")]
        public Input<string>? LamportsPerByteYear { get; set; }

        [Input("ledgerPath", required: true)]
        public Input<string> LedgerPath { get; set; } = null!;

        [Input("slotPerEpoch")]
        public Input<string>? SlotPerEpoch { get; set; }

        [Input("stakePubkey", required: true)]
        public Input<string> StakePubkey { get; set; } = null!;

        [Input("targetLamportsPerSignature")]
        public Input<string>? TargetLamportsPerSignature { get; set; }

        [Input("votePubkey", required: true)]
        public Input<string> VotePubkey { get; set; } = null!;

        public GenesisFlagsArgs()
        {
        }
        public static new GenesisFlagsArgs Empty => new GenesisFlagsArgs();
    }
}
