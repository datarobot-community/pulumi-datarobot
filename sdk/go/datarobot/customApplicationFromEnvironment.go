// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package datarobot

import (
	"context"
	"reflect"

	"errors"
	"github.com/datarobot-community/pulumi-datarobot/sdk/go/datarobot/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Custom Application created from an Execution Environment.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/datarobot-community/pulumi-datarobot/sdk/go/datarobot"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			example, err := datarobot.NewCustomApplicationFromEnvironment(ctx, "example", &datarobot.CustomApplicationFromEnvironmentArgs{
//				EnvironmentId:         pulumi.String("6542cd582a9d3d51bf4ac71e"),
//				ExternalAccessEnabled: pulumi.Bool(true),
//				ExternalAccessRecipients: pulumi.StringArray{
//					pulumi.String("recipient@example.com"),
//				},
//				AllowAutoStopping: pulumi.Bool(false),
//			})
//			if err != nil {
//				return err
//			}
//			ctx.Export("datarobotCustomApplicationId", example.ID())
//			ctx.Export("datarobotCustomApplicationUrl", example.ApplicationUrl)
//			return nil
//		})
//	}
//
// ```
type CustomApplicationFromEnvironment struct {
	pulumi.CustomResourceState

	// Whether auto stopping is allowed for the Custom Application.
	AllowAutoStopping pulumi.BoolOutput `pulumi:"allowAutoStopping"`
	// The URL of the Custom Application.
	ApplicationUrl pulumi.StringOutput `pulumi:"applicationUrl"`
	// The ID of the Execution Environment used to create the Custom Application.
	EnvironmentId pulumi.StringOutput `pulumi:"environmentId"`
	// The version ID of the Execution Environment used to create the Custom Application.
	EnvironmentVersionId pulumi.StringOutput `pulumi:"environmentVersionId"`
	// Whether external access is enabled for the Custom Application.
	ExternalAccessEnabled pulumi.BoolOutput `pulumi:"externalAccessEnabled"`
	// The list of external email addresses that have access to the Custom Application.
	ExternalAccessRecipients pulumi.StringArrayOutput `pulumi:"externalAccessRecipients"`
	// The name of the Custom Application.
	Name pulumi.StringOutput `pulumi:"name"`
	// The list of Use Case IDs to add the Custom Application to.
	UseCaseIds pulumi.StringArrayOutput `pulumi:"useCaseIds"`
}

// NewCustomApplicationFromEnvironment registers a new resource with the given unique name, arguments, and options.
func NewCustomApplicationFromEnvironment(ctx *pulumi.Context,
	name string, args *CustomApplicationFromEnvironmentArgs, opts ...pulumi.ResourceOption) (*CustomApplicationFromEnvironment, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.EnvironmentId == nil {
		return nil, errors.New("invalid value for required argument 'EnvironmentId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource CustomApplicationFromEnvironment
	err := ctx.RegisterResource("datarobot:index/customApplicationFromEnvironment:CustomApplicationFromEnvironment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCustomApplicationFromEnvironment gets an existing CustomApplicationFromEnvironment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCustomApplicationFromEnvironment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CustomApplicationFromEnvironmentState, opts ...pulumi.ResourceOption) (*CustomApplicationFromEnvironment, error) {
	var resource CustomApplicationFromEnvironment
	err := ctx.ReadResource("datarobot:index/customApplicationFromEnvironment:CustomApplicationFromEnvironment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CustomApplicationFromEnvironment resources.
type customApplicationFromEnvironmentState struct {
	// Whether auto stopping is allowed for the Custom Application.
	AllowAutoStopping *bool `pulumi:"allowAutoStopping"`
	// The URL of the Custom Application.
	ApplicationUrl *string `pulumi:"applicationUrl"`
	// The ID of the Execution Environment used to create the Custom Application.
	EnvironmentId *string `pulumi:"environmentId"`
	// The version ID of the Execution Environment used to create the Custom Application.
	EnvironmentVersionId *string `pulumi:"environmentVersionId"`
	// Whether external access is enabled for the Custom Application.
	ExternalAccessEnabled *bool `pulumi:"externalAccessEnabled"`
	// The list of external email addresses that have access to the Custom Application.
	ExternalAccessRecipients []string `pulumi:"externalAccessRecipients"`
	// The name of the Custom Application.
	Name *string `pulumi:"name"`
	// The list of Use Case IDs to add the Custom Application to.
	UseCaseIds []string `pulumi:"useCaseIds"`
}

type CustomApplicationFromEnvironmentState struct {
	// Whether auto stopping is allowed for the Custom Application.
	AllowAutoStopping pulumi.BoolPtrInput
	// The URL of the Custom Application.
	ApplicationUrl pulumi.StringPtrInput
	// The ID of the Execution Environment used to create the Custom Application.
	EnvironmentId pulumi.StringPtrInput
	// The version ID of the Execution Environment used to create the Custom Application.
	EnvironmentVersionId pulumi.StringPtrInput
	// Whether external access is enabled for the Custom Application.
	ExternalAccessEnabled pulumi.BoolPtrInput
	// The list of external email addresses that have access to the Custom Application.
	ExternalAccessRecipients pulumi.StringArrayInput
	// The name of the Custom Application.
	Name pulumi.StringPtrInput
	// The list of Use Case IDs to add the Custom Application to.
	UseCaseIds pulumi.StringArrayInput
}

func (CustomApplicationFromEnvironmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*customApplicationFromEnvironmentState)(nil)).Elem()
}

type customApplicationFromEnvironmentArgs struct {
	// Whether auto stopping is allowed for the Custom Application.
	AllowAutoStopping *bool `pulumi:"allowAutoStopping"`
	// The ID of the Execution Environment used to create the Custom Application.
	EnvironmentId string `pulumi:"environmentId"`
	// Whether external access is enabled for the Custom Application.
	ExternalAccessEnabled *bool `pulumi:"externalAccessEnabled"`
	// The list of external email addresses that have access to the Custom Application.
	ExternalAccessRecipients []string `pulumi:"externalAccessRecipients"`
	// The name of the Custom Application.
	Name *string `pulumi:"name"`
	// The list of Use Case IDs to add the Custom Application to.
	UseCaseIds []string `pulumi:"useCaseIds"`
}

// The set of arguments for constructing a CustomApplicationFromEnvironment resource.
type CustomApplicationFromEnvironmentArgs struct {
	// Whether auto stopping is allowed for the Custom Application.
	AllowAutoStopping pulumi.BoolPtrInput
	// The ID of the Execution Environment used to create the Custom Application.
	EnvironmentId pulumi.StringInput
	// Whether external access is enabled for the Custom Application.
	ExternalAccessEnabled pulumi.BoolPtrInput
	// The list of external email addresses that have access to the Custom Application.
	ExternalAccessRecipients pulumi.StringArrayInput
	// The name of the Custom Application.
	Name pulumi.StringPtrInput
	// The list of Use Case IDs to add the Custom Application to.
	UseCaseIds pulumi.StringArrayInput
}

func (CustomApplicationFromEnvironmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*customApplicationFromEnvironmentArgs)(nil)).Elem()
}

type CustomApplicationFromEnvironmentInput interface {
	pulumi.Input

	ToCustomApplicationFromEnvironmentOutput() CustomApplicationFromEnvironmentOutput
	ToCustomApplicationFromEnvironmentOutputWithContext(ctx context.Context) CustomApplicationFromEnvironmentOutput
}

func (*CustomApplicationFromEnvironment) ElementType() reflect.Type {
	return reflect.TypeOf((**CustomApplicationFromEnvironment)(nil)).Elem()
}

func (i *CustomApplicationFromEnvironment) ToCustomApplicationFromEnvironmentOutput() CustomApplicationFromEnvironmentOutput {
	return i.ToCustomApplicationFromEnvironmentOutputWithContext(context.Background())
}

func (i *CustomApplicationFromEnvironment) ToCustomApplicationFromEnvironmentOutputWithContext(ctx context.Context) CustomApplicationFromEnvironmentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CustomApplicationFromEnvironmentOutput)
}

// CustomApplicationFromEnvironmentArrayInput is an input type that accepts CustomApplicationFromEnvironmentArray and CustomApplicationFromEnvironmentArrayOutput values.
// You can construct a concrete instance of `CustomApplicationFromEnvironmentArrayInput` via:
//
//	CustomApplicationFromEnvironmentArray{ CustomApplicationFromEnvironmentArgs{...} }
type CustomApplicationFromEnvironmentArrayInput interface {
	pulumi.Input

	ToCustomApplicationFromEnvironmentArrayOutput() CustomApplicationFromEnvironmentArrayOutput
	ToCustomApplicationFromEnvironmentArrayOutputWithContext(context.Context) CustomApplicationFromEnvironmentArrayOutput
}

type CustomApplicationFromEnvironmentArray []CustomApplicationFromEnvironmentInput

func (CustomApplicationFromEnvironmentArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*CustomApplicationFromEnvironment)(nil)).Elem()
}

func (i CustomApplicationFromEnvironmentArray) ToCustomApplicationFromEnvironmentArrayOutput() CustomApplicationFromEnvironmentArrayOutput {
	return i.ToCustomApplicationFromEnvironmentArrayOutputWithContext(context.Background())
}

func (i CustomApplicationFromEnvironmentArray) ToCustomApplicationFromEnvironmentArrayOutputWithContext(ctx context.Context) CustomApplicationFromEnvironmentArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CustomApplicationFromEnvironmentArrayOutput)
}

// CustomApplicationFromEnvironmentMapInput is an input type that accepts CustomApplicationFromEnvironmentMap and CustomApplicationFromEnvironmentMapOutput values.
// You can construct a concrete instance of `CustomApplicationFromEnvironmentMapInput` via:
//
//	CustomApplicationFromEnvironmentMap{ "key": CustomApplicationFromEnvironmentArgs{...} }
type CustomApplicationFromEnvironmentMapInput interface {
	pulumi.Input

	ToCustomApplicationFromEnvironmentMapOutput() CustomApplicationFromEnvironmentMapOutput
	ToCustomApplicationFromEnvironmentMapOutputWithContext(context.Context) CustomApplicationFromEnvironmentMapOutput
}

type CustomApplicationFromEnvironmentMap map[string]CustomApplicationFromEnvironmentInput

func (CustomApplicationFromEnvironmentMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*CustomApplicationFromEnvironment)(nil)).Elem()
}

func (i CustomApplicationFromEnvironmentMap) ToCustomApplicationFromEnvironmentMapOutput() CustomApplicationFromEnvironmentMapOutput {
	return i.ToCustomApplicationFromEnvironmentMapOutputWithContext(context.Background())
}

func (i CustomApplicationFromEnvironmentMap) ToCustomApplicationFromEnvironmentMapOutputWithContext(ctx context.Context) CustomApplicationFromEnvironmentMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CustomApplicationFromEnvironmentMapOutput)
}

type CustomApplicationFromEnvironmentOutput struct{ *pulumi.OutputState }

func (CustomApplicationFromEnvironmentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**CustomApplicationFromEnvironment)(nil)).Elem()
}

func (o CustomApplicationFromEnvironmentOutput) ToCustomApplicationFromEnvironmentOutput() CustomApplicationFromEnvironmentOutput {
	return o
}

func (o CustomApplicationFromEnvironmentOutput) ToCustomApplicationFromEnvironmentOutputWithContext(ctx context.Context) CustomApplicationFromEnvironmentOutput {
	return o
}

// Whether auto stopping is allowed for the Custom Application.
func (o CustomApplicationFromEnvironmentOutput) AllowAutoStopping() pulumi.BoolOutput {
	return o.ApplyT(func(v *CustomApplicationFromEnvironment) pulumi.BoolOutput { return v.AllowAutoStopping }).(pulumi.BoolOutput)
}

// The URL of the Custom Application.
func (o CustomApplicationFromEnvironmentOutput) ApplicationUrl() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomApplicationFromEnvironment) pulumi.StringOutput { return v.ApplicationUrl }).(pulumi.StringOutput)
}

// The ID of the Execution Environment used to create the Custom Application.
func (o CustomApplicationFromEnvironmentOutput) EnvironmentId() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomApplicationFromEnvironment) pulumi.StringOutput { return v.EnvironmentId }).(pulumi.StringOutput)
}

// The version ID of the Execution Environment used to create the Custom Application.
func (o CustomApplicationFromEnvironmentOutput) EnvironmentVersionId() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomApplicationFromEnvironment) pulumi.StringOutput { return v.EnvironmentVersionId }).(pulumi.StringOutput)
}

// Whether external access is enabled for the Custom Application.
func (o CustomApplicationFromEnvironmentOutput) ExternalAccessEnabled() pulumi.BoolOutput {
	return o.ApplyT(func(v *CustomApplicationFromEnvironment) pulumi.BoolOutput { return v.ExternalAccessEnabled }).(pulumi.BoolOutput)
}

// The list of external email addresses that have access to the Custom Application.
func (o CustomApplicationFromEnvironmentOutput) ExternalAccessRecipients() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *CustomApplicationFromEnvironment) pulumi.StringArrayOutput { return v.ExternalAccessRecipients }).(pulumi.StringArrayOutput)
}

// The name of the Custom Application.
func (o CustomApplicationFromEnvironmentOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomApplicationFromEnvironment) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The list of Use Case IDs to add the Custom Application to.
func (o CustomApplicationFromEnvironmentOutput) UseCaseIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *CustomApplicationFromEnvironment) pulumi.StringArrayOutput { return v.UseCaseIds }).(pulumi.StringArrayOutput)
}

type CustomApplicationFromEnvironmentArrayOutput struct{ *pulumi.OutputState }

func (CustomApplicationFromEnvironmentArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*CustomApplicationFromEnvironment)(nil)).Elem()
}

func (o CustomApplicationFromEnvironmentArrayOutput) ToCustomApplicationFromEnvironmentArrayOutput() CustomApplicationFromEnvironmentArrayOutput {
	return o
}

func (o CustomApplicationFromEnvironmentArrayOutput) ToCustomApplicationFromEnvironmentArrayOutputWithContext(ctx context.Context) CustomApplicationFromEnvironmentArrayOutput {
	return o
}

func (o CustomApplicationFromEnvironmentArrayOutput) Index(i pulumi.IntInput) CustomApplicationFromEnvironmentOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *CustomApplicationFromEnvironment {
		return vs[0].([]*CustomApplicationFromEnvironment)[vs[1].(int)]
	}).(CustomApplicationFromEnvironmentOutput)
}

type CustomApplicationFromEnvironmentMapOutput struct{ *pulumi.OutputState }

func (CustomApplicationFromEnvironmentMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*CustomApplicationFromEnvironment)(nil)).Elem()
}

func (o CustomApplicationFromEnvironmentMapOutput) ToCustomApplicationFromEnvironmentMapOutput() CustomApplicationFromEnvironmentMapOutput {
	return o
}

func (o CustomApplicationFromEnvironmentMapOutput) ToCustomApplicationFromEnvironmentMapOutputWithContext(ctx context.Context) CustomApplicationFromEnvironmentMapOutput {
	return o
}

func (o CustomApplicationFromEnvironmentMapOutput) MapIndex(k pulumi.StringInput) CustomApplicationFromEnvironmentOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *CustomApplicationFromEnvironment {
		return vs[0].(map[string]*CustomApplicationFromEnvironment)[vs[1].(string)]
	}).(CustomApplicationFromEnvironmentOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CustomApplicationFromEnvironmentInput)(nil)).Elem(), &CustomApplicationFromEnvironment{})
	pulumi.RegisterInputType(reflect.TypeOf((*CustomApplicationFromEnvironmentArrayInput)(nil)).Elem(), CustomApplicationFromEnvironmentArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*CustomApplicationFromEnvironmentMapInput)(nil)).Elem(), CustomApplicationFromEnvironmentMap{})
	pulumi.RegisterOutputType(CustomApplicationFromEnvironmentOutput{})
	pulumi.RegisterOutputType(CustomApplicationFromEnvironmentArrayOutput{})
	pulumi.RegisterOutputType(CustomApplicationFromEnvironmentMapOutput{})
}
