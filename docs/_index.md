---
title: DataRobot
meta_desc: Provides an overview of the DataRobot Provider for Pulumi.
layout: package
---

The `DataRobot` provider for Pulumi can be used to provision any of the resources available with [DataRobot]((https://www.datarobot.com/).

## Example

{{< chooser language "python,typescript,yaml" >}}

{{% /choosable %}}

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumiverse_datartobot as datarobot
import pulumi

use_case = datarobot.UseCase("example fom python",
                            name="example use case",
                            description="pulumi"
)

playground = datarobot.Playground("playground",
                                name="example playground",
                                use_case_id=use_case.id,
)
```

{{% /choosable %}}

{{< /chooser >}}