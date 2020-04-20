// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Ses.Outputs
{

    [OutputType]
    public sealed class ReceiptRuleBounceAction
    {
        /// <summary>
        /// The message to send
        /// </summary>
        public readonly string Message;
        /// <summary>
        /// The position of the action in the receipt rule
        /// </summary>
        public readonly int Position;
        /// <summary>
        /// The email address of the sender
        /// </summary>
        public readonly string Sender;
        /// <summary>
        /// The RFC 5321 SMTP reply code
        /// </summary>
        public readonly string SmtpReplyCode;
        /// <summary>
        /// The RFC 3463 SMTP enhanced status code
        /// </summary>
        public readonly string? StatusCode;
        /// <summary>
        /// The ARN of an SNS topic to notify
        /// </summary>
        public readonly string? TopicArn;

        [OutputConstructor]
        private ReceiptRuleBounceAction(
            string message,

            int position,

            string sender,

            string smtpReplyCode,

            string? statusCode,

            string? topicArn)
        {
            Message = message;
            Position = position;
            Sender = sender;
            SmtpReplyCode = smtpReplyCode;
            StatusCode = statusCode;
            TopicArn = topicArn;
        }
    }
}