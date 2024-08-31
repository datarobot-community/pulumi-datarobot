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

// remote repository
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
//			_, err := datarobot.NewRemoteRepository(ctx, "githubExample", &datarobot.RemoteRepositoryArgs{
//				Description: pulumi.String("Description for the example remote repository"),
//				Location:    pulumi.String("https://github.com/datarobot/datarobot-user-models"),
//				SourceType:  pulumi.String("github"),
//			})
//			if err != nil {
//				return err
//			}
//			_, err = datarobot.NewRemoteRepository(ctx, "gitlabExample", &datarobot.RemoteRepositoryArgs{
//				Location:            pulumi.String("https://gitlab.yourcompany.com/username/repository"),
//				PersonalAccessToken: pulumi.String("your_personal_access_token"),
//				SourceType:          pulumi.String("gitlab-cloud"),
//			})
//			if err != nil {
//				return err
//			}
//			_, err = datarobot.NewRemoteRepository(ctx, "bitbucketExample", &datarobot.RemoteRepositoryArgs{
//				Location:   pulumi.String("https://bitbucket.yourcompany.com/projects/PROJECTKEY/repos/REPONAME/browse"),
//				SourceType: pulumi.String("bitbucket-server"),
//			})
//			if err != nil {
//				return err
//			}
//			_, err = datarobot.NewRemoteRepository(ctx, "s3Example", &datarobot.RemoteRepositoryArgs{
//				Location:   pulumi.String("my-s3-bucket"),
//				SourceType: pulumi.String("s3"),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
type RemoteRepository struct {
	pulumi.CustomResourceState

	// The AWS access key ID for the Remote Repository.
	AwsAccessKeyId pulumi.StringPtrOutput `pulumi:"awsAccessKeyId"`
	// The AWS secret access key for the Remote Repository.
	AwsSecretAccessKey pulumi.StringPtrOutput `pulumi:"awsSecretAccessKey"`
	// The AWS session token for the Remote Repository.
	AwsSessionToken pulumi.StringPtrOutput `pulumi:"awsSessionToken"`
	// The description of the Remote Repository.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The location of the Remote Repository. (Bucket name for S3)
	Location pulumi.StringOutput `pulumi:"location"`
	// The name of the Remote Repository.
	Name pulumi.StringOutput `pulumi:"name"`
	// The personal access token for the Remote Repository.
	PersonalAccessToken pulumi.StringPtrOutput `pulumi:"personalAccessToken"`
	// The source type of the Remote Repository.
	SourceType pulumi.StringOutput `pulumi:"sourceType"`
}

// NewRemoteRepository registers a new resource with the given unique name, arguments, and options.
func NewRemoteRepository(ctx *pulumi.Context,
	name string, args *RemoteRepositoryArgs, opts ...pulumi.ResourceOption) (*RemoteRepository, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Location == nil {
		return nil, errors.New("invalid value for required argument 'Location'")
	}
	if args.SourceType == nil {
		return nil, errors.New("invalid value for required argument 'SourceType'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource RemoteRepository
	err := ctx.RegisterResource("datarobot:index/remoteRepository:RemoteRepository", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRemoteRepository gets an existing RemoteRepository resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRemoteRepository(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RemoteRepositoryState, opts ...pulumi.ResourceOption) (*RemoteRepository, error) {
	var resource RemoteRepository
	err := ctx.ReadResource("datarobot:index/remoteRepository:RemoteRepository", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RemoteRepository resources.
type remoteRepositoryState struct {
	// The AWS access key ID for the Remote Repository.
	AwsAccessKeyId *string `pulumi:"awsAccessKeyId"`
	// The AWS secret access key for the Remote Repository.
	AwsSecretAccessKey *string `pulumi:"awsSecretAccessKey"`
	// The AWS session token for the Remote Repository.
	AwsSessionToken *string `pulumi:"awsSessionToken"`
	// The description of the Remote Repository.
	Description *string `pulumi:"description"`
	// The location of the Remote Repository. (Bucket name for S3)
	Location *string `pulumi:"location"`
	// The name of the Remote Repository.
	Name *string `pulumi:"name"`
	// The personal access token for the Remote Repository.
	PersonalAccessToken *string `pulumi:"personalAccessToken"`
	// The source type of the Remote Repository.
	SourceType *string `pulumi:"sourceType"`
}

type RemoteRepositoryState struct {
	// The AWS access key ID for the Remote Repository.
	AwsAccessKeyId pulumi.StringPtrInput
	// The AWS secret access key for the Remote Repository.
	AwsSecretAccessKey pulumi.StringPtrInput
	// The AWS session token for the Remote Repository.
	AwsSessionToken pulumi.StringPtrInput
	// The description of the Remote Repository.
	Description pulumi.StringPtrInput
	// The location of the Remote Repository. (Bucket name for S3)
	Location pulumi.StringPtrInput
	// The name of the Remote Repository.
	Name pulumi.StringPtrInput
	// The personal access token for the Remote Repository.
	PersonalAccessToken pulumi.StringPtrInput
	// The source type of the Remote Repository.
	SourceType pulumi.StringPtrInput
}

func (RemoteRepositoryState) ElementType() reflect.Type {
	return reflect.TypeOf((*remoteRepositoryState)(nil)).Elem()
}

type remoteRepositoryArgs struct {
	// The AWS access key ID for the Remote Repository.
	AwsAccessKeyId *string `pulumi:"awsAccessKeyId"`
	// The AWS secret access key for the Remote Repository.
	AwsSecretAccessKey *string `pulumi:"awsSecretAccessKey"`
	// The AWS session token for the Remote Repository.
	AwsSessionToken *string `pulumi:"awsSessionToken"`
	// The description of the Remote Repository.
	Description *string `pulumi:"description"`
	// The location of the Remote Repository. (Bucket name for S3)
	Location string `pulumi:"location"`
	// The name of the Remote Repository.
	Name *string `pulumi:"name"`
	// The personal access token for the Remote Repository.
	PersonalAccessToken *string `pulumi:"personalAccessToken"`
	// The source type of the Remote Repository.
	SourceType string `pulumi:"sourceType"`
}

// The set of arguments for constructing a RemoteRepository resource.
type RemoteRepositoryArgs struct {
	// The AWS access key ID for the Remote Repository.
	AwsAccessKeyId pulumi.StringPtrInput
	// The AWS secret access key for the Remote Repository.
	AwsSecretAccessKey pulumi.StringPtrInput
	// The AWS session token for the Remote Repository.
	AwsSessionToken pulumi.StringPtrInput
	// The description of the Remote Repository.
	Description pulumi.StringPtrInput
	// The location of the Remote Repository. (Bucket name for S3)
	Location pulumi.StringInput
	// The name of the Remote Repository.
	Name pulumi.StringPtrInput
	// The personal access token for the Remote Repository.
	PersonalAccessToken pulumi.StringPtrInput
	// The source type of the Remote Repository.
	SourceType pulumi.StringInput
}

func (RemoteRepositoryArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*remoteRepositoryArgs)(nil)).Elem()
}

type RemoteRepositoryInput interface {
	pulumi.Input

	ToRemoteRepositoryOutput() RemoteRepositoryOutput
	ToRemoteRepositoryOutputWithContext(ctx context.Context) RemoteRepositoryOutput
}

func (*RemoteRepository) ElementType() reflect.Type {
	return reflect.TypeOf((**RemoteRepository)(nil)).Elem()
}

func (i *RemoteRepository) ToRemoteRepositoryOutput() RemoteRepositoryOutput {
	return i.ToRemoteRepositoryOutputWithContext(context.Background())
}

func (i *RemoteRepository) ToRemoteRepositoryOutputWithContext(ctx context.Context) RemoteRepositoryOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RemoteRepositoryOutput)
}

// RemoteRepositoryArrayInput is an input type that accepts RemoteRepositoryArray and RemoteRepositoryArrayOutput values.
// You can construct a concrete instance of `RemoteRepositoryArrayInput` via:
//
//	RemoteRepositoryArray{ RemoteRepositoryArgs{...} }
type RemoteRepositoryArrayInput interface {
	pulumi.Input

	ToRemoteRepositoryArrayOutput() RemoteRepositoryArrayOutput
	ToRemoteRepositoryArrayOutputWithContext(context.Context) RemoteRepositoryArrayOutput
}

type RemoteRepositoryArray []RemoteRepositoryInput

func (RemoteRepositoryArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*RemoteRepository)(nil)).Elem()
}

func (i RemoteRepositoryArray) ToRemoteRepositoryArrayOutput() RemoteRepositoryArrayOutput {
	return i.ToRemoteRepositoryArrayOutputWithContext(context.Background())
}

func (i RemoteRepositoryArray) ToRemoteRepositoryArrayOutputWithContext(ctx context.Context) RemoteRepositoryArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RemoteRepositoryArrayOutput)
}

// RemoteRepositoryMapInput is an input type that accepts RemoteRepositoryMap and RemoteRepositoryMapOutput values.
// You can construct a concrete instance of `RemoteRepositoryMapInput` via:
//
//	RemoteRepositoryMap{ "key": RemoteRepositoryArgs{...} }
type RemoteRepositoryMapInput interface {
	pulumi.Input

	ToRemoteRepositoryMapOutput() RemoteRepositoryMapOutput
	ToRemoteRepositoryMapOutputWithContext(context.Context) RemoteRepositoryMapOutput
}

type RemoteRepositoryMap map[string]RemoteRepositoryInput

func (RemoteRepositoryMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*RemoteRepository)(nil)).Elem()
}

func (i RemoteRepositoryMap) ToRemoteRepositoryMapOutput() RemoteRepositoryMapOutput {
	return i.ToRemoteRepositoryMapOutputWithContext(context.Background())
}

func (i RemoteRepositoryMap) ToRemoteRepositoryMapOutputWithContext(ctx context.Context) RemoteRepositoryMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RemoteRepositoryMapOutput)
}

type RemoteRepositoryOutput struct{ *pulumi.OutputState }

func (RemoteRepositoryOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**RemoteRepository)(nil)).Elem()
}

func (o RemoteRepositoryOutput) ToRemoteRepositoryOutput() RemoteRepositoryOutput {
	return o
}

func (o RemoteRepositoryOutput) ToRemoteRepositoryOutputWithContext(ctx context.Context) RemoteRepositoryOutput {
	return o
}

// The AWS access key ID for the Remote Repository.
func (o RemoteRepositoryOutput) AwsAccessKeyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *RemoteRepository) pulumi.StringPtrOutput { return v.AwsAccessKeyId }).(pulumi.StringPtrOutput)
}

// The AWS secret access key for the Remote Repository.
func (o RemoteRepositoryOutput) AwsSecretAccessKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *RemoteRepository) pulumi.StringPtrOutput { return v.AwsSecretAccessKey }).(pulumi.StringPtrOutput)
}

// The AWS session token for the Remote Repository.
func (o RemoteRepositoryOutput) AwsSessionToken() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *RemoteRepository) pulumi.StringPtrOutput { return v.AwsSessionToken }).(pulumi.StringPtrOutput)
}

// The description of the Remote Repository.
func (o RemoteRepositoryOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *RemoteRepository) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The location of the Remote Repository. (Bucket name for S3)
func (o RemoteRepositoryOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v *RemoteRepository) pulumi.StringOutput { return v.Location }).(pulumi.StringOutput)
}

// The name of the Remote Repository.
func (o RemoteRepositoryOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *RemoteRepository) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The personal access token for the Remote Repository.
func (o RemoteRepositoryOutput) PersonalAccessToken() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *RemoteRepository) pulumi.StringPtrOutput { return v.PersonalAccessToken }).(pulumi.StringPtrOutput)
}

// The source type of the Remote Repository.
func (o RemoteRepositoryOutput) SourceType() pulumi.StringOutput {
	return o.ApplyT(func(v *RemoteRepository) pulumi.StringOutput { return v.SourceType }).(pulumi.StringOutput)
}

type RemoteRepositoryArrayOutput struct{ *pulumi.OutputState }

func (RemoteRepositoryArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*RemoteRepository)(nil)).Elem()
}

func (o RemoteRepositoryArrayOutput) ToRemoteRepositoryArrayOutput() RemoteRepositoryArrayOutput {
	return o
}

func (o RemoteRepositoryArrayOutput) ToRemoteRepositoryArrayOutputWithContext(ctx context.Context) RemoteRepositoryArrayOutput {
	return o
}

func (o RemoteRepositoryArrayOutput) Index(i pulumi.IntInput) RemoteRepositoryOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *RemoteRepository {
		return vs[0].([]*RemoteRepository)[vs[1].(int)]
	}).(RemoteRepositoryOutput)
}

type RemoteRepositoryMapOutput struct{ *pulumi.OutputState }

func (RemoteRepositoryMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*RemoteRepository)(nil)).Elem()
}

func (o RemoteRepositoryMapOutput) ToRemoteRepositoryMapOutput() RemoteRepositoryMapOutput {
	return o
}

func (o RemoteRepositoryMapOutput) ToRemoteRepositoryMapOutputWithContext(ctx context.Context) RemoteRepositoryMapOutput {
	return o
}

func (o RemoteRepositoryMapOutput) MapIndex(k pulumi.StringInput) RemoteRepositoryOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *RemoteRepository {
		return vs[0].(map[string]*RemoteRepository)[vs[1].(string)]
	}).(RemoteRepositoryOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*RemoteRepositoryInput)(nil)).Elem(), &RemoteRepository{})
	pulumi.RegisterInputType(reflect.TypeOf((*RemoteRepositoryArrayInput)(nil)).Elem(), RemoteRepositoryArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*RemoteRepositoryMapInput)(nil)).Elem(), RemoteRepositoryMap{})
	pulumi.RegisterOutputType(RemoteRepositoryOutput{})
	pulumi.RegisterOutputType(RemoteRepositoryArrayOutput{})
	pulumi.RegisterOutputType(RemoteRepositoryMapOutput{})
}
