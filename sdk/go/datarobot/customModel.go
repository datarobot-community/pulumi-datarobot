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

type CustomModel struct {
	pulumi.CustomResourceState

	// The ID of the base environment for the Custom Model.
	BaseEnvironmentId pulumi.StringOutput `pulumi:"baseEnvironmentId"`
	// The ID of the base environment version for the Custom Model.
	BaseEnvironmentVersionId pulumi.StringOutput `pulumi:"baseEnvironmentVersionId"`
	// The description of the Custom Model.
	Description pulumi.StringOutput `pulumi:"description"`
	// The name of the Custom Model.
	Name pulumi.StringOutput `pulumi:"name"`
	// The runtime parameter values for the Custom Model.
	RuntimeParameters CustomModelRuntimeParameterArrayOutput `pulumi:"runtimeParameters"`
	// The ID of the source LLM Blueprint for the Custom Model.
	SourceLlmBlueprintId pulumi.StringOutput `pulumi:"sourceLlmBlueprintId"`
	// The ID of the latest Custom Model version.
	VersionId pulumi.StringOutput `pulumi:"versionId"`
}

// NewCustomModel registers a new resource with the given unique name, arguments, and options.
func NewCustomModel(ctx *pulumi.Context,
	name string, args *CustomModelArgs, opts ...pulumi.ResourceOption) (*CustomModel, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Description == nil {
		return nil, errors.New("invalid value for required argument 'Description'")
	}
	if args.SourceLlmBlueprintId == nil {
		return nil, errors.New("invalid value for required argument 'SourceLlmBlueprintId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource CustomModel
	err := ctx.RegisterResource("datarobot:index/customModel:CustomModel", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCustomModel gets an existing CustomModel resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCustomModel(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CustomModelState, opts ...pulumi.ResourceOption) (*CustomModel, error) {
	var resource CustomModel
	err := ctx.ReadResource("datarobot:index/customModel:CustomModel", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CustomModel resources.
type customModelState struct {
	// The ID of the base environment for the Custom Model.
	BaseEnvironmentId *string `pulumi:"baseEnvironmentId"`
	// The ID of the base environment version for the Custom Model.
	BaseEnvironmentVersionId *string `pulumi:"baseEnvironmentVersionId"`
	// The description of the Custom Model.
	Description *string `pulumi:"description"`
	// The name of the Custom Model.
	Name *string `pulumi:"name"`
	// The runtime parameter values for the Custom Model.
	RuntimeParameters []CustomModelRuntimeParameter `pulumi:"runtimeParameters"`
	// The ID of the source LLM Blueprint for the Custom Model.
	SourceLlmBlueprintId *string `pulumi:"sourceLlmBlueprintId"`
	// The ID of the latest Custom Model version.
	VersionId *string `pulumi:"versionId"`
}

type CustomModelState struct {
	// The ID of the base environment for the Custom Model.
	BaseEnvironmentId pulumi.StringPtrInput
	// The ID of the base environment version for the Custom Model.
	BaseEnvironmentVersionId pulumi.StringPtrInput
	// The description of the Custom Model.
	Description pulumi.StringPtrInput
	// The name of the Custom Model.
	Name pulumi.StringPtrInput
	// The runtime parameter values for the Custom Model.
	RuntimeParameters CustomModelRuntimeParameterArrayInput
	// The ID of the source LLM Blueprint for the Custom Model.
	SourceLlmBlueprintId pulumi.StringPtrInput
	// The ID of the latest Custom Model version.
	VersionId pulumi.StringPtrInput
}

func (CustomModelState) ElementType() reflect.Type {
	return reflect.TypeOf((*customModelState)(nil)).Elem()
}

type customModelArgs struct {
	// The ID of the base environment for the Custom Model.
	BaseEnvironmentId *string `pulumi:"baseEnvironmentId"`
	// The ID of the base environment version for the Custom Model.
	BaseEnvironmentVersionId *string `pulumi:"baseEnvironmentVersionId"`
	// The description of the Custom Model.
	Description string `pulumi:"description"`
	// The name of the Custom Model.
	Name *string `pulumi:"name"`
	// The runtime parameter values for the Custom Model.
	RuntimeParameters []CustomModelRuntimeParameter `pulumi:"runtimeParameters"`
	// The ID of the source LLM Blueprint for the Custom Model.
	SourceLlmBlueprintId string `pulumi:"sourceLlmBlueprintId"`
}

// The set of arguments for constructing a CustomModel resource.
type CustomModelArgs struct {
	// The ID of the base environment for the Custom Model.
	BaseEnvironmentId pulumi.StringPtrInput
	// The ID of the base environment version for the Custom Model.
	BaseEnvironmentVersionId pulumi.StringPtrInput
	// The description of the Custom Model.
	Description pulumi.StringInput
	// The name of the Custom Model.
	Name pulumi.StringPtrInput
	// The runtime parameter values for the Custom Model.
	RuntimeParameters CustomModelRuntimeParameterArrayInput
	// The ID of the source LLM Blueprint for the Custom Model.
	SourceLlmBlueprintId pulumi.StringInput
}

func (CustomModelArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*customModelArgs)(nil)).Elem()
}

type CustomModelInput interface {
	pulumi.Input

	ToCustomModelOutput() CustomModelOutput
	ToCustomModelOutputWithContext(ctx context.Context) CustomModelOutput
}

func (*CustomModel) ElementType() reflect.Type {
	return reflect.TypeOf((**CustomModel)(nil)).Elem()
}

func (i *CustomModel) ToCustomModelOutput() CustomModelOutput {
	return i.ToCustomModelOutputWithContext(context.Background())
}

func (i *CustomModel) ToCustomModelOutputWithContext(ctx context.Context) CustomModelOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CustomModelOutput)
}

// CustomModelArrayInput is an input type that accepts CustomModelArray and CustomModelArrayOutput values.
// You can construct a concrete instance of `CustomModelArrayInput` via:
//
//	CustomModelArray{ CustomModelArgs{...} }
type CustomModelArrayInput interface {
	pulumi.Input

	ToCustomModelArrayOutput() CustomModelArrayOutput
	ToCustomModelArrayOutputWithContext(context.Context) CustomModelArrayOutput
}

type CustomModelArray []CustomModelInput

func (CustomModelArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*CustomModel)(nil)).Elem()
}

func (i CustomModelArray) ToCustomModelArrayOutput() CustomModelArrayOutput {
	return i.ToCustomModelArrayOutputWithContext(context.Background())
}

func (i CustomModelArray) ToCustomModelArrayOutputWithContext(ctx context.Context) CustomModelArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CustomModelArrayOutput)
}

// CustomModelMapInput is an input type that accepts CustomModelMap and CustomModelMapOutput values.
// You can construct a concrete instance of `CustomModelMapInput` via:
//
//	CustomModelMap{ "key": CustomModelArgs{...} }
type CustomModelMapInput interface {
	pulumi.Input

	ToCustomModelMapOutput() CustomModelMapOutput
	ToCustomModelMapOutputWithContext(context.Context) CustomModelMapOutput
}

type CustomModelMap map[string]CustomModelInput

func (CustomModelMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*CustomModel)(nil)).Elem()
}

func (i CustomModelMap) ToCustomModelMapOutput() CustomModelMapOutput {
	return i.ToCustomModelMapOutputWithContext(context.Background())
}

func (i CustomModelMap) ToCustomModelMapOutputWithContext(ctx context.Context) CustomModelMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CustomModelMapOutput)
}

type CustomModelOutput struct{ *pulumi.OutputState }

func (CustomModelOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**CustomModel)(nil)).Elem()
}

func (o CustomModelOutput) ToCustomModelOutput() CustomModelOutput {
	return o
}

func (o CustomModelOutput) ToCustomModelOutputWithContext(ctx context.Context) CustomModelOutput {
	return o
}

// The ID of the base environment for the Custom Model.
func (o CustomModelOutput) BaseEnvironmentId() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomModel) pulumi.StringOutput { return v.BaseEnvironmentId }).(pulumi.StringOutput)
}

// The ID of the base environment version for the Custom Model.
func (o CustomModelOutput) BaseEnvironmentVersionId() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomModel) pulumi.StringOutput { return v.BaseEnvironmentVersionId }).(pulumi.StringOutput)
}

// The description of the Custom Model.
func (o CustomModelOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomModel) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// The name of the Custom Model.
func (o CustomModelOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomModel) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The runtime parameter values for the Custom Model.
func (o CustomModelOutput) RuntimeParameters() CustomModelRuntimeParameterArrayOutput {
	return o.ApplyT(func(v *CustomModel) CustomModelRuntimeParameterArrayOutput { return v.RuntimeParameters }).(CustomModelRuntimeParameterArrayOutput)
}

// The ID of the source LLM Blueprint for the Custom Model.
func (o CustomModelOutput) SourceLlmBlueprintId() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomModel) pulumi.StringOutput { return v.SourceLlmBlueprintId }).(pulumi.StringOutput)
}

// The ID of the latest Custom Model version.
func (o CustomModelOutput) VersionId() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomModel) pulumi.StringOutput { return v.VersionId }).(pulumi.StringOutput)
}

type CustomModelArrayOutput struct{ *pulumi.OutputState }

func (CustomModelArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*CustomModel)(nil)).Elem()
}

func (o CustomModelArrayOutput) ToCustomModelArrayOutput() CustomModelArrayOutput {
	return o
}

func (o CustomModelArrayOutput) ToCustomModelArrayOutputWithContext(ctx context.Context) CustomModelArrayOutput {
	return o
}

func (o CustomModelArrayOutput) Index(i pulumi.IntInput) CustomModelOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *CustomModel {
		return vs[0].([]*CustomModel)[vs[1].(int)]
	}).(CustomModelOutput)
}

type CustomModelMapOutput struct{ *pulumi.OutputState }

func (CustomModelMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*CustomModel)(nil)).Elem()
}

func (o CustomModelMapOutput) ToCustomModelMapOutput() CustomModelMapOutput {
	return o
}

func (o CustomModelMapOutput) ToCustomModelMapOutputWithContext(ctx context.Context) CustomModelMapOutput {
	return o
}

func (o CustomModelMapOutput) MapIndex(k pulumi.StringInput) CustomModelOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *CustomModel {
		return vs[0].(map[string]*CustomModel)[vs[1].(string)]
	}).(CustomModelOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CustomModelInput)(nil)).Elem(), &CustomModel{})
	pulumi.RegisterInputType(reflect.TypeOf((*CustomModelArrayInput)(nil)).Elem(), CustomModelArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*CustomModelMapInput)(nil)).Elem(), CustomModelMap{})
	pulumi.RegisterOutputType(CustomModelOutput{})
	pulumi.RegisterOutputType(CustomModelArrayOutput{})
	pulumi.RegisterOutputType(CustomModelMapOutput{})
}
