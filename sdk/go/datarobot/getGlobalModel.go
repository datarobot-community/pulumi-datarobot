// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package datarobot

import (
	"context"
	"reflect"

	"github.com/datarobot-community/pulumi-datarobot/sdk/go/datarobot/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Global Model
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
//			_, err := datarobot.GetGlobalModel(ctx, &datarobot.GetGlobalModelArgs{
//				Name: "[DataRobot] Dummy Binary Classification",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetGlobalModel(ctx *pulumi.Context, args *GetGlobalModelArgs, opts ...pulumi.InvokeOption) (*GetGlobalModelResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetGlobalModelResult
	err := ctx.Invoke("datarobot:index/getGlobalModel:getGlobalModel", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getGlobalModel.
type GetGlobalModelArgs struct {
	// The name of the Registered Model.
	Name string `pulumi:"name"`
}

// A collection of values returned by getGlobalModel.
type GetGlobalModelResult struct {
	// The ID of the Global Model.
	Id string `pulumi:"id"`
	// The name of the Registered Model.
	Name string `pulumi:"name"`
	// The ID of the Global Model Version.
	VersionId string `pulumi:"versionId"`
}

func GetGlobalModelOutput(ctx *pulumi.Context, args GetGlobalModelOutputArgs, opts ...pulumi.InvokeOption) GetGlobalModelResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetGlobalModelResult, error) {
			args := v.(GetGlobalModelArgs)
			r, err := GetGlobalModel(ctx, &args, opts...)
			var s GetGlobalModelResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetGlobalModelResultOutput)
}

// A collection of arguments for invoking getGlobalModel.
type GetGlobalModelOutputArgs struct {
	// The name of the Registered Model.
	Name pulumi.StringInput `pulumi:"name"`
}

func (GetGlobalModelOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetGlobalModelArgs)(nil)).Elem()
}

// A collection of values returned by getGlobalModel.
type GetGlobalModelResultOutput struct{ *pulumi.OutputState }

func (GetGlobalModelResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetGlobalModelResult)(nil)).Elem()
}

func (o GetGlobalModelResultOutput) ToGetGlobalModelResultOutput() GetGlobalModelResultOutput {
	return o
}

func (o GetGlobalModelResultOutput) ToGetGlobalModelResultOutputWithContext(ctx context.Context) GetGlobalModelResultOutput {
	return o
}

// The ID of the Global Model.
func (o GetGlobalModelResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetGlobalModelResult) string { return v.Id }).(pulumi.StringOutput)
}

// The name of the Registered Model.
func (o GetGlobalModelResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v GetGlobalModelResult) string { return v.Name }).(pulumi.StringOutput)
}

// The ID of the Global Model Version.
func (o GetGlobalModelResultOutput) VersionId() pulumi.StringOutput {
	return o.ApplyT(func(v GetGlobalModelResult) string { return v.VersionId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetGlobalModelResultOutput{})
}
