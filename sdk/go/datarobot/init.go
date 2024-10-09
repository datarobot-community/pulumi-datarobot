// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package datarobot

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/datarobot-community/pulumi-datarobot/sdk/go/datarobot/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "datarobot:index/apiTokenCredential:ApiTokenCredential":
		r = &ApiTokenCredential{}
	case "datarobot:index/applicationSource:ApplicationSource":
		r = &ApplicationSource{}
	case "datarobot:index/basicCredential:BasicCredential":
		r = &BasicCredential{}
	case "datarobot:index/customApplication:CustomApplication":
		r = &CustomApplication{}
	case "datarobot:index/customModel:CustomModel":
		r = &CustomModel{}
	case "datarobot:index/datasetFromFile:DatasetFromFile":
		r = &DatasetFromFile{}
	case "datarobot:index/datasetFromUrl:DatasetFromUrl":
		r = &DatasetFromUrl{}
	case "datarobot:index/deployment:Deployment":
		r = &Deployment{}
	case "datarobot:index/googleCloudCredential:GoogleCloudCredential":
		r = &GoogleCloudCredential{}
	case "datarobot:index/llmBlueprint:LlmBlueprint":
		r = &LlmBlueprint{}
	case "datarobot:index/playground:Playground":
		r = &Playground{}
	case "datarobot:index/predictionEnvironment:PredictionEnvironment":
		r = &PredictionEnvironment{}
	case "datarobot:index/qaApplication:QaApplication":
		r = &QaApplication{}
	case "datarobot:index/registeredModel:RegisteredModel":
		r = &RegisteredModel{}
	case "datarobot:index/registeredModelFromLeaderboard:RegisteredModelFromLeaderboard":
		r = &RegisteredModelFromLeaderboard{}
	case "datarobot:index/remoteRepository:RemoteRepository":
		r = &RemoteRepository{}
	case "datarobot:index/useCase:UseCase":
		r = &UseCase{}
	case "datarobot:index/vectorDatabase:VectorDatabase":
		r = &VectorDatabase{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

type pkg struct {
	version semver.Version
}

func (p *pkg) Version() semver.Version {
	return p.version
}

func (p *pkg) ConstructProvider(ctx *pulumi.Context, name, typ, urn string) (pulumi.ProviderResource, error) {
	if typ != "pulumi:providers:datarobot" {
		return nil, fmt.Errorf("unknown provider type: %s", typ)
	}

	r := &Provider{}
	err := ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return r, err
}

func init() {
	version, err := internal.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"datarobot",
		"index/apiTokenCredential",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"datarobot",
		"index/applicationSource",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"datarobot",
		"index/basicCredential",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"datarobot",
		"index/customApplication",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"datarobot",
		"index/customModel",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"datarobot",
		"index/datasetFromFile",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"datarobot",
		"index/datasetFromUrl",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"datarobot",
		"index/deployment",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"datarobot",
		"index/googleCloudCredential",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"datarobot",
		"index/llmBlueprint",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"datarobot",
		"index/playground",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"datarobot",
		"index/predictionEnvironment",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"datarobot",
		"index/qaApplication",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"datarobot",
		"index/registeredModel",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"datarobot",
		"index/registeredModelFromLeaderboard",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"datarobot",
		"index/remoteRepository",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"datarobot",
		"index/useCase",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"datarobot",
		"index/vectorDatabase",
		&module{version},
	)
	pulumi.RegisterResourcePackage(
		"datarobot",
		&pkg{version},
	)
}
