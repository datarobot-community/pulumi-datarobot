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

// Execution Environment
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
//			example, err := datarobot.NewExecutionEnvironment(ctx, "example", &datarobot.ExecutionEnvironmentArgs{
//				ProgrammingLanguage: pulumi.String("python"),
//				Description:         pulumi.String("Example Execution Environment Description"),
//				DockerContextPath:   pulumi.String("docker_context.zip"),
//				DockerImage:         pulumi.String("docker_image.tar"),
//				UseCases: pulumi.StringArray{
//					pulumi.String("customModel"),
//				},
//			})
//			if err != nil {
//				return err
//			}
//			ctx.Export("datarobotExecutionEnvironmentId", example.ID())
//			ctx.Export("datarobotExecutionEnvironmentVersionId", example.VersionId)
//			return nil
//		})
//	}
//
// ```
type ExecutionEnvironment struct {
	pulumi.CustomResourceState

	// The status of the Execution Environment version build.
	BuildStatus pulumi.StringOutput `pulumi:"buildStatus"`
	// The description of the Execution Environment.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The path to a docker context archive or folder
	DockerContextPath pulumi.StringPtrOutput `pulumi:"dockerContextPath"`
	// A prebuilt environment image saved as a tarball using the Docker save command.
	DockerImage pulumi.StringPtrOutput `pulumi:"dockerImage"`
	// The name of the Execution Environment.
	Name pulumi.StringOutput `pulumi:"name"`
	// The programming language of the Execution Environment.
	ProgrammingLanguage pulumi.StringOutput `pulumi:"programmingLanguage"`
	// The list of Use Cases that the Execution Environment supports.
	UseCases pulumi.StringArrayOutput `pulumi:"useCases"`
	// The description of the Execution Environment version.
	VersionDescription pulumi.StringPtrOutput `pulumi:"versionDescription"`
	// The ID of the Execution Environment Version.
	VersionId pulumi.StringOutput `pulumi:"versionId"`
}

// NewExecutionEnvironment registers a new resource with the given unique name, arguments, and options.
func NewExecutionEnvironment(ctx *pulumi.Context,
	name string, args *ExecutionEnvironmentArgs, opts ...pulumi.ResourceOption) (*ExecutionEnvironment, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ProgrammingLanguage == nil {
		return nil, errors.New("invalid value for required argument 'ProgrammingLanguage'")
	}
	if args.UseCases == nil {
		return nil, errors.New("invalid value for required argument 'UseCases'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ExecutionEnvironment
	err := ctx.RegisterResource("datarobot:index/executionEnvironment:ExecutionEnvironment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetExecutionEnvironment gets an existing ExecutionEnvironment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetExecutionEnvironment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ExecutionEnvironmentState, opts ...pulumi.ResourceOption) (*ExecutionEnvironment, error) {
	var resource ExecutionEnvironment
	err := ctx.ReadResource("datarobot:index/executionEnvironment:ExecutionEnvironment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ExecutionEnvironment resources.
type executionEnvironmentState struct {
	// The status of the Execution Environment version build.
	BuildStatus *string `pulumi:"buildStatus"`
	// The description of the Execution Environment.
	Description *string `pulumi:"description"`
	// The path to a docker context archive or folder
	DockerContextPath *string `pulumi:"dockerContextPath"`
	// A prebuilt environment image saved as a tarball using the Docker save command.
	DockerImage *string `pulumi:"dockerImage"`
	// The name of the Execution Environment.
	Name *string `pulumi:"name"`
	// The programming language of the Execution Environment.
	ProgrammingLanguage *string `pulumi:"programmingLanguage"`
	// The list of Use Cases that the Execution Environment supports.
	UseCases []string `pulumi:"useCases"`
	// The description of the Execution Environment version.
	VersionDescription *string `pulumi:"versionDescription"`
	// The ID of the Execution Environment Version.
	VersionId *string `pulumi:"versionId"`
}

type ExecutionEnvironmentState struct {
	// The status of the Execution Environment version build.
	BuildStatus pulumi.StringPtrInput
	// The description of the Execution Environment.
	Description pulumi.StringPtrInput
	// The path to a docker context archive or folder
	DockerContextPath pulumi.StringPtrInput
	// A prebuilt environment image saved as a tarball using the Docker save command.
	DockerImage pulumi.StringPtrInput
	// The name of the Execution Environment.
	Name pulumi.StringPtrInput
	// The programming language of the Execution Environment.
	ProgrammingLanguage pulumi.StringPtrInput
	// The list of Use Cases that the Execution Environment supports.
	UseCases pulumi.StringArrayInput
	// The description of the Execution Environment version.
	VersionDescription pulumi.StringPtrInput
	// The ID of the Execution Environment Version.
	VersionId pulumi.StringPtrInput
}

func (ExecutionEnvironmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*executionEnvironmentState)(nil)).Elem()
}

type executionEnvironmentArgs struct {
	// The description of the Execution Environment.
	Description *string `pulumi:"description"`
	// The path to a docker context archive or folder
	DockerContextPath *string `pulumi:"dockerContextPath"`
	// A prebuilt environment image saved as a tarball using the Docker save command.
	DockerImage *string `pulumi:"dockerImage"`
	// The name of the Execution Environment.
	Name *string `pulumi:"name"`
	// The programming language of the Execution Environment.
	ProgrammingLanguage string `pulumi:"programmingLanguage"`
	// The list of Use Cases that the Execution Environment supports.
	UseCases []string `pulumi:"useCases"`
	// The description of the Execution Environment version.
	VersionDescription *string `pulumi:"versionDescription"`
}

// The set of arguments for constructing a ExecutionEnvironment resource.
type ExecutionEnvironmentArgs struct {
	// The description of the Execution Environment.
	Description pulumi.StringPtrInput
	// The path to a docker context archive or folder
	DockerContextPath pulumi.StringPtrInput
	// A prebuilt environment image saved as a tarball using the Docker save command.
	DockerImage pulumi.StringPtrInput
	// The name of the Execution Environment.
	Name pulumi.StringPtrInput
	// The programming language of the Execution Environment.
	ProgrammingLanguage pulumi.StringInput
	// The list of Use Cases that the Execution Environment supports.
	UseCases pulumi.StringArrayInput
	// The description of the Execution Environment version.
	VersionDescription pulumi.StringPtrInput
}

func (ExecutionEnvironmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*executionEnvironmentArgs)(nil)).Elem()
}

type ExecutionEnvironmentInput interface {
	pulumi.Input

	ToExecutionEnvironmentOutput() ExecutionEnvironmentOutput
	ToExecutionEnvironmentOutputWithContext(ctx context.Context) ExecutionEnvironmentOutput
}

func (*ExecutionEnvironment) ElementType() reflect.Type {
	return reflect.TypeOf((**ExecutionEnvironment)(nil)).Elem()
}

func (i *ExecutionEnvironment) ToExecutionEnvironmentOutput() ExecutionEnvironmentOutput {
	return i.ToExecutionEnvironmentOutputWithContext(context.Background())
}

func (i *ExecutionEnvironment) ToExecutionEnvironmentOutputWithContext(ctx context.Context) ExecutionEnvironmentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ExecutionEnvironmentOutput)
}

// ExecutionEnvironmentArrayInput is an input type that accepts ExecutionEnvironmentArray and ExecutionEnvironmentArrayOutput values.
// You can construct a concrete instance of `ExecutionEnvironmentArrayInput` via:
//
//	ExecutionEnvironmentArray{ ExecutionEnvironmentArgs{...} }
type ExecutionEnvironmentArrayInput interface {
	pulumi.Input

	ToExecutionEnvironmentArrayOutput() ExecutionEnvironmentArrayOutput
	ToExecutionEnvironmentArrayOutputWithContext(context.Context) ExecutionEnvironmentArrayOutput
}

type ExecutionEnvironmentArray []ExecutionEnvironmentInput

func (ExecutionEnvironmentArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ExecutionEnvironment)(nil)).Elem()
}

func (i ExecutionEnvironmentArray) ToExecutionEnvironmentArrayOutput() ExecutionEnvironmentArrayOutput {
	return i.ToExecutionEnvironmentArrayOutputWithContext(context.Background())
}

func (i ExecutionEnvironmentArray) ToExecutionEnvironmentArrayOutputWithContext(ctx context.Context) ExecutionEnvironmentArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ExecutionEnvironmentArrayOutput)
}

// ExecutionEnvironmentMapInput is an input type that accepts ExecutionEnvironmentMap and ExecutionEnvironmentMapOutput values.
// You can construct a concrete instance of `ExecutionEnvironmentMapInput` via:
//
//	ExecutionEnvironmentMap{ "key": ExecutionEnvironmentArgs{...} }
type ExecutionEnvironmentMapInput interface {
	pulumi.Input

	ToExecutionEnvironmentMapOutput() ExecutionEnvironmentMapOutput
	ToExecutionEnvironmentMapOutputWithContext(context.Context) ExecutionEnvironmentMapOutput
}

type ExecutionEnvironmentMap map[string]ExecutionEnvironmentInput

func (ExecutionEnvironmentMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ExecutionEnvironment)(nil)).Elem()
}

func (i ExecutionEnvironmentMap) ToExecutionEnvironmentMapOutput() ExecutionEnvironmentMapOutput {
	return i.ToExecutionEnvironmentMapOutputWithContext(context.Background())
}

func (i ExecutionEnvironmentMap) ToExecutionEnvironmentMapOutputWithContext(ctx context.Context) ExecutionEnvironmentMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ExecutionEnvironmentMapOutput)
}

type ExecutionEnvironmentOutput struct{ *pulumi.OutputState }

func (ExecutionEnvironmentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ExecutionEnvironment)(nil)).Elem()
}

func (o ExecutionEnvironmentOutput) ToExecutionEnvironmentOutput() ExecutionEnvironmentOutput {
	return o
}

func (o ExecutionEnvironmentOutput) ToExecutionEnvironmentOutputWithContext(ctx context.Context) ExecutionEnvironmentOutput {
	return o
}

// The status of the Execution Environment version build.
func (o ExecutionEnvironmentOutput) BuildStatus() pulumi.StringOutput {
	return o.ApplyT(func(v *ExecutionEnvironment) pulumi.StringOutput { return v.BuildStatus }).(pulumi.StringOutput)
}

// The description of the Execution Environment.
func (o ExecutionEnvironmentOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ExecutionEnvironment) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The path to a docker context archive or folder
func (o ExecutionEnvironmentOutput) DockerContextPath() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ExecutionEnvironment) pulumi.StringPtrOutput { return v.DockerContextPath }).(pulumi.StringPtrOutput)
}

// A prebuilt environment image saved as a tarball using the Docker save command.
func (o ExecutionEnvironmentOutput) DockerImage() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ExecutionEnvironment) pulumi.StringPtrOutput { return v.DockerImage }).(pulumi.StringPtrOutput)
}

// The name of the Execution Environment.
func (o ExecutionEnvironmentOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *ExecutionEnvironment) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The programming language of the Execution Environment.
func (o ExecutionEnvironmentOutput) ProgrammingLanguage() pulumi.StringOutput {
	return o.ApplyT(func(v *ExecutionEnvironment) pulumi.StringOutput { return v.ProgrammingLanguage }).(pulumi.StringOutput)
}

// The list of Use Cases that the Execution Environment supports.
func (o ExecutionEnvironmentOutput) UseCases() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *ExecutionEnvironment) pulumi.StringArrayOutput { return v.UseCases }).(pulumi.StringArrayOutput)
}

// The description of the Execution Environment version.
func (o ExecutionEnvironmentOutput) VersionDescription() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ExecutionEnvironment) pulumi.StringPtrOutput { return v.VersionDescription }).(pulumi.StringPtrOutput)
}

// The ID of the Execution Environment Version.
func (o ExecutionEnvironmentOutput) VersionId() pulumi.StringOutput {
	return o.ApplyT(func(v *ExecutionEnvironment) pulumi.StringOutput { return v.VersionId }).(pulumi.StringOutput)
}

type ExecutionEnvironmentArrayOutput struct{ *pulumi.OutputState }

func (ExecutionEnvironmentArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ExecutionEnvironment)(nil)).Elem()
}

func (o ExecutionEnvironmentArrayOutput) ToExecutionEnvironmentArrayOutput() ExecutionEnvironmentArrayOutput {
	return o
}

func (o ExecutionEnvironmentArrayOutput) ToExecutionEnvironmentArrayOutputWithContext(ctx context.Context) ExecutionEnvironmentArrayOutput {
	return o
}

func (o ExecutionEnvironmentArrayOutput) Index(i pulumi.IntInput) ExecutionEnvironmentOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *ExecutionEnvironment {
		return vs[0].([]*ExecutionEnvironment)[vs[1].(int)]
	}).(ExecutionEnvironmentOutput)
}

type ExecutionEnvironmentMapOutput struct{ *pulumi.OutputState }

func (ExecutionEnvironmentMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ExecutionEnvironment)(nil)).Elem()
}

func (o ExecutionEnvironmentMapOutput) ToExecutionEnvironmentMapOutput() ExecutionEnvironmentMapOutput {
	return o
}

func (o ExecutionEnvironmentMapOutput) ToExecutionEnvironmentMapOutputWithContext(ctx context.Context) ExecutionEnvironmentMapOutput {
	return o
}

func (o ExecutionEnvironmentMapOutput) MapIndex(k pulumi.StringInput) ExecutionEnvironmentOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *ExecutionEnvironment {
		return vs[0].(map[string]*ExecutionEnvironment)[vs[1].(string)]
	}).(ExecutionEnvironmentOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ExecutionEnvironmentInput)(nil)).Elem(), &ExecutionEnvironment{})
	pulumi.RegisterInputType(reflect.TypeOf((*ExecutionEnvironmentArrayInput)(nil)).Elem(), ExecutionEnvironmentArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ExecutionEnvironmentMapInput)(nil)).Elem(), ExecutionEnvironmentMap{})
	pulumi.RegisterOutputType(ExecutionEnvironmentOutput{})
	pulumi.RegisterOutputType(ExecutionEnvironmentArrayOutput{})
	pulumi.RegisterOutputType(ExecutionEnvironmentMapOutput{})
}
