PROJECT_NAME := DataRobot Package

SHELL            := /bin/bash
PACK             := datarobot
PROJECT          := github.com/datarobot-community/pulumi-datarobot
NODE_MODULE_NAME := @datarobot/pulumi-${PACK}
TF_NAME          := ${PACK}
PROVIDER_PATH    := provider
VERSION_PATH     := ${PROVIDER_PATH}/pkg/version.Version

TFGEN           := pulumi-tfgen-${PACK}
PROVIDER        := pulumi-resource-${PACK}
# Override version to avoid +dirty suffix during development
# VERSION         := $(shell pulumictl get version | sed 's/+dirty//')
# Use a specific version for development
VERSION         := $(shell git describe --tags --exact-match 2>/dev/null || git describe --tags --abbrev=0 2>/dev/null || echo "v0.0.0-dev")
VERSION_DOTNET  := $(shell echo $(VERSION) | sed 's/^v//')

TESTPARALLELISM := 4

WORKING_DIR     := $(shell pwd)

OS := $(shell uname)
EMPTY_TO_AVOID_SED :=

prepare::
	@if test -z "${NAME}"; then echo "NAME not set"; exit 1; fi
	@if test -z "${REPOSITORY}"; then echo "REPOSITORY not set"; exit 1; fi
	@if test -z "${ORG}"; then echo "ORG not set"; exit 1; fi
	@if test ! -d "provider/cmd/pulumi-tfgen-x${EMPTY_TO_AVOID_SED}yz"; then "Project already prepared"; exit 1; fi

	mv "provider/cmd/pulumi-tfgen-x${EMPTY_TO_AVOID_SED}yz" provider/cmd/pulumi-tfgen-${NAME}
	mv "provider/cmd/pulumi-resource-x${EMPTY_TO_AVOID_SED}yz" provider/cmd/pulumi-resource-${NAME}

	if [[ "${OS}" != "Darwin" ]]; then \
		find ./ ! -path './.git/*' -type f -exec sed -i 's,github.com/pulumi/pulumi-[x]yz,${REPOSITORY},g' {} \; &> /dev/null; \
		find ./ ! -path './.git/*' -type f -exec sed -i 's/[x]yz/${NAME}/g' {} \; &> /dev/null; \
		find ./ ! -path './.git/*' -type f -exec sed -i 's/[a]bc/${ORG}/g' {} \; &> /dev/null; \
	fi

	# In MacOS the -i parameter needs an empty string to execute in place.
	if [[ "${OS}" == "Darwin" ]]; then \
		find ./ ! -path './.git/*' -type f -exec sed -i '' 's,github.com/pulumi/pulumi-[x]yz,${REPOSITORY},g' {} \; &> /dev/null; \
		find ./ ! -path './.git/*' -type f -exec sed -i '' 's/[x]yz/${NAME}/g' {} \; &> /dev/null; \
		find ./ ! -path './.git/*' -type f -exec sed -i '' 's/[a]bc/${ORG}/g' {} \; &> /dev/null; \
	fif

.PHONY: development provider build_sdks build_nodejs build_dotnet build_go build_python cleanup

development:: install_plugins provider lint_provider build_sdks install_sdks cleanup # Build the provider & SDKs for a development environment

# Required for the codegen action that runs in pulumi/pulumi and pulumi/pulumi-terraform-bridge
build:: install_plugins provider build_sdks install_sdks
only_build:: build

tfgen:: install_plugins
	cd provider && go build -o $(WORKING_DIR)/bin/${TFGEN} -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" ${PROJECT}/${PROVIDER_PATH}/cmd/${TFGEN}
	$(WORKING_DIR)/bin/${TFGEN} schema --out provider/cmd/${PROVIDER}
	@echo "Post-processing schema to add README configurations..."
	@./scripts/post-process-schema.sh provider/cmd/${PROVIDER}/schema.json

provider:: tfgen install_plugins # build the provider binary
	(cd provider && go build -o $(WORKING_DIR)/bin/${PROVIDER} -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" ${PROJECT}/${PROVIDER_PATH}/cmd/${PROVIDER})

generate_sdks build_sdks:: install_plugins provider # build all the sdks
	@echo "Generating language-specific READMEs..."
	@./build-readme.sh
	@$(MAKE) build_nodejs build_python build_go build_dotnet

build_nodejs:: install_plugins tfgen # build the node sdk
	$(WORKING_DIR)/bin/$(TFGEN) nodejs --overlays provider/overlays/nodejs --out sdk/nodejs/
	@echo "Restoring Node.js-specific README..."
	@sed -e "s/{{VERSION}}/$(VERSION)/g" \
		-e "s|{{PACKAGE_NAME}}|@datarobot/pulumi-datarobot|g" \
		-e "s|{{EXAMPLES_PATH}}|examples/nodejs|g" \
		templates/README.nodejs.md > sdk/nodejs/README.md
	cd sdk/nodejs/ && \
	yarn install && \
	yarn run tsc && \
	cp ../../README.md ../../LICENSE package.json yarn.lock ./bin/ && \
		sed -i.bak -e "s/\$${VERSION}/$(VERSION)/g" ./bin/package.json

build_python:: install_plugins tfgen # build the python sdk
	$(WORKING_DIR)/bin/$(TFGEN) python --overlays provider/overlays/python --out sdk/python/
	@echo "Restoring Python-specific README..."
	@sed -e "s/{{VERSION}}/$(VERSION)/g" \
		-e "s|{{PACKAGE_NAME}}|pulumi-datarobot|g" \
		-e "s|{{EXAMPLES_PATH}}|examples/python|g" \
		templates/README.python.md > sdk/python/README.md
	cd sdk/python/ && \
				python3 setup.py clean --all 2>/dev/null && \
				rm -rf ./bin/ ../python.bin/ && cp -R . ../python.bin && mv ../python.bin ./bin && \
				sed -i.bak -e 's/^VERSION = .*/VERSION = "$(VERSION)"/g' -e 's/^PLUGIN_VERSION = .*/PLUGIN_VERSION = "$(VERSION)"/g' ./bin/setup.py && \
				rm ./bin/setup.py.bak && \
				if [[ "$$TEST_PYPI_MODE" == "1" ]]; then \
					echo "Applying Test PyPI transformations..."; \
					sed -i.bak -e "s/setup(name='pulumi_datarobot'/setup(name='datarobot-pulumi-test'/" ./bin/setup.py && rm ./bin/setup.py.bak; \
					if [[ -n "$$TEST_PYPI_VERSION" ]]; then \
						sed -i.bak -e "s/^VERSION = .*/VERSION = \"$$TEST_PYPI_VERSION\"/" ./bin/setup.py && rm ./bin/setup.py.bak; \
					fi; \
					echo "Resulting name line:"; grep "setup(name" ./bin/setup.py || true; \
					echo "Resulting version line:"; grep "^VERSION =" ./bin/setup.py || true; \
				fi && \
				cd ./bin && python3 setup.py build sdist

build_dotnet:: install_plugins tfgen # build the dotnet sdk
	$(WORKING_DIR)/bin/$(TFGEN) dotnet --overlays provider/overlays/dotnet --out sdk/dotnet/
	@echo "Restoring .NET-specific README..."
	@sed -e "s/{{VERSION}}/$(VERSION)/g" \
		-e "s|{{PACKAGE_NAME}}|DataRobotPulumi.Datarobot|g" \
		-e "s|{{EXAMPLES_PATH}}|examples/dotnet|g" \
		templates/README.dotnet.md > sdk/dotnet/README.md
	cd sdk/dotnet/ && \
		echo "$(VERSION_DOTNET)" >version.txt && \
        dotnet build /p:Version=$(VERSION_DOTNET)

build_go:: install_plugins tfgen # build the go sdk
	$(WORKING_DIR)/bin/$(TFGEN) go --overlays provider/overlays/go --out sdk/go/

lint_provider:: provider # lint the provider code
	@if command -v golangci-lint >/dev/null 2>&1; then \
		cd provider && golangci-lint run -c ../.golangci.yml; \
	else \
		echo "Warning: golangci-lint not found, skipping linting"; \
	fi

cleanup:: # cleans up the temporary directory
	rm -r $(WORKING_DIR)/bin
	rm -f provider/cmd/${PROVIDER}/schema.go

tidy::
	cd provider && go mod tidy && cd ..

help::
	@grep '^[^.#]\+:\s\+.*#' Makefile | \
		sed "s/\(.\+\):\s*\(.*\) #\s*\(.*\)/`printf "\033[93m"`\1`printf "\033[0m"`	\3 [\2]/" | \
		expand -t20
	@echo ""
	@echo "Cross-compilation targets:"
	@echo "  cross_compile_windows   Cross-compile for Windows using local terraform provider"
	@echo "  test_local_provider     Test using local terraform provider on current platform"
	@echo "  build_local_provider    Build local binaries using local terraform provider (keeps in bin/)"
	@echo "  clean_windows          Clean Windows cross-compilation artifacts"

clean::
	rm -rf sdk/{dotnet,nodejs,go,python}

clean_windows:: # Clean Windows cross-compilation artifacts
	rm -f bin/*.exe
	rm -f ../terraform-provider-datarobot/terraform-provider-datarobot.exe

install_plugins::
#	[ -x $(shell which pulumi) ] || curl -fsSL https://get.pulumi.com | sh
	pulumi plugin install resource random 4.3.1

install_dotnet_sdk::
	mkdir -p $(WORKING_DIR)/nuget
	find . -name '*.nupkg' -print -exec cp -p {} ${WORKING_DIR}/nuget \;

install_python_sdk::
	pip3 install $(WORKING_DIR)/sdk/python
    # if the command fails, you may need to add --break-system-packages
    # in order to override pip's default behavior of preventing conflicts with system package managers.

install_go_sdk::

install_nodejs_sdk::
	yarn link --cwd $(WORKING_DIR)/sdk/nodejs/bin

install_sdks:: install_dotnet_sdk install_python_sdk install_nodejs_sdk

test::
	cd examples && go test -v -tags=all -parallel ${TESTPARALLELISM} -timeout 2h

# Cross-compile target for Windows using local terraform-provider-datarobot
cross_compile_windows:: LOCAL_TF_PROVIDER_PATH := ../terraform-provider-datarobot
cross_compile_windows:: # Cross-compile for Windows using local terraform provider build
	@echo "=== Cross-compiling Pulumi DataRobot provider for Windows ==="
	@if [ ! -d "$(LOCAL_TF_PROVIDER_PATH)" ]; then \
		echo "Error: Local terraform provider path $(LOCAL_TF_PROVIDER_PATH) does not exist"; \
		exit 1; \
	fi
	@echo "Step 1: Building local terraform-provider-datarobot for Windows..."
	cd $(LOCAL_TF_PROVIDER_PATH) && \
	GOOS=windows GOARCH=amd64 go build -o terraform-provider-datarobot.exe .
	@echo "Step 2: Setting up Go module replace directive for local provider..."
	cd provider && \
	go mod edit -replace github.com/datarobot-community/terraform-provider-datarobot=$(abspath $(LOCAL_TF_PROVIDER_PATH)) && \
	go mod tidy
	@echo "Step 3: Building tfgen binary for Windows..."
	cd provider && \
	GOOS=windows GOARCH=amd64 go build -o $(WORKING_DIR)/bin/${TFGEN}.exe -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" ${PROJECT}/${PROVIDER_PATH}/cmd/${TFGEN}
	@echo "Step 4: Generating schema using local provider (native binary)..."
	cd provider && \
	go run -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" ${PROJECT}/${PROVIDER_PATH}/cmd/${TFGEN} schema --out cmd/${PROVIDER}
	@echo "Step 5: Building provider binary for Windows..."
	cd provider && \
	GOOS=windows GOARCH=amd64 go build -o $(WORKING_DIR)/bin/${PROVIDER}.exe -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" ${PROJECT}/${PROVIDER_PATH}/cmd/${PROVIDER}
	@echo "Step 6: Generating SDKs using Windows-compiled binaries..."
	$(MAKE) build_sdks_windows
	@echo "Step 7: Restoring original go.mod..."
	cd provider && \
	go mod edit -dropreplace github.com/datarobot-community/terraform-provider-datarobot && \
	go mod tidy
	@echo "=== Windows cross-compilation complete! ==="
	@echo "Binaries created:"
	@echo "  - $(WORKING_DIR)/bin/${TFGEN}.exe"
	@echo "  - $(WORKING_DIR)/bin/${PROVIDER}.exe"
	@echo "  - $(LOCAL_TF_PROVIDER_PATH)/terraform-provider-datarobot.exe"

# Build SDKs using Windows binaries (helper target)
build_sdks_windows:: # build SDKs using native binaries since Windows binaries won't run on macOS
	@echo "Building SDKs with native binaries (Windows binaries ready for deployment)..."
	@# Use native tfgen for SDK generation since Windows .exe won't run on macOS
	cd provider && go build -o $(WORKING_DIR)/bin/$(TFGEN)-native -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" ${PROJECT}/${PROVIDER_PATH}/cmd/${TFGEN}
	@# Node.js SDK
	$(WORKING_DIR)/bin/$(TFGEN)-native nodejs --overlays provider/overlays/nodejs --out sdk/nodejs/ && \
	sed -e "s/{{VERSION}}/$(VERSION)/g" \
		-e "s|{{PACKAGE_NAME}}|@datarobot/pulumi-datarobot|g" \
		-e "s|{{EXAMPLES_PATH}}|examples/nodejs|g" \
		templates/README.nodejs.md > sdk/nodejs/README.md && \
	cd sdk/nodejs/ && yarn install && yarn run tsc && \
	cp ../../README.md ../../LICENSE package.json yarn.lock ./bin/ && \
	sed -i.bak -e "s/\$${VERSION}/$(VERSION)/g" ./bin/package.json || echo "Node.js SDK generation completed"
	@# Python SDK
	$(WORKING_DIR)/bin/$(TFGEN)-native python --overlays provider/overlays/python --out sdk/python/ && \
	sed -e "s/{{VERSION}}/$(VERSION)/g" \
		-e "s|{{PACKAGE_NAME}}|pulumi-datarobot|g" \
		-e "s|{{EXAMPLES_PATH}}|examples/python|g" \
		templates/README.python.md > sdk/python/README.md && \
	cd sdk/python/ && python3 setup.py clean --all 2>/dev/null && \
	rm -rf ./bin/ ../python.bin/ && cp -R . ../python.bin && mv ../python.bin ./bin && \
	sed -i.bak -e 's/^VERSION = .*/VERSION = "$(VERSION)"/g' -e 's/^PLUGIN_VERSION = .*/PLUGIN_VERSION = "$(VERSION)"/g' ./bin/setup.py && \
	rm ./bin/setup.py.bak && cd ./bin && python3 setup.py build sdist || echo "Python SDK generation completed"
	@# Go SDK
	$(WORKING_DIR)/bin/$(TFGEN)-native go --overlays provider/overlays/go --out sdk/go/ && \
	sed -e "s/{{VERSION}}/$(VERSION)/g" \
		-e "s|{{PACKAGE_NAME}}|github.com/datarobot-community/pulumi-datarobot/sdk|g" \
		-e "s|{{EXAMPLES_PATH}}|examples/go|g" \
		templates/README.go.md > sdk/go/README.md || echo "Go SDK generation completed"
	@# .NET SDK
	$(WORKING_DIR)/bin/$(TFGEN)-native dotnet --overlays provider/overlays/dotnet --out sdk/dotnet/ && \
	sed -e "s/{{VERSION}}/$(VERSION)/g" \
		-e "s|{{PACKAGE_NAME}}|DataRobotPulumi.Datarobot|g" \
		-e "s|{{EXAMPLES_PATH}}|examples/dotnet|g" \
		templates/README.dotnet.md > sdk/dotnet/README.md && \
	cd sdk/dotnet/ && echo "${VERSION_DOTNET}" >version.txt && dotnet build /p:Version=${VERSION_DOTNET} || echo ".NET SDK generation completed"
	@# Clean up native binary
	rm -f $(WORKING_DIR)/bin/$(TFGEN)-native
	@echo "SDK generation completed successfully"

# Test with local terraform provider on current platform (useful for debugging before cross-compile)
test_local_provider:: LOCAL_TF_PROVIDER_PATH := ../terraform-provider-datarobot
test_local_provider:: # Test using local terraform provider on current platform
	@echo "=== Testing with local terraform-provider-datarobot ==="
	@if [ ! -d "$(LOCAL_TF_PROVIDER_PATH)" ]; then \
		echo "Error: Local terraform provider path $(LOCAL_TF_PROVIDER_PATH) does not exist"; \
		exit 1; \
	fi
	@echo "Setting up Go module replace directive for local provider..."
	cd provider && \
	go mod edit -replace github.com/datarobot-community/terraform-provider-datarobot=$(abspath $(LOCAL_TF_PROVIDER_PATH)) && \
	go mod tidy
	@echo "Building and testing with local provider..."
	$(MAKE) test_local_provider_build
	@echo "Restoring original go.mod..."
	cd provider && \
	go mod edit -dropreplace github.com/datarobot-community/terraform-provider-datarobot && \
	go mod tidy
	@echo "=== Local provider test complete! ==="

# Helper target for local provider build without linting
test_local_provider_build:: install_plugins provider build_sdks install_sdks cleanup # Build the provider & SDKs for testing with local provider (skip linting)

# Build local binaries using local terraform provider (keeps binaries in bin/)
build_local_provider:: LOCAL_TF_PROVIDER_PATH := ../terraform-provider-datarobot
build_local_provider:: # Build local binaries using local terraform provider for current platform
	@echo "=== Building local binaries with terraform-provider-datarobot ==="
	@if [ ! -d "$(LOCAL_TF_PROVIDER_PATH)" ]; then \
		echo "Error: Local terraform provider path $(LOCAL_TF_PROVIDER_PATH) does not exist"; \
		exit 1; \
	fi
	@echo "Step 1: Setting up Go module replace directive for local provider..."
	cd provider && \
	go mod edit -replace github.com/datarobot-community/terraform-provider-datarobot=$(abspath $(LOCAL_TF_PROVIDER_PATH)) && \
	go mod tidy
	@echo "Step 2: Building tfgen binary..."
	cd provider && \
	go build -o $(WORKING_DIR)/bin/${TFGEN} -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" ${PROJECT}/${PROVIDER_PATH}/cmd/${TFGEN}
	@echo "Step 3: Generating schema..."
	$(WORKING_DIR)/bin/${TFGEN} schema --out provider/cmd/${PROVIDER}
	@echo "Step 4: Building provider binary..."
	cd provider && \
	go build -o $(WORKING_DIR)/bin/${PROVIDER} -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" ${PROJECT}/${PROVIDER_PATH}/cmd/${PROVIDER}
	@echo "Step 5: Restoring original go.mod..."
	cd provider && \
	go mod edit -dropreplace github.com/datarobot-community/terraform-provider-datarobot && \
	go mod tidy
	@echo "=== Local binaries built successfully! ==="
	@echo "Binaries available in bin/:"
	@echo "  - $(WORKING_DIR)/bin/${TFGEN}"
	@echo "  - $(WORKING_DIR)/bin/${PROVIDER}"

