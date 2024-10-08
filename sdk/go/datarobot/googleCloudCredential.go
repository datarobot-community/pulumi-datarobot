// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package datarobot

import (
	"context"
	"reflect"

	"github.com/datarobot-community/pulumi-datarobot/sdk/go/datarobot/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Api Token Credential
type GoogleCloudCredential struct {
	pulumi.CustomResourceState

	// The GCP key in JSON format.
	GcpKey pulumi.StringPtrOutput `pulumi:"gcpKey"`
	// The file that has the GCP key. Cannot be used with `gcpKey`.
	GcpKeyFile pulumi.StringPtrOutput `pulumi:"gcpKeyFile"`
	// The hash of the GCP key file contents.
	GcpKeyFileHash pulumi.StringOutput `pulumi:"gcpKeyFileHash"`
	// The name of the Google Cloud Credential.
	Name pulumi.StringOutput `pulumi:"name"`
}

// NewGoogleCloudCredential registers a new resource with the given unique name, arguments, and options.
func NewGoogleCloudCredential(ctx *pulumi.Context,
	name string, args *GoogleCloudCredentialArgs, opts ...pulumi.ResourceOption) (*GoogleCloudCredential, error) {
	if args == nil {
		args = &GoogleCloudCredentialArgs{}
	}

	if args.GcpKey != nil {
		args.GcpKey = pulumi.ToSecret(args.GcpKey).(pulumi.StringPtrInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"gcpKey",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource GoogleCloudCredential
	err := ctx.RegisterResource("datarobot:index/googleCloudCredential:GoogleCloudCredential", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetGoogleCloudCredential gets an existing GoogleCloudCredential resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGoogleCloudCredential(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *GoogleCloudCredentialState, opts ...pulumi.ResourceOption) (*GoogleCloudCredential, error) {
	var resource GoogleCloudCredential
	err := ctx.ReadResource("datarobot:index/googleCloudCredential:GoogleCloudCredential", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering GoogleCloudCredential resources.
type googleCloudCredentialState struct {
	// The GCP key in JSON format.
	GcpKey *string `pulumi:"gcpKey"`
	// The file that has the GCP key. Cannot be used with `gcpKey`.
	GcpKeyFile *string `pulumi:"gcpKeyFile"`
	// The hash of the GCP key file contents.
	GcpKeyFileHash *string `pulumi:"gcpKeyFileHash"`
	// The name of the Google Cloud Credential.
	Name *string `pulumi:"name"`
}

type GoogleCloudCredentialState struct {
	// The GCP key in JSON format.
	GcpKey pulumi.StringPtrInput
	// The file that has the GCP key. Cannot be used with `gcpKey`.
	GcpKeyFile pulumi.StringPtrInput
	// The hash of the GCP key file contents.
	GcpKeyFileHash pulumi.StringPtrInput
	// The name of the Google Cloud Credential.
	Name pulumi.StringPtrInput
}

func (GoogleCloudCredentialState) ElementType() reflect.Type {
	return reflect.TypeOf((*googleCloudCredentialState)(nil)).Elem()
}

type googleCloudCredentialArgs struct {
	// The GCP key in JSON format.
	GcpKey *string `pulumi:"gcpKey"`
	// The file that has the GCP key. Cannot be used with `gcpKey`.
	GcpKeyFile *string `pulumi:"gcpKeyFile"`
	// The name of the Google Cloud Credential.
	Name *string `pulumi:"name"`
}

// The set of arguments for constructing a GoogleCloudCredential resource.
type GoogleCloudCredentialArgs struct {
	// The GCP key in JSON format.
	GcpKey pulumi.StringPtrInput
	// The file that has the GCP key. Cannot be used with `gcpKey`.
	GcpKeyFile pulumi.StringPtrInput
	// The name of the Google Cloud Credential.
	Name pulumi.StringPtrInput
}

func (GoogleCloudCredentialArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*googleCloudCredentialArgs)(nil)).Elem()
}

type GoogleCloudCredentialInput interface {
	pulumi.Input

	ToGoogleCloudCredentialOutput() GoogleCloudCredentialOutput
	ToGoogleCloudCredentialOutputWithContext(ctx context.Context) GoogleCloudCredentialOutput
}

func (*GoogleCloudCredential) ElementType() reflect.Type {
	return reflect.TypeOf((**GoogleCloudCredential)(nil)).Elem()
}

func (i *GoogleCloudCredential) ToGoogleCloudCredentialOutput() GoogleCloudCredentialOutput {
	return i.ToGoogleCloudCredentialOutputWithContext(context.Background())
}

func (i *GoogleCloudCredential) ToGoogleCloudCredentialOutputWithContext(ctx context.Context) GoogleCloudCredentialOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GoogleCloudCredentialOutput)
}

// GoogleCloudCredentialArrayInput is an input type that accepts GoogleCloudCredentialArray and GoogleCloudCredentialArrayOutput values.
// You can construct a concrete instance of `GoogleCloudCredentialArrayInput` via:
//
//	GoogleCloudCredentialArray{ GoogleCloudCredentialArgs{...} }
type GoogleCloudCredentialArrayInput interface {
	pulumi.Input

	ToGoogleCloudCredentialArrayOutput() GoogleCloudCredentialArrayOutput
	ToGoogleCloudCredentialArrayOutputWithContext(context.Context) GoogleCloudCredentialArrayOutput
}

type GoogleCloudCredentialArray []GoogleCloudCredentialInput

func (GoogleCloudCredentialArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*GoogleCloudCredential)(nil)).Elem()
}

func (i GoogleCloudCredentialArray) ToGoogleCloudCredentialArrayOutput() GoogleCloudCredentialArrayOutput {
	return i.ToGoogleCloudCredentialArrayOutputWithContext(context.Background())
}

func (i GoogleCloudCredentialArray) ToGoogleCloudCredentialArrayOutputWithContext(ctx context.Context) GoogleCloudCredentialArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GoogleCloudCredentialArrayOutput)
}

// GoogleCloudCredentialMapInput is an input type that accepts GoogleCloudCredentialMap and GoogleCloudCredentialMapOutput values.
// You can construct a concrete instance of `GoogleCloudCredentialMapInput` via:
//
//	GoogleCloudCredentialMap{ "key": GoogleCloudCredentialArgs{...} }
type GoogleCloudCredentialMapInput interface {
	pulumi.Input

	ToGoogleCloudCredentialMapOutput() GoogleCloudCredentialMapOutput
	ToGoogleCloudCredentialMapOutputWithContext(context.Context) GoogleCloudCredentialMapOutput
}

type GoogleCloudCredentialMap map[string]GoogleCloudCredentialInput

func (GoogleCloudCredentialMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*GoogleCloudCredential)(nil)).Elem()
}

func (i GoogleCloudCredentialMap) ToGoogleCloudCredentialMapOutput() GoogleCloudCredentialMapOutput {
	return i.ToGoogleCloudCredentialMapOutputWithContext(context.Background())
}

func (i GoogleCloudCredentialMap) ToGoogleCloudCredentialMapOutputWithContext(ctx context.Context) GoogleCloudCredentialMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GoogleCloudCredentialMapOutput)
}

type GoogleCloudCredentialOutput struct{ *pulumi.OutputState }

func (GoogleCloudCredentialOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**GoogleCloudCredential)(nil)).Elem()
}

func (o GoogleCloudCredentialOutput) ToGoogleCloudCredentialOutput() GoogleCloudCredentialOutput {
	return o
}

func (o GoogleCloudCredentialOutput) ToGoogleCloudCredentialOutputWithContext(ctx context.Context) GoogleCloudCredentialOutput {
	return o
}

// The GCP key in JSON format.
func (o GoogleCloudCredentialOutput) GcpKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *GoogleCloudCredential) pulumi.StringPtrOutput { return v.GcpKey }).(pulumi.StringPtrOutput)
}

// The file that has the GCP key. Cannot be used with `gcpKey`.
func (o GoogleCloudCredentialOutput) GcpKeyFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *GoogleCloudCredential) pulumi.StringPtrOutput { return v.GcpKeyFile }).(pulumi.StringPtrOutput)
}

// The hash of the GCP key file contents.
func (o GoogleCloudCredentialOutput) GcpKeyFileHash() pulumi.StringOutput {
	return o.ApplyT(func(v *GoogleCloudCredential) pulumi.StringOutput { return v.GcpKeyFileHash }).(pulumi.StringOutput)
}

// The name of the Google Cloud Credential.
func (o GoogleCloudCredentialOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *GoogleCloudCredential) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

type GoogleCloudCredentialArrayOutput struct{ *pulumi.OutputState }

func (GoogleCloudCredentialArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*GoogleCloudCredential)(nil)).Elem()
}

func (o GoogleCloudCredentialArrayOutput) ToGoogleCloudCredentialArrayOutput() GoogleCloudCredentialArrayOutput {
	return o
}

func (o GoogleCloudCredentialArrayOutput) ToGoogleCloudCredentialArrayOutputWithContext(ctx context.Context) GoogleCloudCredentialArrayOutput {
	return o
}

func (o GoogleCloudCredentialArrayOutput) Index(i pulumi.IntInput) GoogleCloudCredentialOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *GoogleCloudCredential {
		return vs[0].([]*GoogleCloudCredential)[vs[1].(int)]
	}).(GoogleCloudCredentialOutput)
}

type GoogleCloudCredentialMapOutput struct{ *pulumi.OutputState }

func (GoogleCloudCredentialMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*GoogleCloudCredential)(nil)).Elem()
}

func (o GoogleCloudCredentialMapOutput) ToGoogleCloudCredentialMapOutput() GoogleCloudCredentialMapOutput {
	return o
}

func (o GoogleCloudCredentialMapOutput) ToGoogleCloudCredentialMapOutputWithContext(ctx context.Context) GoogleCloudCredentialMapOutput {
	return o
}

func (o GoogleCloudCredentialMapOutput) MapIndex(k pulumi.StringInput) GoogleCloudCredentialOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *GoogleCloudCredential {
		return vs[0].(map[string]*GoogleCloudCredential)[vs[1].(string)]
	}).(GoogleCloudCredentialOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*GoogleCloudCredentialInput)(nil)).Elem(), &GoogleCloudCredential{})
	pulumi.RegisterInputType(reflect.TypeOf((*GoogleCloudCredentialArrayInput)(nil)).Elem(), GoogleCloudCredentialArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*GoogleCloudCredentialMapInput)(nil)).Elem(), GoogleCloudCredentialMap{})
	pulumi.RegisterOutputType(GoogleCloudCredentialOutput{})
	pulumi.RegisterOutputType(GoogleCloudCredentialArrayOutput{})
	pulumi.RegisterOutputType(GoogleCloudCredentialMapOutput{})
}
