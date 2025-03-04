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

// registered model from leaderboard
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
//			example, err := datarobot.NewRegisteredModelFromLeaderboard(ctx, "example", &datarobot.RegisteredModelFromLeaderboardArgs{
//				ModelId:                       pulumi.String("111111111111"),
//				Description:                   pulumi.String("example description"),
//				VersionName:                   pulumi.String("example version name"),
//				PredictionThreshold:           pulumi.Float64(0.5),
//				ComputeAllTsIntervals:         pulumi.Bool(true),
//				DistributionPredictionModelId: pulumi.String("222222222222"),
//				UseCaseIds: pulumi.StringArray{
//					datarobot_use_case.Example.Id,
//				},
//			})
//			if err != nil {
//				return err
//			}
//			ctx.Export("datarobotRegisteredModelFromLeaderboardId", example.ID())
//			ctx.Export("datarobotRegisteredModelFromLeaderboardVersionId", example.VersionId)
//			return nil
//		})
//	}
//
// ```
type RegisteredModelFromLeaderboard struct {
	pulumi.CustomResourceState

	// Whether to compute all time series intervals (1-100 percentiles).
	ComputeAllTsIntervals pulumi.BoolPtrOutput `pulumi:"computeAllTsIntervals"`
	// The description of the Registered Model.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The ID of the DataRobot distribution prediction model trained on predictions from the DataRobot model.
	DistributionPredictionModelId pulumi.StringPtrOutput `pulumi:"distributionPredictionModelId"`
	// The ID of the DataRobot model for this Registered Model.
	ModelId pulumi.StringOutput `pulumi:"modelId"`
	// The name of the Registered Model.
	Name pulumi.StringOutput `pulumi:"name"`
	// The prediction threshold for the model.
	PredictionThreshold pulumi.Float64PtrOutput `pulumi:"predictionThreshold"`
	// The list of Use Case IDs to add the Registered Model version to.
	UseCaseIds pulumi.StringArrayOutput `pulumi:"useCaseIds"`
	// The ID of the Registered Model Version.
	VersionId pulumi.StringOutput `pulumi:"versionId"`
	// The name of the Registered Model Version.
	VersionName pulumi.StringOutput `pulumi:"versionName"`
}

// NewRegisteredModelFromLeaderboard registers a new resource with the given unique name, arguments, and options.
func NewRegisteredModelFromLeaderboard(ctx *pulumi.Context,
	name string, args *RegisteredModelFromLeaderboardArgs, opts ...pulumi.ResourceOption) (*RegisteredModelFromLeaderboard, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ModelId == nil {
		return nil, errors.New("invalid value for required argument 'ModelId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource RegisteredModelFromLeaderboard
	err := ctx.RegisterResource("datarobot:index/registeredModelFromLeaderboard:RegisteredModelFromLeaderboard", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRegisteredModelFromLeaderboard gets an existing RegisteredModelFromLeaderboard resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRegisteredModelFromLeaderboard(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RegisteredModelFromLeaderboardState, opts ...pulumi.ResourceOption) (*RegisteredModelFromLeaderboard, error) {
	var resource RegisteredModelFromLeaderboard
	err := ctx.ReadResource("datarobot:index/registeredModelFromLeaderboard:RegisteredModelFromLeaderboard", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RegisteredModelFromLeaderboard resources.
type registeredModelFromLeaderboardState struct {
	// Whether to compute all time series intervals (1-100 percentiles).
	ComputeAllTsIntervals *bool `pulumi:"computeAllTsIntervals"`
	// The description of the Registered Model.
	Description *string `pulumi:"description"`
	// The ID of the DataRobot distribution prediction model trained on predictions from the DataRobot model.
	DistributionPredictionModelId *string `pulumi:"distributionPredictionModelId"`
	// The ID of the DataRobot model for this Registered Model.
	ModelId *string `pulumi:"modelId"`
	// The name of the Registered Model.
	Name *string `pulumi:"name"`
	// The prediction threshold for the model.
	PredictionThreshold *float64 `pulumi:"predictionThreshold"`
	// The list of Use Case IDs to add the Registered Model version to.
	UseCaseIds []string `pulumi:"useCaseIds"`
	// The ID of the Registered Model Version.
	VersionId *string `pulumi:"versionId"`
	// The name of the Registered Model Version.
	VersionName *string `pulumi:"versionName"`
}

type RegisteredModelFromLeaderboardState struct {
	// Whether to compute all time series intervals (1-100 percentiles).
	ComputeAllTsIntervals pulumi.BoolPtrInput
	// The description of the Registered Model.
	Description pulumi.StringPtrInput
	// The ID of the DataRobot distribution prediction model trained on predictions from the DataRobot model.
	DistributionPredictionModelId pulumi.StringPtrInput
	// The ID of the DataRobot model for this Registered Model.
	ModelId pulumi.StringPtrInput
	// The name of the Registered Model.
	Name pulumi.StringPtrInput
	// The prediction threshold for the model.
	PredictionThreshold pulumi.Float64PtrInput
	// The list of Use Case IDs to add the Registered Model version to.
	UseCaseIds pulumi.StringArrayInput
	// The ID of the Registered Model Version.
	VersionId pulumi.StringPtrInput
	// The name of the Registered Model Version.
	VersionName pulumi.StringPtrInput
}

func (RegisteredModelFromLeaderboardState) ElementType() reflect.Type {
	return reflect.TypeOf((*registeredModelFromLeaderboardState)(nil)).Elem()
}

type registeredModelFromLeaderboardArgs struct {
	// Whether to compute all time series intervals (1-100 percentiles).
	ComputeAllTsIntervals *bool `pulumi:"computeAllTsIntervals"`
	// The description of the Registered Model.
	Description *string `pulumi:"description"`
	// The ID of the DataRobot distribution prediction model trained on predictions from the DataRobot model.
	DistributionPredictionModelId *string `pulumi:"distributionPredictionModelId"`
	// The ID of the DataRobot model for this Registered Model.
	ModelId string `pulumi:"modelId"`
	// The name of the Registered Model.
	Name *string `pulumi:"name"`
	// The prediction threshold for the model.
	PredictionThreshold *float64 `pulumi:"predictionThreshold"`
	// The list of Use Case IDs to add the Registered Model version to.
	UseCaseIds []string `pulumi:"useCaseIds"`
	// The name of the Registered Model Version.
	VersionName *string `pulumi:"versionName"`
}

// The set of arguments for constructing a RegisteredModelFromLeaderboard resource.
type RegisteredModelFromLeaderboardArgs struct {
	// Whether to compute all time series intervals (1-100 percentiles).
	ComputeAllTsIntervals pulumi.BoolPtrInput
	// The description of the Registered Model.
	Description pulumi.StringPtrInput
	// The ID of the DataRobot distribution prediction model trained on predictions from the DataRobot model.
	DistributionPredictionModelId pulumi.StringPtrInput
	// The ID of the DataRobot model for this Registered Model.
	ModelId pulumi.StringInput
	// The name of the Registered Model.
	Name pulumi.StringPtrInput
	// The prediction threshold for the model.
	PredictionThreshold pulumi.Float64PtrInput
	// The list of Use Case IDs to add the Registered Model version to.
	UseCaseIds pulumi.StringArrayInput
	// The name of the Registered Model Version.
	VersionName pulumi.StringPtrInput
}

func (RegisteredModelFromLeaderboardArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*registeredModelFromLeaderboardArgs)(nil)).Elem()
}

type RegisteredModelFromLeaderboardInput interface {
	pulumi.Input

	ToRegisteredModelFromLeaderboardOutput() RegisteredModelFromLeaderboardOutput
	ToRegisteredModelFromLeaderboardOutputWithContext(ctx context.Context) RegisteredModelFromLeaderboardOutput
}

func (*RegisteredModelFromLeaderboard) ElementType() reflect.Type {
	return reflect.TypeOf((**RegisteredModelFromLeaderboard)(nil)).Elem()
}

func (i *RegisteredModelFromLeaderboard) ToRegisteredModelFromLeaderboardOutput() RegisteredModelFromLeaderboardOutput {
	return i.ToRegisteredModelFromLeaderboardOutputWithContext(context.Background())
}

func (i *RegisteredModelFromLeaderboard) ToRegisteredModelFromLeaderboardOutputWithContext(ctx context.Context) RegisteredModelFromLeaderboardOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RegisteredModelFromLeaderboardOutput)
}

// RegisteredModelFromLeaderboardArrayInput is an input type that accepts RegisteredModelFromLeaderboardArray and RegisteredModelFromLeaderboardArrayOutput values.
// You can construct a concrete instance of `RegisteredModelFromLeaderboardArrayInput` via:
//
//	RegisteredModelFromLeaderboardArray{ RegisteredModelFromLeaderboardArgs{...} }
type RegisteredModelFromLeaderboardArrayInput interface {
	pulumi.Input

	ToRegisteredModelFromLeaderboardArrayOutput() RegisteredModelFromLeaderboardArrayOutput
	ToRegisteredModelFromLeaderboardArrayOutputWithContext(context.Context) RegisteredModelFromLeaderboardArrayOutput
}

type RegisteredModelFromLeaderboardArray []RegisteredModelFromLeaderboardInput

func (RegisteredModelFromLeaderboardArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*RegisteredModelFromLeaderboard)(nil)).Elem()
}

func (i RegisteredModelFromLeaderboardArray) ToRegisteredModelFromLeaderboardArrayOutput() RegisteredModelFromLeaderboardArrayOutput {
	return i.ToRegisteredModelFromLeaderboardArrayOutputWithContext(context.Background())
}

func (i RegisteredModelFromLeaderboardArray) ToRegisteredModelFromLeaderboardArrayOutputWithContext(ctx context.Context) RegisteredModelFromLeaderboardArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RegisteredModelFromLeaderboardArrayOutput)
}

// RegisteredModelFromLeaderboardMapInput is an input type that accepts RegisteredModelFromLeaderboardMap and RegisteredModelFromLeaderboardMapOutput values.
// You can construct a concrete instance of `RegisteredModelFromLeaderboardMapInput` via:
//
//	RegisteredModelFromLeaderboardMap{ "key": RegisteredModelFromLeaderboardArgs{...} }
type RegisteredModelFromLeaderboardMapInput interface {
	pulumi.Input

	ToRegisteredModelFromLeaderboardMapOutput() RegisteredModelFromLeaderboardMapOutput
	ToRegisteredModelFromLeaderboardMapOutputWithContext(context.Context) RegisteredModelFromLeaderboardMapOutput
}

type RegisteredModelFromLeaderboardMap map[string]RegisteredModelFromLeaderboardInput

func (RegisteredModelFromLeaderboardMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*RegisteredModelFromLeaderboard)(nil)).Elem()
}

func (i RegisteredModelFromLeaderboardMap) ToRegisteredModelFromLeaderboardMapOutput() RegisteredModelFromLeaderboardMapOutput {
	return i.ToRegisteredModelFromLeaderboardMapOutputWithContext(context.Background())
}

func (i RegisteredModelFromLeaderboardMap) ToRegisteredModelFromLeaderboardMapOutputWithContext(ctx context.Context) RegisteredModelFromLeaderboardMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RegisteredModelFromLeaderboardMapOutput)
}

type RegisteredModelFromLeaderboardOutput struct{ *pulumi.OutputState }

func (RegisteredModelFromLeaderboardOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**RegisteredModelFromLeaderboard)(nil)).Elem()
}

func (o RegisteredModelFromLeaderboardOutput) ToRegisteredModelFromLeaderboardOutput() RegisteredModelFromLeaderboardOutput {
	return o
}

func (o RegisteredModelFromLeaderboardOutput) ToRegisteredModelFromLeaderboardOutputWithContext(ctx context.Context) RegisteredModelFromLeaderboardOutput {
	return o
}

// Whether to compute all time series intervals (1-100 percentiles).
func (o RegisteredModelFromLeaderboardOutput) ComputeAllTsIntervals() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *RegisteredModelFromLeaderboard) pulumi.BoolPtrOutput { return v.ComputeAllTsIntervals }).(pulumi.BoolPtrOutput)
}

// The description of the Registered Model.
func (o RegisteredModelFromLeaderboardOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *RegisteredModelFromLeaderboard) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The ID of the DataRobot distribution prediction model trained on predictions from the DataRobot model.
func (o RegisteredModelFromLeaderboardOutput) DistributionPredictionModelId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *RegisteredModelFromLeaderboard) pulumi.StringPtrOutput { return v.DistributionPredictionModelId }).(pulumi.StringPtrOutput)
}

// The ID of the DataRobot model for this Registered Model.
func (o RegisteredModelFromLeaderboardOutput) ModelId() pulumi.StringOutput {
	return o.ApplyT(func(v *RegisteredModelFromLeaderboard) pulumi.StringOutput { return v.ModelId }).(pulumi.StringOutput)
}

// The name of the Registered Model.
func (o RegisteredModelFromLeaderboardOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *RegisteredModelFromLeaderboard) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The prediction threshold for the model.
func (o RegisteredModelFromLeaderboardOutput) PredictionThreshold() pulumi.Float64PtrOutput {
	return o.ApplyT(func(v *RegisteredModelFromLeaderboard) pulumi.Float64PtrOutput { return v.PredictionThreshold }).(pulumi.Float64PtrOutput)
}

// The list of Use Case IDs to add the Registered Model version to.
func (o RegisteredModelFromLeaderboardOutput) UseCaseIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *RegisteredModelFromLeaderboard) pulumi.StringArrayOutput { return v.UseCaseIds }).(pulumi.StringArrayOutput)
}

// The ID of the Registered Model Version.
func (o RegisteredModelFromLeaderboardOutput) VersionId() pulumi.StringOutput {
	return o.ApplyT(func(v *RegisteredModelFromLeaderboard) pulumi.StringOutput { return v.VersionId }).(pulumi.StringOutput)
}

// The name of the Registered Model Version.
func (o RegisteredModelFromLeaderboardOutput) VersionName() pulumi.StringOutput {
	return o.ApplyT(func(v *RegisteredModelFromLeaderboard) pulumi.StringOutput { return v.VersionName }).(pulumi.StringOutput)
}

type RegisteredModelFromLeaderboardArrayOutput struct{ *pulumi.OutputState }

func (RegisteredModelFromLeaderboardArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*RegisteredModelFromLeaderboard)(nil)).Elem()
}

func (o RegisteredModelFromLeaderboardArrayOutput) ToRegisteredModelFromLeaderboardArrayOutput() RegisteredModelFromLeaderboardArrayOutput {
	return o
}

func (o RegisteredModelFromLeaderboardArrayOutput) ToRegisteredModelFromLeaderboardArrayOutputWithContext(ctx context.Context) RegisteredModelFromLeaderboardArrayOutput {
	return o
}

func (o RegisteredModelFromLeaderboardArrayOutput) Index(i pulumi.IntInput) RegisteredModelFromLeaderboardOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *RegisteredModelFromLeaderboard {
		return vs[0].([]*RegisteredModelFromLeaderboard)[vs[1].(int)]
	}).(RegisteredModelFromLeaderboardOutput)
}

type RegisteredModelFromLeaderboardMapOutput struct{ *pulumi.OutputState }

func (RegisteredModelFromLeaderboardMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*RegisteredModelFromLeaderboard)(nil)).Elem()
}

func (o RegisteredModelFromLeaderboardMapOutput) ToRegisteredModelFromLeaderboardMapOutput() RegisteredModelFromLeaderboardMapOutput {
	return o
}

func (o RegisteredModelFromLeaderboardMapOutput) ToRegisteredModelFromLeaderboardMapOutputWithContext(ctx context.Context) RegisteredModelFromLeaderboardMapOutput {
	return o
}

func (o RegisteredModelFromLeaderboardMapOutput) MapIndex(k pulumi.StringInput) RegisteredModelFromLeaderboardOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *RegisteredModelFromLeaderboard {
		return vs[0].(map[string]*RegisteredModelFromLeaderboard)[vs[1].(string)]
	}).(RegisteredModelFromLeaderboardOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*RegisteredModelFromLeaderboardInput)(nil)).Elem(), &RegisteredModelFromLeaderboard{})
	pulumi.RegisterInputType(reflect.TypeOf((*RegisteredModelFromLeaderboardArrayInput)(nil)).Elem(), RegisteredModelFromLeaderboardArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*RegisteredModelFromLeaderboardMapInput)(nil)).Elem(), RegisteredModelFromLeaderboardMap{})
	pulumi.RegisterOutputType(RegisteredModelFromLeaderboardOutput{})
	pulumi.RegisterOutputType(RegisteredModelFromLeaderboardArrayOutput{})
	pulumi.RegisterOutputType(RegisteredModelFromLeaderboardMapOutput{})
}
