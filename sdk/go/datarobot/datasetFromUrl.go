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

// Data set from file
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
//			example, err := datarobot.NewDatasetFromUrl(ctx, "example", &datarobot.DatasetFromUrlArgs{
//				Url: pulumi.String("[URL to upload from]"),
//				UseCaseIds: pulumi.StringArray{
//					datarobot_use_case.Example.Id,
//				},
//			})
//			if err != nil {
//				return err
//			}
//			ctx.Export("exampleId", example.ID())
//			return nil
//		})
//	}
//
// ```
type DatasetFromUrl struct {
	pulumi.CustomResourceState

	// The name of the Dataset.
	Name pulumi.StringOutput `pulumi:"name"`
	// The URL to upload the Dataset from.
	Url pulumi.StringOutput `pulumi:"url"`
	// The list of Use Case IDs to add the Dataset to.
	UseCaseIds pulumi.StringArrayOutput `pulumi:"useCaseIds"`
}

// NewDatasetFromUrl registers a new resource with the given unique name, arguments, and options.
func NewDatasetFromUrl(ctx *pulumi.Context,
	name string, args *DatasetFromUrlArgs, opts ...pulumi.ResourceOption) (*DatasetFromUrl, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Url == nil {
		return nil, errors.New("invalid value for required argument 'Url'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource DatasetFromUrl
	err := ctx.RegisterResource("datarobot:index/datasetFromUrl:DatasetFromUrl", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDatasetFromUrl gets an existing DatasetFromUrl resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDatasetFromUrl(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DatasetFromUrlState, opts ...pulumi.ResourceOption) (*DatasetFromUrl, error) {
	var resource DatasetFromUrl
	err := ctx.ReadResource("datarobot:index/datasetFromUrl:DatasetFromUrl", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DatasetFromUrl resources.
type datasetFromUrlState struct {
	// The name of the Dataset.
	Name *string `pulumi:"name"`
	// The URL to upload the Dataset from.
	Url *string `pulumi:"url"`
	// The list of Use Case IDs to add the Dataset to.
	UseCaseIds []string `pulumi:"useCaseIds"`
}

type DatasetFromUrlState struct {
	// The name of the Dataset.
	Name pulumi.StringPtrInput
	// The URL to upload the Dataset from.
	Url pulumi.StringPtrInput
	// The list of Use Case IDs to add the Dataset to.
	UseCaseIds pulumi.StringArrayInput
}

func (DatasetFromUrlState) ElementType() reflect.Type {
	return reflect.TypeOf((*datasetFromUrlState)(nil)).Elem()
}

type datasetFromUrlArgs struct {
	// The name of the Dataset.
	Name *string `pulumi:"name"`
	// The URL to upload the Dataset from.
	Url string `pulumi:"url"`
	// The list of Use Case IDs to add the Dataset to.
	UseCaseIds []string `pulumi:"useCaseIds"`
}

// The set of arguments for constructing a DatasetFromUrl resource.
type DatasetFromUrlArgs struct {
	// The name of the Dataset.
	Name pulumi.StringPtrInput
	// The URL to upload the Dataset from.
	Url pulumi.StringInput
	// The list of Use Case IDs to add the Dataset to.
	UseCaseIds pulumi.StringArrayInput
}

func (DatasetFromUrlArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*datasetFromUrlArgs)(nil)).Elem()
}

type DatasetFromUrlInput interface {
	pulumi.Input

	ToDatasetFromUrlOutput() DatasetFromUrlOutput
	ToDatasetFromUrlOutputWithContext(ctx context.Context) DatasetFromUrlOutput
}

func (*DatasetFromUrl) ElementType() reflect.Type {
	return reflect.TypeOf((**DatasetFromUrl)(nil)).Elem()
}

func (i *DatasetFromUrl) ToDatasetFromUrlOutput() DatasetFromUrlOutput {
	return i.ToDatasetFromUrlOutputWithContext(context.Background())
}

func (i *DatasetFromUrl) ToDatasetFromUrlOutputWithContext(ctx context.Context) DatasetFromUrlOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DatasetFromUrlOutput)
}

// DatasetFromUrlArrayInput is an input type that accepts DatasetFromUrlArray and DatasetFromUrlArrayOutput values.
// You can construct a concrete instance of `DatasetFromUrlArrayInput` via:
//
//	DatasetFromUrlArray{ DatasetFromUrlArgs{...} }
type DatasetFromUrlArrayInput interface {
	pulumi.Input

	ToDatasetFromUrlArrayOutput() DatasetFromUrlArrayOutput
	ToDatasetFromUrlArrayOutputWithContext(context.Context) DatasetFromUrlArrayOutput
}

type DatasetFromUrlArray []DatasetFromUrlInput

func (DatasetFromUrlArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DatasetFromUrl)(nil)).Elem()
}

func (i DatasetFromUrlArray) ToDatasetFromUrlArrayOutput() DatasetFromUrlArrayOutput {
	return i.ToDatasetFromUrlArrayOutputWithContext(context.Background())
}

func (i DatasetFromUrlArray) ToDatasetFromUrlArrayOutputWithContext(ctx context.Context) DatasetFromUrlArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DatasetFromUrlArrayOutput)
}

// DatasetFromUrlMapInput is an input type that accepts DatasetFromUrlMap and DatasetFromUrlMapOutput values.
// You can construct a concrete instance of `DatasetFromUrlMapInput` via:
//
//	DatasetFromUrlMap{ "key": DatasetFromUrlArgs{...} }
type DatasetFromUrlMapInput interface {
	pulumi.Input

	ToDatasetFromUrlMapOutput() DatasetFromUrlMapOutput
	ToDatasetFromUrlMapOutputWithContext(context.Context) DatasetFromUrlMapOutput
}

type DatasetFromUrlMap map[string]DatasetFromUrlInput

func (DatasetFromUrlMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DatasetFromUrl)(nil)).Elem()
}

func (i DatasetFromUrlMap) ToDatasetFromUrlMapOutput() DatasetFromUrlMapOutput {
	return i.ToDatasetFromUrlMapOutputWithContext(context.Background())
}

func (i DatasetFromUrlMap) ToDatasetFromUrlMapOutputWithContext(ctx context.Context) DatasetFromUrlMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DatasetFromUrlMapOutput)
}

type DatasetFromUrlOutput struct{ *pulumi.OutputState }

func (DatasetFromUrlOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DatasetFromUrl)(nil)).Elem()
}

func (o DatasetFromUrlOutput) ToDatasetFromUrlOutput() DatasetFromUrlOutput {
	return o
}

func (o DatasetFromUrlOutput) ToDatasetFromUrlOutputWithContext(ctx context.Context) DatasetFromUrlOutput {
	return o
}

// The name of the Dataset.
func (o DatasetFromUrlOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *DatasetFromUrl) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The URL to upload the Dataset from.
func (o DatasetFromUrlOutput) Url() pulumi.StringOutput {
	return o.ApplyT(func(v *DatasetFromUrl) pulumi.StringOutput { return v.Url }).(pulumi.StringOutput)
}

// The list of Use Case IDs to add the Dataset to.
func (o DatasetFromUrlOutput) UseCaseIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *DatasetFromUrl) pulumi.StringArrayOutput { return v.UseCaseIds }).(pulumi.StringArrayOutput)
}

type DatasetFromUrlArrayOutput struct{ *pulumi.OutputState }

func (DatasetFromUrlArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DatasetFromUrl)(nil)).Elem()
}

func (o DatasetFromUrlArrayOutput) ToDatasetFromUrlArrayOutput() DatasetFromUrlArrayOutput {
	return o
}

func (o DatasetFromUrlArrayOutput) ToDatasetFromUrlArrayOutputWithContext(ctx context.Context) DatasetFromUrlArrayOutput {
	return o
}

func (o DatasetFromUrlArrayOutput) Index(i pulumi.IntInput) DatasetFromUrlOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *DatasetFromUrl {
		return vs[0].([]*DatasetFromUrl)[vs[1].(int)]
	}).(DatasetFromUrlOutput)
}

type DatasetFromUrlMapOutput struct{ *pulumi.OutputState }

func (DatasetFromUrlMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DatasetFromUrl)(nil)).Elem()
}

func (o DatasetFromUrlMapOutput) ToDatasetFromUrlMapOutput() DatasetFromUrlMapOutput {
	return o
}

func (o DatasetFromUrlMapOutput) ToDatasetFromUrlMapOutputWithContext(ctx context.Context) DatasetFromUrlMapOutput {
	return o
}

func (o DatasetFromUrlMapOutput) MapIndex(k pulumi.StringInput) DatasetFromUrlOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *DatasetFromUrl {
		return vs[0].(map[string]*DatasetFromUrl)[vs[1].(string)]
	}).(DatasetFromUrlOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DatasetFromUrlInput)(nil)).Elem(), &DatasetFromUrl{})
	pulumi.RegisterInputType(reflect.TypeOf((*DatasetFromUrlArrayInput)(nil)).Elem(), DatasetFromUrlArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*DatasetFromUrlMapInput)(nil)).Elem(), DatasetFromUrlMap{})
	pulumi.RegisterOutputType(DatasetFromUrlOutput{})
	pulumi.RegisterOutputType(DatasetFromUrlArrayOutput{})
	pulumi.RegisterOutputType(DatasetFromUrlMapOutput{})
}