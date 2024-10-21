package examples

import (
	"os"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

func getApiKey(t *testing.T) string {
	name := os.Getenv("DATAROBOT_API_TOKEN")
	if name == "" {
		t.Skipf("Skipping test due to missing DATAROBOT_API_TOKEN environment variable")
	}

	return name
}

func getCwd(t *testing.T) string {
	cwd, err := os.Getwd()
	if err != nil {
		t.FailNow()
	}

	return cwd
}

func getBaseOptions(t *testing.T) integration.ProgramTestOptions {
	key := getApiKey(t)
	return integration.ProgramTestOptions{
		Config: map[string]string{
			"apiKey": key,
		},
	}
}
