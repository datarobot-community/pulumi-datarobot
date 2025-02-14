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

// Custom Application
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
//			exampleApplicationSource, err := datarobot.NewApplicationSource(ctx, "exampleApplicationSource", &datarobot.ApplicationSourceArgs{
//				Files: pulumi.Any{
//					[]string{
//						"start-app.sh",
//					},
//					[]string{
//						"streamlit-app.py",
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			exampleCustomApplication, err := datarobot.NewCustomApplication(ctx, "exampleCustomApplication", &datarobot.CustomApplicationArgs{
//				SourceVersionId:       exampleApplicationSource.VersionId,
//				ExternalAccessEnabled: pulumi.Bool(true),
//				ExternalAccessRecipients: pulumi.StringArray{
//					pulumi.String("recipient@example.com"),
//				},
//				AllowAutoStopping: pulumi.Bool(false),
//			})
//			if err != nil {
//				return err
//			}
//			ctx.Export("datarobotCustomApplicationId", exampleCustomApplication.ID())
//			ctx.Export("datarobotCustomApplicationSourceId", exampleCustomApplication.SourceId)
//			ctx.Export("datarobotCustomApplicationSourceVersionId", exampleCustomApplication.SourceVersionId)
//			ctx.Export("datarobotCustomApplicationUrl", exampleCustomApplication.ApplicationUrl)
//			return nil
//		})
//	}
//
// ```
type CustomApplication struct {
	pulumi.CustomResourceState

	// Whether auto stopping is allowed for the Custom Application.
	AllowAutoStopping pulumi.BoolOutput `pulumi:"allowAutoStopping"`
	// The URL of the Custom Application.
	ApplicationUrl pulumi.StringOutput `pulumi:"applicationUrl"`
	// Whether external access is enabled for the Custom Application.
	ExternalAccessEnabled pulumi.BoolOutput `pulumi:"externalAccessEnabled"`
	// The list of external email addresses that have access to the Custom Application.
	ExternalAccessRecipients pulumi.StringArrayOutput `pulumi:"externalAccessRecipients"`
	// The name of the Custom Application.
	Name pulumi.StringOutput `pulumi:"name"`
	// The ID of the Custom Application Source.
	SourceId pulumi.StringOutput `pulumi:"sourceId"`
	// The version ID of the Custom Application Source.
	SourceVersionId pulumi.StringOutput `pulumi:"sourceVersionId"`
	// The list of Use Case IDs to add the Custom Application to.
	UseCaseIds pulumi.StringArrayOutput `pulumi:"useCaseIds"`
}

// NewCustomApplication registers a new resource with the given unique name, arguments, and options.
func NewCustomApplication(ctx *pulumi.Context,
	name string, args *CustomApplicationArgs, opts ...pulumi.ResourceOption) (*CustomApplication, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.SourceVersionId == nil {
		return nil, errors.New("invalid value for required argument 'SourceVersionId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource CustomApplication
	err := ctx.RegisterResource("datarobot:index/customApplication:CustomApplication", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCustomApplication gets an existing CustomApplication resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCustomApplication(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CustomApplicationState, opts ...pulumi.ResourceOption) (*CustomApplication, error) {
	var resource CustomApplication
	err := ctx.ReadResource("datarobot:index/customApplication:CustomApplication", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CustomApplication resources.
type customApplicationState struct {
	// Whether auto stopping is allowed for the Custom Application.
	AllowAutoStopping *bool `pulumi:"allowAutoStopping"`
	// The URL of the Custom Application.
	ApplicationUrl *string `pulumi:"applicationUrl"`
	// Whether external access is enabled for the Custom Application.
	ExternalAccessEnabled *bool `pulumi:"externalAccessEnabled"`
	// The list of external email addresses that have access to the Custom Application.
	ExternalAccessRecipients []string `pulumi:"externalAccessRecipients"`
	// The name of the Custom Application.
	Name *string `pulumi:"name"`
	// The ID of the Custom Application Source.
	SourceId *string `pulumi:"sourceId"`
	// The version ID of the Custom Application Source.
	SourceVersionId *string `pulumi:"sourceVersionId"`
	// The list of Use Case IDs to add the Custom Application to.
	UseCaseIds []string `pulumi:"useCaseIds"`
}

type CustomApplicationState struct {
	// Whether auto stopping is allowed for the Custom Application.
	AllowAutoStopping pulumi.BoolPtrInput
	// The URL of the Custom Application.
	ApplicationUrl pulumi.StringPtrInput
	// Whether external access is enabled for the Custom Application.
	ExternalAccessEnabled pulumi.BoolPtrInput
	// The list of external email addresses that have access to the Custom Application.
	ExternalAccessRecipients pulumi.StringArrayInput
	// The name of the Custom Application.
	Name pulumi.StringPtrInput
	// The ID of the Custom Application Source.
	SourceId pulumi.StringPtrInput
	// The version ID of the Custom Application Source.
	SourceVersionId pulumi.StringPtrInput
	// The list of Use Case IDs to add the Custom Application to.
	UseCaseIds pulumi.StringArrayInput
}

func (CustomApplicationState) ElementType() reflect.Type {
	return reflect.TypeOf((*customApplicationState)(nil)).Elem()
}

type customApplicationArgs struct {
	// Whether auto stopping is allowed for the Custom Application.
	AllowAutoStopping *bool `pulumi:"allowAutoStopping"`
	// Whether external access is enabled for the Custom Application.
	ExternalAccessEnabled *bool `pulumi:"externalAccessEnabled"`
	// The list of external email addresses that have access to the Custom Application.
	ExternalAccessRecipients []string `pulumi:"externalAccessRecipients"`
	// The name of the Custom Application.
	Name *string `pulumi:"name"`
	// The version ID of the Custom Application Source.
	SourceVersionId string `pulumi:"sourceVersionId"`
	// The list of Use Case IDs to add the Custom Application to.
	UseCaseIds []string `pulumi:"useCaseIds"`
}

// The set of arguments for constructing a CustomApplication resource.
type CustomApplicationArgs struct {
	// Whether auto stopping is allowed for the Custom Application.
	AllowAutoStopping pulumi.BoolPtrInput
	// Whether external access is enabled for the Custom Application.
	ExternalAccessEnabled pulumi.BoolPtrInput
	// The list of external email addresses that have access to the Custom Application.
	ExternalAccessRecipients pulumi.StringArrayInput
	// The name of the Custom Application.
	Name pulumi.StringPtrInput
	// The version ID of the Custom Application Source.
	SourceVersionId pulumi.StringInput
	// The list of Use Case IDs to add the Custom Application to.
	UseCaseIds pulumi.StringArrayInput
}

func (CustomApplicationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*customApplicationArgs)(nil)).Elem()
}

type CustomApplicationInput interface {
	pulumi.Input

	ToCustomApplicationOutput() CustomApplicationOutput
	ToCustomApplicationOutputWithContext(ctx context.Context) CustomApplicationOutput
}

func (*CustomApplication) ElementType() reflect.Type {
	return reflect.TypeOf((**CustomApplication)(nil)).Elem()
}

func (i *CustomApplication) ToCustomApplicationOutput() CustomApplicationOutput {
	return i.ToCustomApplicationOutputWithContext(context.Background())
}

func (i *CustomApplication) ToCustomApplicationOutputWithContext(ctx context.Context) CustomApplicationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CustomApplicationOutput)
}

// CustomApplicationArrayInput is an input type that accepts CustomApplicationArray and CustomApplicationArrayOutput values.
// You can construct a concrete instance of `CustomApplicationArrayInput` via:
//
//	CustomApplicationArray{ CustomApplicationArgs{...} }
type CustomApplicationArrayInput interface {
	pulumi.Input

	ToCustomApplicationArrayOutput() CustomApplicationArrayOutput
	ToCustomApplicationArrayOutputWithContext(context.Context) CustomApplicationArrayOutput
}

type CustomApplicationArray []CustomApplicationInput

func (CustomApplicationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*CustomApplication)(nil)).Elem()
}

func (i CustomApplicationArray) ToCustomApplicationArrayOutput() CustomApplicationArrayOutput {
	return i.ToCustomApplicationArrayOutputWithContext(context.Background())
}

func (i CustomApplicationArray) ToCustomApplicationArrayOutputWithContext(ctx context.Context) CustomApplicationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CustomApplicationArrayOutput)
}

// CustomApplicationMapInput is an input type that accepts CustomApplicationMap and CustomApplicationMapOutput values.
// You can construct a concrete instance of `CustomApplicationMapInput` via:
//
//	CustomApplicationMap{ "key": CustomApplicationArgs{...} }
type CustomApplicationMapInput interface {
	pulumi.Input

	ToCustomApplicationMapOutput() CustomApplicationMapOutput
	ToCustomApplicationMapOutputWithContext(context.Context) CustomApplicationMapOutput
}

type CustomApplicationMap map[string]CustomApplicationInput

func (CustomApplicationMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*CustomApplication)(nil)).Elem()
}

func (i CustomApplicationMap) ToCustomApplicationMapOutput() CustomApplicationMapOutput {
	return i.ToCustomApplicationMapOutputWithContext(context.Background())
}

func (i CustomApplicationMap) ToCustomApplicationMapOutputWithContext(ctx context.Context) CustomApplicationMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CustomApplicationMapOutput)
}

type CustomApplicationOutput struct{ *pulumi.OutputState }

func (CustomApplicationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**CustomApplication)(nil)).Elem()
}

func (o CustomApplicationOutput) ToCustomApplicationOutput() CustomApplicationOutput {
	return o
}

func (o CustomApplicationOutput) ToCustomApplicationOutputWithContext(ctx context.Context) CustomApplicationOutput {
	return o
}

// Whether auto stopping is allowed for the Custom Application.
func (o CustomApplicationOutput) AllowAutoStopping() pulumi.BoolOutput {
	return o.ApplyT(func(v *CustomApplication) pulumi.BoolOutput { return v.AllowAutoStopping }).(pulumi.BoolOutput)
}

// The URL of the Custom Application.
func (o CustomApplicationOutput) ApplicationUrl() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomApplication) pulumi.StringOutput { return v.ApplicationUrl }).(pulumi.StringOutput)
}

// Whether external access is enabled for the Custom Application.
func (o CustomApplicationOutput) ExternalAccessEnabled() pulumi.BoolOutput {
	return o.ApplyT(func(v *CustomApplication) pulumi.BoolOutput { return v.ExternalAccessEnabled }).(pulumi.BoolOutput)
}

// The list of external email addresses that have access to the Custom Application.
func (o CustomApplicationOutput) ExternalAccessRecipients() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *CustomApplication) pulumi.StringArrayOutput { return v.ExternalAccessRecipients }).(pulumi.StringArrayOutput)
}

// The name of the Custom Application.
func (o CustomApplicationOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomApplication) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The ID of the Custom Application Source.
func (o CustomApplicationOutput) SourceId() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomApplication) pulumi.StringOutput { return v.SourceId }).(pulumi.StringOutput)
}

// The version ID of the Custom Application Source.
func (o CustomApplicationOutput) SourceVersionId() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomApplication) pulumi.StringOutput { return v.SourceVersionId }).(pulumi.StringOutput)
}

// The list of Use Case IDs to add the Custom Application to.
func (o CustomApplicationOutput) UseCaseIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *CustomApplication) pulumi.StringArrayOutput { return v.UseCaseIds }).(pulumi.StringArrayOutput)
}

type CustomApplicationArrayOutput struct{ *pulumi.OutputState }

func (CustomApplicationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*CustomApplication)(nil)).Elem()
}

func (o CustomApplicationArrayOutput) ToCustomApplicationArrayOutput() CustomApplicationArrayOutput {
	return o
}

func (o CustomApplicationArrayOutput) ToCustomApplicationArrayOutputWithContext(ctx context.Context) CustomApplicationArrayOutput {
	return o
}

func (o CustomApplicationArrayOutput) Index(i pulumi.IntInput) CustomApplicationOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *CustomApplication {
		return vs[0].([]*CustomApplication)[vs[1].(int)]
	}).(CustomApplicationOutput)
}

type CustomApplicationMapOutput struct{ *pulumi.OutputState }

func (CustomApplicationMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*CustomApplication)(nil)).Elem()
}

func (o CustomApplicationMapOutput) ToCustomApplicationMapOutput() CustomApplicationMapOutput {
	return o
}

func (o CustomApplicationMapOutput) ToCustomApplicationMapOutputWithContext(ctx context.Context) CustomApplicationMapOutput {
	return o
}

func (o CustomApplicationMapOutput) MapIndex(k pulumi.StringInput) CustomApplicationOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *CustomApplication {
		return vs[0].(map[string]*CustomApplication)[vs[1].(string)]
	}).(CustomApplicationOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CustomApplicationInput)(nil)).Elem(), &CustomApplication{})
	pulumi.RegisterInputType(reflect.TypeOf((*CustomApplicationArrayInput)(nil)).Elem(), CustomApplicationArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*CustomApplicationMapInput)(nil)).Elem(), CustomApplicationMap{})
	pulumi.RegisterOutputType(CustomApplicationOutput{})
	pulumi.RegisterOutputType(CustomApplicationArrayOutput{})
	pulumi.RegisterOutputType(CustomApplicationMapOutput{})
}
