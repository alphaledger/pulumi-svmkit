// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ABKLabs.Svmkit.Agave.Inputs
{

    public sealed class ShutdownPolicyArgs : global::Pulumi.ResourceArgs
    {
        [Input("force")]
        public Input<bool>? Force { get; set; }

        [Input("maxDelinquentStake")]
        public Input<int>? MaxDelinquentStake { get; set; }

        [Input("minIdleTime")]
        public Input<int>? MinIdleTime { get; set; }

        [Input("skipHealthCheck")]
        public Input<bool>? SkipHealthCheck { get; set; }

        [Input("skipNewSnapshotCheck")]
        public Input<bool>? SkipNewSnapshotCheck { get; set; }

        public ShutdownPolicyArgs()
        {
        }
        public static new ShutdownPolicyArgs Empty => new ShutdownPolicyArgs();
    }
}
