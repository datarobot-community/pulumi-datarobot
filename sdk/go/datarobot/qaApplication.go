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

// Q&A Application
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
//			exampleCustomModel, err := datarobot.NewCustomModel(ctx, "exampleCustomModel", &datarobot.CustomModelArgs{
//				Description:         pulumi.String("Description for the example custom model"),
//				TargetType:          pulumi.String("Binary"),
//				TargetName:          pulumi.String("my_label"),
//				BaseEnvironmentName: pulumi.String("[GenAI] Python 3.11 with Moderations"),
//				LocalFiles: pulumi.StringArray{
//					pulumi.String("example.py"),
//				},
//			})
//			if err != nil {
//				return err
//			}
//			exampleRegisteredModel, err := datarobot.NewRegisteredModel(ctx, "exampleRegisteredModel", &datarobot.RegisteredModelArgs{
//				CustomModelVersionId: exampleCustomModel.VersionId,
//				Description:          pulumi.String("Description for the example registered model"),
//			})
//			if err != nil {
//				return err
//			}
//			examplePredictionEnvironment, err := datarobot.NewPredictionEnvironment(ctx, "examplePredictionEnvironment", &datarobot.PredictionEnvironmentArgs{
//				Description: pulumi.String("Description for the example prediction environment"),
//				Platform:    pulumi.String("datarobotServerless"),
//			})
//			if err != nil {
//				return err
//			}
//			exampleDeployment, err := datarobot.NewDeployment(ctx, "exampleDeployment", &datarobot.DeploymentArgs{
//				Label:                    pulumi.String("An example deployment"),
//				PredictionEnvironmentId:  examplePredictionEnvironment.ID(),
//				RegisteredModelVersionId: exampleRegisteredModel.VersionId,
//			})
//			if err != nil {
//				return err
//			}
//			exampleQaApplication, err := datarobot.NewQaApplication(ctx, "exampleQaApplication", &datarobot.QaApplicationArgs{
//				DeploymentId:          exampleDeployment.ID(),
//				ExternalAccessEnabled: pulumi.Bool(true),
//				ExternalAccessRecipients: pulumi.StringArray{
//					pulumi.String("recipient@example.com"),
//				},
//			})
//			if err != nil {
//				return err
//			}
//			ctx.Export("datarobotQaApplicationId", exampleQaApplication.ID())
//			ctx.Export("datarobotQaApplicationSourceId", exampleQaApplication.SourceId)
//			ctx.Export("datarobotQaApplicationSourceVersionId", exampleQaApplication.SourceVersionId)
//			ctx.Export("datarobotQaApplicationUrl", exampleQaApplication.ApplicationUrl)
//			return nil
//		})
//	}
//
// ```
type QaApplication struct {
	pulumi.CustomResourceState

	// The URL of the Q&A Application.
	ApplicationUrl pulumi.StringOutput `pulumi:"applicationUrl"`
	// The deployment ID of the Q&A Application.
	DeploymentId pulumi.StringOutput `pulumi:"deploymentId"`
	// Whether external access is enabled for the Q&A Application.
	ExternalAccessEnabled pulumi.BoolOutput `pulumi:"externalAccessEnabled"`
	// The list of external email addresses that have access to the Q&A Application.
	ExternalAccessRecipients pulumi.StringArrayOutput `pulumi:"externalAccessRecipients"`
	// The name of the Q&A Application.
	Name pulumi.StringOutput `pulumi:"name"`
	// The ID of the Q&A Application Source.
	SourceId pulumi.StringOutput `pulumi:"sourceId"`
	// The version ID of the Q&A Application Source.
	SourceVersionId pulumi.StringOutput `pulumi:"sourceVersionId"`
}

// NewQaApplication registers a new resource with the given unique name, arguments, and options.
func NewQaApplication(ctx *pulumi.Context,
	name string, args *QaApplicationArgs, opts ...pulumi.ResourceOption) (*QaApplication, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DeploymentId == nil {
		return nil, errors.New("invalid value for required argument 'DeploymentId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource QaApplication
	err := ctx.RegisterResource("datarobot:index/qaApplication:QaApplication", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetQaApplication gets an existing QaApplication resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetQaApplication(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *QaApplicationState, opts ...pulumi.ResourceOption) (*QaApplication, error) {
	var resource QaApplication
	err := ctx.ReadResource("datarobot:index/qaApplication:QaApplication", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering QaApplication resources.
type qaApplicationState struct {
	// The URL of the Q&A Application.
	ApplicationUrl *string `pulumi:"applicationUrl"`
	// The deployment ID of the Q&A Application.
	DeploymentId *string `pulumi:"deploymentId"`
	// Whether external access is enabled for the Q&A Application.
	ExternalAccessEnabled *bool `pulumi:"externalAccessEnabled"`
	// The list of external email addresses that have access to the Q&A Application.
	ExternalAccessRecipients []string `pulumi:"externalAccessRecipients"`
	// The name of the Q&A Application.
	Name *string `pulumi:"name"`
	// The ID of the Q&A Application Source.
	SourceId *string `pulumi:"sourceId"`
	// The version ID of the Q&A Application Source.
	SourceVersionId *string `pulumi:"sourceVersionId"`
}

type QaApplicationState struct {
	// The URL of the Q&A Application.
	ApplicationUrl pulumi.StringPtrInput
	// The deployment ID of the Q&A Application.
	DeploymentId pulumi.StringPtrInput
	// Whether external access is enabled for the Q&A Application.
	ExternalAccessEnabled pulumi.BoolPtrInput
	// The list of external email addresses that have access to the Q&A Application.
	ExternalAccessRecipients pulumi.StringArrayInput
	// The name of the Q&A Application.
	Name pulumi.StringPtrInput
	// The ID of the Q&A Application Source.
	SourceId pulumi.StringPtrInput
	// The version ID of the Q&A Application Source.
	SourceVersionId pulumi.StringPtrInput
}

func (QaApplicationState) ElementType() reflect.Type {
	return reflect.TypeOf((*qaApplicationState)(nil)).Elem()
}

type qaApplicationArgs struct {
	// The deployment ID of the Q&A Application.
	DeploymentId string `pulumi:"deploymentId"`
	// Whether external access is enabled for the Q&A Application.
	ExternalAccessEnabled *bool `pulumi:"externalAccessEnabled"`
	// The list of external email addresses that have access to the Q&A Application.
	ExternalAccessRecipients []string `pulumi:"externalAccessRecipients"`
	// The name of the Q&A Application.
	Name *string `pulumi:"name"`
}

// The set of arguments for constructing a QaApplication resource.
type QaApplicationArgs struct {
	// The deployment ID of the Q&A Application.
	DeploymentId pulumi.StringInput
	// Whether external access is enabled for the Q&A Application.
	ExternalAccessEnabled pulumi.BoolPtrInput
	// The list of external email addresses that have access to the Q&A Application.
	ExternalAccessRecipients pulumi.StringArrayInput
	// The name of the Q&A Application.
	Name pulumi.StringPtrInput
}

func (QaApplicationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*qaApplicationArgs)(nil)).Elem()
}

type QaApplicationInput interface {
	pulumi.Input

	ToQaApplicationOutput() QaApplicationOutput
	ToQaApplicationOutputWithContext(ctx context.Context) QaApplicationOutput
}

func (*QaApplication) ElementType() reflect.Type {
	return reflect.TypeOf((**QaApplication)(nil)).Elem()
}

func (i *QaApplication) ToQaApplicationOutput() QaApplicationOutput {
	return i.ToQaApplicationOutputWithContext(context.Background())
}

func (i *QaApplication) ToQaApplicationOutputWithContext(ctx context.Context) QaApplicationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(QaApplicationOutput)
}

// QaApplicationArrayInput is an input type that accepts QaApplicationArray and QaApplicationArrayOutput values.
// You can construct a concrete instance of `QaApplicationArrayInput` via:
//
//	QaApplicationArray{ QaApplicationArgs{...} }
type QaApplicationArrayInput interface {
	pulumi.Input

	ToQaApplicationArrayOutput() QaApplicationArrayOutput
	ToQaApplicationArrayOutputWithContext(context.Context) QaApplicationArrayOutput
}

type QaApplicationArray []QaApplicationInput

func (QaApplicationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*QaApplication)(nil)).Elem()
}

func (i QaApplicationArray) ToQaApplicationArrayOutput() QaApplicationArrayOutput {
	return i.ToQaApplicationArrayOutputWithContext(context.Background())
}

func (i QaApplicationArray) ToQaApplicationArrayOutputWithContext(ctx context.Context) QaApplicationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(QaApplicationArrayOutput)
}

// QaApplicationMapInput is an input type that accepts QaApplicationMap and QaApplicationMapOutput values.
// You can construct a concrete instance of `QaApplicationMapInput` via:
//
//	QaApplicationMap{ "key": QaApplicationArgs{...} }
type QaApplicationMapInput interface {
	pulumi.Input

	ToQaApplicationMapOutput() QaApplicationMapOutput
	ToQaApplicationMapOutputWithContext(context.Context) QaApplicationMapOutput
}

type QaApplicationMap map[string]QaApplicationInput

func (QaApplicationMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*QaApplication)(nil)).Elem()
}

func (i QaApplicationMap) ToQaApplicationMapOutput() QaApplicationMapOutput {
	return i.ToQaApplicationMapOutputWithContext(context.Background())
}

func (i QaApplicationMap) ToQaApplicationMapOutputWithContext(ctx context.Context) QaApplicationMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(QaApplicationMapOutput)
}

type QaApplicationOutput struct{ *pulumi.OutputState }

func (QaApplicationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**QaApplication)(nil)).Elem()
}

func (o QaApplicationOutput) ToQaApplicationOutput() QaApplicationOutput {
	return o
}

func (o QaApplicationOutput) ToQaApplicationOutputWithContext(ctx context.Context) QaApplicationOutput {
	return o
}

// The URL of the Q&A Application.
func (o QaApplicationOutput) ApplicationUrl() pulumi.StringOutput {
	return o.ApplyT(func(v *QaApplication) pulumi.StringOutput { return v.ApplicationUrl }).(pulumi.StringOutput)
}

// The deployment ID of the Q&A Application.
func (o QaApplicationOutput) DeploymentId() pulumi.StringOutput {
	return o.ApplyT(func(v *QaApplication) pulumi.StringOutput { return v.DeploymentId }).(pulumi.StringOutput)
}

// Whether external access is enabled for the Q&A Application.
func (o QaApplicationOutput) ExternalAccessEnabled() pulumi.BoolOutput {
	return o.ApplyT(func(v *QaApplication) pulumi.BoolOutput { return v.ExternalAccessEnabled }).(pulumi.BoolOutput)
}

// The list of external email addresses that have access to the Q&A Application.
func (o QaApplicationOutput) ExternalAccessRecipients() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *QaApplication) pulumi.StringArrayOutput { return v.ExternalAccessRecipients }).(pulumi.StringArrayOutput)
}

// The name of the Q&A Application.
func (o QaApplicationOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *QaApplication) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The ID of the Q&A Application Source.
func (o QaApplicationOutput) SourceId() pulumi.StringOutput {
	return o.ApplyT(func(v *QaApplication) pulumi.StringOutput { return v.SourceId }).(pulumi.StringOutput)
}

// The version ID of the Q&A Application Source.
func (o QaApplicationOutput) SourceVersionId() pulumi.StringOutput {
	return o.ApplyT(func(v *QaApplication) pulumi.StringOutput { return v.SourceVersionId }).(pulumi.StringOutput)
}

type QaApplicationArrayOutput struct{ *pulumi.OutputState }

func (QaApplicationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*QaApplication)(nil)).Elem()
}

func (o QaApplicationArrayOutput) ToQaApplicationArrayOutput() QaApplicationArrayOutput {
	return o
}

func (o QaApplicationArrayOutput) ToQaApplicationArrayOutputWithContext(ctx context.Context) QaApplicationArrayOutput {
	return o
}

func (o QaApplicationArrayOutput) Index(i pulumi.IntInput) QaApplicationOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *QaApplication {
		return vs[0].([]*QaApplication)[vs[1].(int)]
	}).(QaApplicationOutput)
}

type QaApplicationMapOutput struct{ *pulumi.OutputState }

func (QaApplicationMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*QaApplication)(nil)).Elem()
}

func (o QaApplicationMapOutput) ToQaApplicationMapOutput() QaApplicationMapOutput {
	return o
}

func (o QaApplicationMapOutput) ToQaApplicationMapOutputWithContext(ctx context.Context) QaApplicationMapOutput {
	return o
}

func (o QaApplicationMapOutput) MapIndex(k pulumi.StringInput) QaApplicationOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *QaApplication {
		return vs[0].(map[string]*QaApplication)[vs[1].(string)]
	}).(QaApplicationOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*QaApplicationInput)(nil)).Elem(), &QaApplication{})
	pulumi.RegisterInputType(reflect.TypeOf((*QaApplicationArrayInput)(nil)).Elem(), QaApplicationArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*QaApplicationMapInput)(nil)).Elem(), QaApplicationMap{})
	pulumi.RegisterOutputType(QaApplicationOutput{})
	pulumi.RegisterOutputType(QaApplicationArrayOutput{})
	pulumi.RegisterOutputType(QaApplicationMapOutput{})
}
