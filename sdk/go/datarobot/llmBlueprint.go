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

// LLMBlueprint
type LlmBlueprint struct {
	pulumi.CustomResourceState

	// The custom model LLM settings for the LLM Blueprint.
	CustomModelLlmSettings LlmBlueprintCustomModelLlmSettingsPtrOutput `pulumi:"customModelLlmSettings"`
	// The description of the LLM Blueprint.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The id of the LLM for the LLM Blueprint. If custom*model*llm_settings is set, this value must be 'custom-model'.
	LlmId pulumi.StringPtrOutput `pulumi:"llmId"`
	// The LLM settings for the LLM Blueprint.
	LlmSettings LlmBlueprintLlmSettingsPtrOutput `pulumi:"llmSettings"`
	// The name of the LLM Blueprint.
	Name pulumi.StringOutput `pulumi:"name"`
	// The id of the Playground for the LLM Blueprint.
	PlaygroundId pulumi.StringOutput `pulumi:"playgroundId"`
	// The prompt type for the LLM Blueprint.
	PromptType pulumi.StringOutput `pulumi:"promptType"`
	// The id of the Vector Database for the LLM Blueprint.
	VectorDatabaseId pulumi.StringPtrOutput `pulumi:"vectorDatabaseId"`
	// The Vector Database settings for the LLM Blueprint.
	VectorDatabaseSettings LlmBlueprintVectorDatabaseSettingsPtrOutput `pulumi:"vectorDatabaseSettings"`
}

// NewLlmBlueprint registers a new resource with the given unique name, arguments, and options.
func NewLlmBlueprint(ctx *pulumi.Context,
	name string, args *LlmBlueprintArgs, opts ...pulumi.ResourceOption) (*LlmBlueprint, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.PlaygroundId == nil {
		return nil, errors.New("invalid value for required argument 'PlaygroundId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource LlmBlueprint
	err := ctx.RegisterResource("datarobot:index/llmBlueprint:LlmBlueprint", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLlmBlueprint gets an existing LlmBlueprint resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLlmBlueprint(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LlmBlueprintState, opts ...pulumi.ResourceOption) (*LlmBlueprint, error) {
	var resource LlmBlueprint
	err := ctx.ReadResource("datarobot:index/llmBlueprint:LlmBlueprint", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LlmBlueprint resources.
type llmBlueprintState struct {
	// The custom model LLM settings for the LLM Blueprint.
	CustomModelLlmSettings *LlmBlueprintCustomModelLlmSettings `pulumi:"customModelLlmSettings"`
	// The description of the LLM Blueprint.
	Description *string `pulumi:"description"`
	// The id of the LLM for the LLM Blueprint. If custom*model*llm_settings is set, this value must be 'custom-model'.
	LlmId *string `pulumi:"llmId"`
	// The LLM settings for the LLM Blueprint.
	LlmSettings *LlmBlueprintLlmSettings `pulumi:"llmSettings"`
	// The name of the LLM Blueprint.
	Name *string `pulumi:"name"`
	// The id of the Playground for the LLM Blueprint.
	PlaygroundId *string `pulumi:"playgroundId"`
	// The prompt type for the LLM Blueprint.
	PromptType *string `pulumi:"promptType"`
	// The id of the Vector Database for the LLM Blueprint.
	VectorDatabaseId *string `pulumi:"vectorDatabaseId"`
	// The Vector Database settings for the LLM Blueprint.
	VectorDatabaseSettings *LlmBlueprintVectorDatabaseSettings `pulumi:"vectorDatabaseSettings"`
}

type LlmBlueprintState struct {
	// The custom model LLM settings for the LLM Blueprint.
	CustomModelLlmSettings LlmBlueprintCustomModelLlmSettingsPtrInput
	// The description of the LLM Blueprint.
	Description pulumi.StringPtrInput
	// The id of the LLM for the LLM Blueprint. If custom*model*llm_settings is set, this value must be 'custom-model'.
	LlmId pulumi.StringPtrInput
	// The LLM settings for the LLM Blueprint.
	LlmSettings LlmBlueprintLlmSettingsPtrInput
	// The name of the LLM Blueprint.
	Name pulumi.StringPtrInput
	// The id of the Playground for the LLM Blueprint.
	PlaygroundId pulumi.StringPtrInput
	// The prompt type for the LLM Blueprint.
	PromptType pulumi.StringPtrInput
	// The id of the Vector Database for the LLM Blueprint.
	VectorDatabaseId pulumi.StringPtrInput
	// The Vector Database settings for the LLM Blueprint.
	VectorDatabaseSettings LlmBlueprintVectorDatabaseSettingsPtrInput
}

func (LlmBlueprintState) ElementType() reflect.Type {
	return reflect.TypeOf((*llmBlueprintState)(nil)).Elem()
}

type llmBlueprintArgs struct {
	// The custom model LLM settings for the LLM Blueprint.
	CustomModelLlmSettings *LlmBlueprintCustomModelLlmSettings `pulumi:"customModelLlmSettings"`
	// The description of the LLM Blueprint.
	Description *string `pulumi:"description"`
	// The id of the LLM for the LLM Blueprint. If custom*model*llm_settings is set, this value must be 'custom-model'.
	LlmId *string `pulumi:"llmId"`
	// The LLM settings for the LLM Blueprint.
	LlmSettings *LlmBlueprintLlmSettings `pulumi:"llmSettings"`
	// The name of the LLM Blueprint.
	Name *string `pulumi:"name"`
	// The id of the Playground for the LLM Blueprint.
	PlaygroundId string `pulumi:"playgroundId"`
	// The prompt type for the LLM Blueprint.
	PromptType *string `pulumi:"promptType"`
	// The id of the Vector Database for the LLM Blueprint.
	VectorDatabaseId *string `pulumi:"vectorDatabaseId"`
	// The Vector Database settings for the LLM Blueprint.
	VectorDatabaseSettings *LlmBlueprintVectorDatabaseSettings `pulumi:"vectorDatabaseSettings"`
}

// The set of arguments for constructing a LlmBlueprint resource.
type LlmBlueprintArgs struct {
	// The custom model LLM settings for the LLM Blueprint.
	CustomModelLlmSettings LlmBlueprintCustomModelLlmSettingsPtrInput
	// The description of the LLM Blueprint.
	Description pulumi.StringPtrInput
	// The id of the LLM for the LLM Blueprint. If custom*model*llm_settings is set, this value must be 'custom-model'.
	LlmId pulumi.StringPtrInput
	// The LLM settings for the LLM Blueprint.
	LlmSettings LlmBlueprintLlmSettingsPtrInput
	// The name of the LLM Blueprint.
	Name pulumi.StringPtrInput
	// The id of the Playground for the LLM Blueprint.
	PlaygroundId pulumi.StringInput
	// The prompt type for the LLM Blueprint.
	PromptType pulumi.StringPtrInput
	// The id of the Vector Database for the LLM Blueprint.
	VectorDatabaseId pulumi.StringPtrInput
	// The Vector Database settings for the LLM Blueprint.
	VectorDatabaseSettings LlmBlueprintVectorDatabaseSettingsPtrInput
}

func (LlmBlueprintArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*llmBlueprintArgs)(nil)).Elem()
}

type LlmBlueprintInput interface {
	pulumi.Input

	ToLlmBlueprintOutput() LlmBlueprintOutput
	ToLlmBlueprintOutputWithContext(ctx context.Context) LlmBlueprintOutput
}

func (*LlmBlueprint) ElementType() reflect.Type {
	return reflect.TypeOf((**LlmBlueprint)(nil)).Elem()
}

func (i *LlmBlueprint) ToLlmBlueprintOutput() LlmBlueprintOutput {
	return i.ToLlmBlueprintOutputWithContext(context.Background())
}

func (i *LlmBlueprint) ToLlmBlueprintOutputWithContext(ctx context.Context) LlmBlueprintOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LlmBlueprintOutput)
}

// LlmBlueprintArrayInput is an input type that accepts LlmBlueprintArray and LlmBlueprintArrayOutput values.
// You can construct a concrete instance of `LlmBlueprintArrayInput` via:
//
//	LlmBlueprintArray{ LlmBlueprintArgs{...} }
type LlmBlueprintArrayInput interface {
	pulumi.Input

	ToLlmBlueprintArrayOutput() LlmBlueprintArrayOutput
	ToLlmBlueprintArrayOutputWithContext(context.Context) LlmBlueprintArrayOutput
}

type LlmBlueprintArray []LlmBlueprintInput

func (LlmBlueprintArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*LlmBlueprint)(nil)).Elem()
}

func (i LlmBlueprintArray) ToLlmBlueprintArrayOutput() LlmBlueprintArrayOutput {
	return i.ToLlmBlueprintArrayOutputWithContext(context.Background())
}

func (i LlmBlueprintArray) ToLlmBlueprintArrayOutputWithContext(ctx context.Context) LlmBlueprintArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LlmBlueprintArrayOutput)
}

// LlmBlueprintMapInput is an input type that accepts LlmBlueprintMap and LlmBlueprintMapOutput values.
// You can construct a concrete instance of `LlmBlueprintMapInput` via:
//
//	LlmBlueprintMap{ "key": LlmBlueprintArgs{...} }
type LlmBlueprintMapInput interface {
	pulumi.Input

	ToLlmBlueprintMapOutput() LlmBlueprintMapOutput
	ToLlmBlueprintMapOutputWithContext(context.Context) LlmBlueprintMapOutput
}

type LlmBlueprintMap map[string]LlmBlueprintInput

func (LlmBlueprintMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*LlmBlueprint)(nil)).Elem()
}

func (i LlmBlueprintMap) ToLlmBlueprintMapOutput() LlmBlueprintMapOutput {
	return i.ToLlmBlueprintMapOutputWithContext(context.Background())
}

func (i LlmBlueprintMap) ToLlmBlueprintMapOutputWithContext(ctx context.Context) LlmBlueprintMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LlmBlueprintMapOutput)
}

type LlmBlueprintOutput struct{ *pulumi.OutputState }

func (LlmBlueprintOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**LlmBlueprint)(nil)).Elem()
}

func (o LlmBlueprintOutput) ToLlmBlueprintOutput() LlmBlueprintOutput {
	return o
}

func (o LlmBlueprintOutput) ToLlmBlueprintOutputWithContext(ctx context.Context) LlmBlueprintOutput {
	return o
}

// The custom model LLM settings for the LLM Blueprint.
func (o LlmBlueprintOutput) CustomModelLlmSettings() LlmBlueprintCustomModelLlmSettingsPtrOutput {
	return o.ApplyT(func(v *LlmBlueprint) LlmBlueprintCustomModelLlmSettingsPtrOutput { return v.CustomModelLlmSettings }).(LlmBlueprintCustomModelLlmSettingsPtrOutput)
}

// The description of the LLM Blueprint.
func (o LlmBlueprintOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *LlmBlueprint) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The id of the LLM for the LLM Blueprint. If custom*model*llm_settings is set, this value must be 'custom-model'.
func (o LlmBlueprintOutput) LlmId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *LlmBlueprint) pulumi.StringPtrOutput { return v.LlmId }).(pulumi.StringPtrOutput)
}

// The LLM settings for the LLM Blueprint.
func (o LlmBlueprintOutput) LlmSettings() LlmBlueprintLlmSettingsPtrOutput {
	return o.ApplyT(func(v *LlmBlueprint) LlmBlueprintLlmSettingsPtrOutput { return v.LlmSettings }).(LlmBlueprintLlmSettingsPtrOutput)
}

// The name of the LLM Blueprint.
func (o LlmBlueprintOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *LlmBlueprint) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The id of the Playground for the LLM Blueprint.
func (o LlmBlueprintOutput) PlaygroundId() pulumi.StringOutput {
	return o.ApplyT(func(v *LlmBlueprint) pulumi.StringOutput { return v.PlaygroundId }).(pulumi.StringOutput)
}

// The prompt type for the LLM Blueprint.
func (o LlmBlueprintOutput) PromptType() pulumi.StringOutput {
	return o.ApplyT(func(v *LlmBlueprint) pulumi.StringOutput { return v.PromptType }).(pulumi.StringOutput)
}

// The id of the Vector Database for the LLM Blueprint.
func (o LlmBlueprintOutput) VectorDatabaseId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *LlmBlueprint) pulumi.StringPtrOutput { return v.VectorDatabaseId }).(pulumi.StringPtrOutput)
}

// The Vector Database settings for the LLM Blueprint.
func (o LlmBlueprintOutput) VectorDatabaseSettings() LlmBlueprintVectorDatabaseSettingsPtrOutput {
	return o.ApplyT(func(v *LlmBlueprint) LlmBlueprintVectorDatabaseSettingsPtrOutput { return v.VectorDatabaseSettings }).(LlmBlueprintVectorDatabaseSettingsPtrOutput)
}

type LlmBlueprintArrayOutput struct{ *pulumi.OutputState }

func (LlmBlueprintArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*LlmBlueprint)(nil)).Elem()
}

func (o LlmBlueprintArrayOutput) ToLlmBlueprintArrayOutput() LlmBlueprintArrayOutput {
	return o
}

func (o LlmBlueprintArrayOutput) ToLlmBlueprintArrayOutputWithContext(ctx context.Context) LlmBlueprintArrayOutput {
	return o
}

func (o LlmBlueprintArrayOutput) Index(i pulumi.IntInput) LlmBlueprintOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *LlmBlueprint {
		return vs[0].([]*LlmBlueprint)[vs[1].(int)]
	}).(LlmBlueprintOutput)
}

type LlmBlueprintMapOutput struct{ *pulumi.OutputState }

func (LlmBlueprintMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*LlmBlueprint)(nil)).Elem()
}

func (o LlmBlueprintMapOutput) ToLlmBlueprintMapOutput() LlmBlueprintMapOutput {
	return o
}

func (o LlmBlueprintMapOutput) ToLlmBlueprintMapOutputWithContext(ctx context.Context) LlmBlueprintMapOutput {
	return o
}

func (o LlmBlueprintMapOutput) MapIndex(k pulumi.StringInput) LlmBlueprintOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *LlmBlueprint {
		return vs[0].(map[string]*LlmBlueprint)[vs[1].(string)]
	}).(LlmBlueprintOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*LlmBlueprintInput)(nil)).Elem(), &LlmBlueprint{})
	pulumi.RegisterInputType(reflect.TypeOf((*LlmBlueprintArrayInput)(nil)).Elem(), LlmBlueprintArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*LlmBlueprintMapInput)(nil)).Elem(), LlmBlueprintMap{})
	pulumi.RegisterOutputType(LlmBlueprintOutput{})
	pulumi.RegisterOutputType(LlmBlueprintArrayOutput{})
	pulumi.RegisterOutputType(LlmBlueprintMapOutput{})
}
