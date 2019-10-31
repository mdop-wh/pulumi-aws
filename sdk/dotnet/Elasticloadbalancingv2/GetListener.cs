// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Elasticloadbalancingv2
{
    public static partial class Invokes
    {
        /// <summary>
        /// &gt; **Note:** `aws.alb.Listener` is known as `aws.lb.Listener`. The functionality is identical.
        /// 
        /// Provides information about a Load Balancer Listener.
        /// 
        /// This data source can prove useful when a module accepts an LB Listener as an
        /// input variable and needs to know the LB it is attached to, or other
        /// information specific to the listener in question.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/lb_listener_legacy.html.markdown.
        /// </summary>
        public static Task<GetListenerResult> GetListener(GetListenerArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetListenerResult>("aws:elasticloadbalancingv2/getListener:getListener", args, options.WithVersion());
    }

    public sealed class GetListenerArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The arn of the listener. Required if `load_balancer_arn` and `port` is not set.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// The arn of the load balancer. Required if `arn` is not set.
        /// </summary>
        [Input("loadBalancerArn")]
        public Input<string>? LoadBalancerArn { get; set; }

        /// <summary>
        /// The port of the listener. Required if `arn` is not set.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        public GetListenerArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetListenerResult
    {
        public readonly string Arn;
        public readonly string CertificateArn;
        public readonly ImmutableArray<Outputs.GetListenerDefaultActionsResult> DefaultActions;
        public readonly string LoadBalancerArn;
        public readonly int Port;
        public readonly string Protocol;
        public readonly string SslPolicy;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetListenerResult(
            string arn,
            string certificateArn,
            ImmutableArray<Outputs.GetListenerDefaultActionsResult> defaultActions,
            string loadBalancerArn,
            int port,
            string protocol,
            string sslPolicy,
            string id)
        {
            Arn = arn;
            CertificateArn = certificateArn;
            DefaultActions = defaultActions;
            LoadBalancerArn = loadBalancerArn;
            Port = port;
            Protocol = protocol;
            SslPolicy = sslPolicy;
            Id = id;
        }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetListenerDefaultActionsAuthenticateCognitosResult
    {
        public readonly ImmutableDictionary<string, object> AuthenticationRequestExtraParams;
        public readonly string OnUnauthenticatedRequest;
        public readonly string Scope;
        public readonly string SessionCookieName;
        public readonly int SessionTimeout;
        public readonly string UserPoolArn;
        public readonly string UserPoolClientId;
        public readonly string UserPoolDomain;

        [OutputConstructor]
        private GetListenerDefaultActionsAuthenticateCognitosResult(
            ImmutableDictionary<string, object> authenticationRequestExtraParams,
            string onUnauthenticatedRequest,
            string scope,
            string sessionCookieName,
            int sessionTimeout,
            string userPoolArn,
            string userPoolClientId,
            string userPoolDomain)
        {
            AuthenticationRequestExtraParams = authenticationRequestExtraParams;
            OnUnauthenticatedRequest = onUnauthenticatedRequest;
            Scope = scope;
            SessionCookieName = sessionCookieName;
            SessionTimeout = sessionTimeout;
            UserPoolArn = userPoolArn;
            UserPoolClientId = userPoolClientId;
            UserPoolDomain = userPoolDomain;
        }
    }

    [OutputType]
    public sealed class GetListenerDefaultActionsAuthenticateOidcsResult
    {
        public readonly ImmutableDictionary<string, object> AuthenticationRequestExtraParams;
        public readonly string AuthorizationEndpoint;
        public readonly string ClientId;
        public readonly string ClientSecret;
        public readonly string Issuer;
        public readonly string OnUnauthenticatedRequest;
        public readonly string Scope;
        public readonly string SessionCookieName;
        public readonly int SessionTimeout;
        public readonly string TokenEndpoint;
        public readonly string UserInfoEndpoint;

        [OutputConstructor]
        private GetListenerDefaultActionsAuthenticateOidcsResult(
            ImmutableDictionary<string, object> authenticationRequestExtraParams,
            string authorizationEndpoint,
            string clientId,
            string clientSecret,
            string issuer,
            string onUnauthenticatedRequest,
            string scope,
            string sessionCookieName,
            int sessionTimeout,
            string tokenEndpoint,
            string userInfoEndpoint)
        {
            AuthenticationRequestExtraParams = authenticationRequestExtraParams;
            AuthorizationEndpoint = authorizationEndpoint;
            ClientId = clientId;
            ClientSecret = clientSecret;
            Issuer = issuer;
            OnUnauthenticatedRequest = onUnauthenticatedRequest;
            Scope = scope;
            SessionCookieName = sessionCookieName;
            SessionTimeout = sessionTimeout;
            TokenEndpoint = tokenEndpoint;
            UserInfoEndpoint = userInfoEndpoint;
        }
    }

    [OutputType]
    public sealed class GetListenerDefaultActionsFixedResponsesResult
    {
        public readonly string ContentType;
        public readonly string MessageBody;
        public readonly string StatusCode;

        [OutputConstructor]
        private GetListenerDefaultActionsFixedResponsesResult(
            string contentType,
            string messageBody,
            string statusCode)
        {
            ContentType = contentType;
            MessageBody = messageBody;
            StatusCode = statusCode;
        }
    }

    [OutputType]
    public sealed class GetListenerDefaultActionsRedirectsResult
    {
        public readonly string Host;
        public readonly string Path;
        /// <summary>
        /// The port of the listener. Required if `arn` is not set.
        /// </summary>
        public readonly string Port;
        public readonly string Protocol;
        public readonly string Query;
        public readonly string StatusCode;

        [OutputConstructor]
        private GetListenerDefaultActionsRedirectsResult(
            string host,
            string path,
            string port,
            string protocol,
            string query,
            string statusCode)
        {
            Host = host;
            Path = path;
            Port = port;
            Protocol = protocol;
            Query = query;
            StatusCode = statusCode;
        }
    }

    [OutputType]
    public sealed class GetListenerDefaultActionsResult
    {
        public readonly ImmutableArray<GetListenerDefaultActionsAuthenticateCognitosResult> AuthenticateCognitos;
        public readonly ImmutableArray<GetListenerDefaultActionsAuthenticateOidcsResult> AuthenticateOidcs;
        public readonly ImmutableArray<GetListenerDefaultActionsFixedResponsesResult> FixedResponses;
        public readonly int Order;
        public readonly ImmutableArray<GetListenerDefaultActionsRedirectsResult> Redirects;
        public readonly string TargetGroupArn;
        public readonly string Type;

        [OutputConstructor]
        private GetListenerDefaultActionsResult(
            ImmutableArray<GetListenerDefaultActionsAuthenticateCognitosResult> authenticateCognitos,
            ImmutableArray<GetListenerDefaultActionsAuthenticateOidcsResult> authenticateOidcs,
            ImmutableArray<GetListenerDefaultActionsFixedResponsesResult> fixedResponses,
            int order,
            ImmutableArray<GetListenerDefaultActionsRedirectsResult> redirects,
            string targetGroupArn,
            string type)
        {
            AuthenticateCognitos = authenticateCognitos;
            AuthenticateOidcs = authenticateOidcs;
            FixedResponses = fixedResponses;
            Order = order;
            Redirects = redirects;
            TargetGroupArn = targetGroupArn;
            Type = type;
        }
    }
    }
}
