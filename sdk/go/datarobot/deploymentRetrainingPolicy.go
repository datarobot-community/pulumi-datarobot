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

// Deployment Retraining Policy
type DeploymentRetrainingPolicy struct {
	pulumi.CustomResourceState

	// The the action to take on the resultant new model.
	Action pulumi.StringOutput `pulumi:"action"`
	// Options for projects used to build new models.
	AutopilotOptions DeploymentRetrainingPolicyAutopilotOptionsOutput `pulumi:"autopilotOptions"`
	// The ID of the Deployment for the Retraining Policy.
	DeploymentId pulumi.StringOutput `pulumi:"deploymentId"`
	// The description of the Retraining Policy.
	Description pulumi.StringOutput `pulumi:"description"`
	// The feature list strategy used for modeling.
	FeatureListStrategy pulumi.StringOutput `pulumi:"featureListStrategy"`
	// Determines how the new model is selected when the retraining policy runs.
	ModelSelectionStrategy pulumi.StringOutput `pulumi:"modelSelectionStrategy"`
	// The name of the Retraining Policy.
	Name pulumi.StringOutput `pulumi:"name"`
	// Options for projects used to build new models.
	ProjectOptions DeploymentRetrainingPolicyProjectOptionsOutput `pulumi:"projectOptions"`
	// The project option strategy used for modeling.
	ProjectOptionsStrategy pulumi.StringOutput `pulumi:"projectOptionsStrategy"`
	// Time Series project options used to build new models.
	TimeSeriesOptions DeploymentRetrainingPolicyTimeSeriesOptionsPtrOutput `pulumi:"timeSeriesOptions"`
	// Retraining policy trigger.
	Trigger DeploymentRetrainingPolicyTriggerPtrOutput `pulumi:"trigger"`
	// The ID of the use case to which the retraining policy belongs.
	UseCaseId pulumi.StringPtrOutput `pulumi:"useCaseId"`
}

// NewDeploymentRetrainingPolicy registers a new resource with the given unique name, arguments, and options.
func NewDeploymentRetrainingPolicy(ctx *pulumi.Context,
	name string, args *DeploymentRetrainingPolicyArgs, opts ...pulumi.ResourceOption) (*DeploymentRetrainingPolicy, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DeploymentId == nil {
		return nil, errors.New("invalid value for required argument 'DeploymentId'")
	}
	if args.Description == nil {
		return nil, errors.New("invalid value for required argument 'Description'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource DeploymentRetrainingPolicy
	err := ctx.RegisterResource("datarobot:index/deploymentRetrainingPolicy:DeploymentRetrainingPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDeploymentRetrainingPolicy gets an existing DeploymentRetrainingPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDeploymentRetrainingPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DeploymentRetrainingPolicyState, opts ...pulumi.ResourceOption) (*DeploymentRetrainingPolicy, error) {
	var resource DeploymentRetrainingPolicy
	err := ctx.ReadResource("datarobot:index/deploymentRetrainingPolicy:DeploymentRetrainingPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DeploymentRetrainingPolicy resources.
type deploymentRetrainingPolicyState struct {
	// The the action to take on the resultant new model.
	Action *string `pulumi:"action"`
	// Options for projects used to build new models.
	AutopilotOptions *DeploymentRetrainingPolicyAutopilotOptions `pulumi:"autopilotOptions"`
	// The ID of the Deployment for the Retraining Policy.
	DeploymentId *string `pulumi:"deploymentId"`
	// The description of the Retraining Policy.
	Description *string `pulumi:"description"`
	// The feature list strategy used for modeling.
	FeatureListStrategy *string `pulumi:"featureListStrategy"`
	// Determines how the new model is selected when the retraining policy runs.
	ModelSelectionStrategy *string `pulumi:"modelSelectionStrategy"`
	// The name of the Retraining Policy.
	Name *string `pulumi:"name"`
	// Options for projects used to build new models.
	ProjectOptions *DeploymentRetrainingPolicyProjectOptions `pulumi:"projectOptions"`
	// The project option strategy used for modeling.
	ProjectOptionsStrategy *string `pulumi:"projectOptionsStrategy"`
	// Time Series project options used to build new models.
	TimeSeriesOptions *DeploymentRetrainingPolicyTimeSeriesOptions `pulumi:"timeSeriesOptions"`
	// Retraining policy trigger.
	Trigger *DeploymentRetrainingPolicyTrigger `pulumi:"trigger"`
	// The ID of the use case to which the retraining policy belongs.
	UseCaseId *string `pulumi:"useCaseId"`
}

type DeploymentRetrainingPolicyState struct {
	// The the action to take on the resultant new model.
	Action pulumi.StringPtrInput
	// Options for projects used to build new models.
	AutopilotOptions DeploymentRetrainingPolicyAutopilotOptionsPtrInput
	// The ID of the Deployment for the Retraining Policy.
	DeploymentId pulumi.StringPtrInput
	// The description of the Retraining Policy.
	Description pulumi.StringPtrInput
	// The feature list strategy used for modeling.
	FeatureListStrategy pulumi.StringPtrInput
	// Determines how the new model is selected when the retraining policy runs.
	ModelSelectionStrategy pulumi.StringPtrInput
	// The name of the Retraining Policy.
	Name pulumi.StringPtrInput
	// Options for projects used to build new models.
	ProjectOptions DeploymentRetrainingPolicyProjectOptionsPtrInput
	// The project option strategy used for modeling.
	ProjectOptionsStrategy pulumi.StringPtrInput
	// Time Series project options used to build new models.
	TimeSeriesOptions DeploymentRetrainingPolicyTimeSeriesOptionsPtrInput
	// Retraining policy trigger.
	Trigger DeploymentRetrainingPolicyTriggerPtrInput
	// The ID of the use case to which the retraining policy belongs.
	UseCaseId pulumi.StringPtrInput
}

func (DeploymentRetrainingPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*deploymentRetrainingPolicyState)(nil)).Elem()
}

type deploymentRetrainingPolicyArgs struct {
	// The the action to take on the resultant new model.
	Action *string `pulumi:"action"`
	// Options for projects used to build new models.
	AutopilotOptions *DeploymentRetrainingPolicyAutopilotOptions `pulumi:"autopilotOptions"`
	// The ID of the Deployment for the Retraining Policy.
	DeploymentId string `pulumi:"deploymentId"`
	// The description of the Retraining Policy.
	Description string `pulumi:"description"`
	// The feature list strategy used for modeling.
	FeatureListStrategy *string `pulumi:"featureListStrategy"`
	// Determines how the new model is selected when the retraining policy runs.
	ModelSelectionStrategy *string `pulumi:"modelSelectionStrategy"`
	// The name of the Retraining Policy.
	Name *string `pulumi:"name"`
	// Options for projects used to build new models.
	ProjectOptions *DeploymentRetrainingPolicyProjectOptions `pulumi:"projectOptions"`
	// The project option strategy used for modeling.
	ProjectOptionsStrategy *string `pulumi:"projectOptionsStrategy"`
	// Time Series project options used to build new models.
	TimeSeriesOptions *DeploymentRetrainingPolicyTimeSeriesOptions `pulumi:"timeSeriesOptions"`
	// Retraining policy trigger.
	Trigger *DeploymentRetrainingPolicyTrigger `pulumi:"trigger"`
	// The ID of the use case to which the retraining policy belongs.
	UseCaseId *string `pulumi:"useCaseId"`
}

// The set of arguments for constructing a DeploymentRetrainingPolicy resource.
type DeploymentRetrainingPolicyArgs struct {
	// The the action to take on the resultant new model.
	Action pulumi.StringPtrInput
	// Options for projects used to build new models.
	AutopilotOptions DeploymentRetrainingPolicyAutopilotOptionsPtrInput
	// The ID of the Deployment for the Retraining Policy.
	DeploymentId pulumi.StringInput
	// The description of the Retraining Policy.
	Description pulumi.StringInput
	// The feature list strategy used for modeling.
	FeatureListStrategy pulumi.StringPtrInput
	// Determines how the new model is selected when the retraining policy runs.
	ModelSelectionStrategy pulumi.StringPtrInput
	// The name of the Retraining Policy.
	Name pulumi.StringPtrInput
	// Options for projects used to build new models.
	ProjectOptions DeploymentRetrainingPolicyProjectOptionsPtrInput
	// The project option strategy used for modeling.
	ProjectOptionsStrategy pulumi.StringPtrInput
	// Time Series project options used to build new models.
	TimeSeriesOptions DeploymentRetrainingPolicyTimeSeriesOptionsPtrInput
	// Retraining policy trigger.
	Trigger DeploymentRetrainingPolicyTriggerPtrInput
	// The ID of the use case to which the retraining policy belongs.
	UseCaseId pulumi.StringPtrInput
}

func (DeploymentRetrainingPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*deploymentRetrainingPolicyArgs)(nil)).Elem()
}

type DeploymentRetrainingPolicyInput interface {
	pulumi.Input

	ToDeploymentRetrainingPolicyOutput() DeploymentRetrainingPolicyOutput
	ToDeploymentRetrainingPolicyOutputWithContext(ctx context.Context) DeploymentRetrainingPolicyOutput
}

func (*DeploymentRetrainingPolicy) ElementType() reflect.Type {
	return reflect.TypeOf((**DeploymentRetrainingPolicy)(nil)).Elem()
}

func (i *DeploymentRetrainingPolicy) ToDeploymentRetrainingPolicyOutput() DeploymentRetrainingPolicyOutput {
	return i.ToDeploymentRetrainingPolicyOutputWithContext(context.Background())
}

func (i *DeploymentRetrainingPolicy) ToDeploymentRetrainingPolicyOutputWithContext(ctx context.Context) DeploymentRetrainingPolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DeploymentRetrainingPolicyOutput)
}

// DeploymentRetrainingPolicyArrayInput is an input type that accepts DeploymentRetrainingPolicyArray and DeploymentRetrainingPolicyArrayOutput values.
// You can construct a concrete instance of `DeploymentRetrainingPolicyArrayInput` via:
//
//	DeploymentRetrainingPolicyArray{ DeploymentRetrainingPolicyArgs{...} }
type DeploymentRetrainingPolicyArrayInput interface {
	pulumi.Input

	ToDeploymentRetrainingPolicyArrayOutput() DeploymentRetrainingPolicyArrayOutput
	ToDeploymentRetrainingPolicyArrayOutputWithContext(context.Context) DeploymentRetrainingPolicyArrayOutput
}

type DeploymentRetrainingPolicyArray []DeploymentRetrainingPolicyInput

func (DeploymentRetrainingPolicyArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DeploymentRetrainingPolicy)(nil)).Elem()
}

func (i DeploymentRetrainingPolicyArray) ToDeploymentRetrainingPolicyArrayOutput() DeploymentRetrainingPolicyArrayOutput {
	return i.ToDeploymentRetrainingPolicyArrayOutputWithContext(context.Background())
}

func (i DeploymentRetrainingPolicyArray) ToDeploymentRetrainingPolicyArrayOutputWithContext(ctx context.Context) DeploymentRetrainingPolicyArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DeploymentRetrainingPolicyArrayOutput)
}

// DeploymentRetrainingPolicyMapInput is an input type that accepts DeploymentRetrainingPolicyMap and DeploymentRetrainingPolicyMapOutput values.
// You can construct a concrete instance of `DeploymentRetrainingPolicyMapInput` via:
//
//	DeploymentRetrainingPolicyMap{ "key": DeploymentRetrainingPolicyArgs{...} }
type DeploymentRetrainingPolicyMapInput interface {
	pulumi.Input

	ToDeploymentRetrainingPolicyMapOutput() DeploymentRetrainingPolicyMapOutput
	ToDeploymentRetrainingPolicyMapOutputWithContext(context.Context) DeploymentRetrainingPolicyMapOutput
}

type DeploymentRetrainingPolicyMap map[string]DeploymentRetrainingPolicyInput

func (DeploymentRetrainingPolicyMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DeploymentRetrainingPolicy)(nil)).Elem()
}

func (i DeploymentRetrainingPolicyMap) ToDeploymentRetrainingPolicyMapOutput() DeploymentRetrainingPolicyMapOutput {
	return i.ToDeploymentRetrainingPolicyMapOutputWithContext(context.Background())
}

func (i DeploymentRetrainingPolicyMap) ToDeploymentRetrainingPolicyMapOutputWithContext(ctx context.Context) DeploymentRetrainingPolicyMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DeploymentRetrainingPolicyMapOutput)
}

type DeploymentRetrainingPolicyOutput struct{ *pulumi.OutputState }

func (DeploymentRetrainingPolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DeploymentRetrainingPolicy)(nil)).Elem()
}

func (o DeploymentRetrainingPolicyOutput) ToDeploymentRetrainingPolicyOutput() DeploymentRetrainingPolicyOutput {
	return o
}

func (o DeploymentRetrainingPolicyOutput) ToDeploymentRetrainingPolicyOutputWithContext(ctx context.Context) DeploymentRetrainingPolicyOutput {
	return o
}

// The the action to take on the resultant new model.
func (o DeploymentRetrainingPolicyOutput) Action() pulumi.StringOutput {
	return o.ApplyT(func(v *DeploymentRetrainingPolicy) pulumi.StringOutput { return v.Action }).(pulumi.StringOutput)
}

// Options for projects used to build new models.
func (o DeploymentRetrainingPolicyOutput) AutopilotOptions() DeploymentRetrainingPolicyAutopilotOptionsOutput {
	return o.ApplyT(func(v *DeploymentRetrainingPolicy) DeploymentRetrainingPolicyAutopilotOptionsOutput {
		return v.AutopilotOptions
	}).(DeploymentRetrainingPolicyAutopilotOptionsOutput)
}

// The ID of the Deployment for the Retraining Policy.
func (o DeploymentRetrainingPolicyOutput) DeploymentId() pulumi.StringOutput {
	return o.ApplyT(func(v *DeploymentRetrainingPolicy) pulumi.StringOutput { return v.DeploymentId }).(pulumi.StringOutput)
}

// The description of the Retraining Policy.
func (o DeploymentRetrainingPolicyOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *DeploymentRetrainingPolicy) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// The feature list strategy used for modeling.
func (o DeploymentRetrainingPolicyOutput) FeatureListStrategy() pulumi.StringOutput {
	return o.ApplyT(func(v *DeploymentRetrainingPolicy) pulumi.StringOutput { return v.FeatureListStrategy }).(pulumi.StringOutput)
}

// Determines how the new model is selected when the retraining policy runs.
func (o DeploymentRetrainingPolicyOutput) ModelSelectionStrategy() pulumi.StringOutput {
	return o.ApplyT(func(v *DeploymentRetrainingPolicy) pulumi.StringOutput { return v.ModelSelectionStrategy }).(pulumi.StringOutput)
}

// The name of the Retraining Policy.
func (o DeploymentRetrainingPolicyOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *DeploymentRetrainingPolicy) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Options for projects used to build new models.
func (o DeploymentRetrainingPolicyOutput) ProjectOptions() DeploymentRetrainingPolicyProjectOptionsOutput {
	return o.ApplyT(func(v *DeploymentRetrainingPolicy) DeploymentRetrainingPolicyProjectOptionsOutput {
		return v.ProjectOptions
	}).(DeploymentRetrainingPolicyProjectOptionsOutput)
}

// The project option strategy used for modeling.
func (o DeploymentRetrainingPolicyOutput) ProjectOptionsStrategy() pulumi.StringOutput {
	return o.ApplyT(func(v *DeploymentRetrainingPolicy) pulumi.StringOutput { return v.ProjectOptionsStrategy }).(pulumi.StringOutput)
}

// Time Series project options used to build new models.
func (o DeploymentRetrainingPolicyOutput) TimeSeriesOptions() DeploymentRetrainingPolicyTimeSeriesOptionsPtrOutput {
	return o.ApplyT(func(v *DeploymentRetrainingPolicy) DeploymentRetrainingPolicyTimeSeriesOptionsPtrOutput {
		return v.TimeSeriesOptions
	}).(DeploymentRetrainingPolicyTimeSeriesOptionsPtrOutput)
}

// Retraining policy trigger.
func (o DeploymentRetrainingPolicyOutput) Trigger() DeploymentRetrainingPolicyTriggerPtrOutput {
	return o.ApplyT(func(v *DeploymentRetrainingPolicy) DeploymentRetrainingPolicyTriggerPtrOutput { return v.Trigger }).(DeploymentRetrainingPolicyTriggerPtrOutput)
}

// The ID of the use case to which the retraining policy belongs.
func (o DeploymentRetrainingPolicyOutput) UseCaseId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DeploymentRetrainingPolicy) pulumi.StringPtrOutput { return v.UseCaseId }).(pulumi.StringPtrOutput)
}

type DeploymentRetrainingPolicyArrayOutput struct{ *pulumi.OutputState }

func (DeploymentRetrainingPolicyArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DeploymentRetrainingPolicy)(nil)).Elem()
}

func (o DeploymentRetrainingPolicyArrayOutput) ToDeploymentRetrainingPolicyArrayOutput() DeploymentRetrainingPolicyArrayOutput {
	return o
}

func (o DeploymentRetrainingPolicyArrayOutput) ToDeploymentRetrainingPolicyArrayOutputWithContext(ctx context.Context) DeploymentRetrainingPolicyArrayOutput {
	return o
}

func (o DeploymentRetrainingPolicyArrayOutput) Index(i pulumi.IntInput) DeploymentRetrainingPolicyOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *DeploymentRetrainingPolicy {
		return vs[0].([]*DeploymentRetrainingPolicy)[vs[1].(int)]
	}).(DeploymentRetrainingPolicyOutput)
}

type DeploymentRetrainingPolicyMapOutput struct{ *pulumi.OutputState }

func (DeploymentRetrainingPolicyMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DeploymentRetrainingPolicy)(nil)).Elem()
}

func (o DeploymentRetrainingPolicyMapOutput) ToDeploymentRetrainingPolicyMapOutput() DeploymentRetrainingPolicyMapOutput {
	return o
}

func (o DeploymentRetrainingPolicyMapOutput) ToDeploymentRetrainingPolicyMapOutputWithContext(ctx context.Context) DeploymentRetrainingPolicyMapOutput {
	return o
}

func (o DeploymentRetrainingPolicyMapOutput) MapIndex(k pulumi.StringInput) DeploymentRetrainingPolicyOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *DeploymentRetrainingPolicy {
		return vs[0].(map[string]*DeploymentRetrainingPolicy)[vs[1].(string)]
	}).(DeploymentRetrainingPolicyOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DeploymentRetrainingPolicyInput)(nil)).Elem(), &DeploymentRetrainingPolicy{})
	pulumi.RegisterInputType(reflect.TypeOf((*DeploymentRetrainingPolicyArrayInput)(nil)).Elem(), DeploymentRetrainingPolicyArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*DeploymentRetrainingPolicyMapInput)(nil)).Elem(), DeploymentRetrainingPolicyMap{})
	pulumi.RegisterOutputType(DeploymentRetrainingPolicyOutput{})
	pulumi.RegisterOutputType(DeploymentRetrainingPolicyArrayOutput{})
	pulumi.RegisterOutputType(DeploymentRetrainingPolicyMapOutput{})
}
