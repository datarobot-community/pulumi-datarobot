//go:build python || all
// +build python all

package examples

import (
	"path/filepath"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

func getPythonBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := getBaseOptions(t)
	basePython := base.With(integration.ProgramTestOptions{
		ExpectRefreshChanges: true,
		Dependencies: []string{
			filepath.Join("..", "sdk", "python"),
		},
	})

	return basePython
}

func TestAccDatarobotPy(t *testing.T) {
	test := getPythonBaseOptions(t).
		With(integration.ProgramTestOptions{
			Dir: filepath.Join(getCwd(t), "py"),
		})
	integration.ProgramTest(t, &test)
}
