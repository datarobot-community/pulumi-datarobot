# Pulumi: minimal Workload replacement example

Pulumi port of `terraform-provider-datarobot`'s
[`examples/workflows/workload_replacement/main.tf`](../../../../terraform-provider-datarobot/examples/workflows/workload_replacement/main.tf).

## How it triggers a replacement

Two independent `Artifact`/`Workload` pairs — (`app-1`, `api-1`) and
(`app-2`, `api-2`) — defined in [`__main__.py`](__main__.py), so you can
trigger and observe replacement on each one separately (or both at once):

- Each artifact's `image_uri` is driven by its own Pulumi config value
  (`containerImage1` / `containerImage2`, both default to
  `containous/whoami:latest`).
- Artifacts default to `status="locked"`, so any spec change — changing
  either `containerImage1`/`containerImage2` — makes Pulumi create a **new
  artifact version with a new `artifact_id`** on the next `pulumi up`,
  instead of updating in place.
- Each workload's `artifact_id` is wired to its own artifact's
  `artifact_id`. Per the `Workload` schema, changing `artifact_id` forces an
  **in-place replacement** of that workload (`workload_id` /
  `workload_endpoint` stay stable — only the running version behind them
  changes). The two pairs are independent: changing `containerImage1` only
  replaces `api-1`, and vice versa.

Uses the public `containous/whoami:latest` image via `image_uri` directly —
no `source`/`image_build_config`, so there's no server-side image build step.

## Setup

```bash
cd examples/py/workload_replacement
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e ../../../sdk/python/bin   # or: pip install pulumi-datarobot

pulumi stack init dev   # or: pulumi stack select dev
pulumi config set datarobot:apikey <your-api-token> --secret
```

## Run it

**1. First deploy** — creates both pairs: `app-1`/`api-1` and `app-2`/`api-2`,
each serving `containous/whoami:latest`:

```bash
pulumi up
```

**2. Trigger replacement on one, both, or each independently:**

```bash
# Replace only workload 1
pulumi config set containerImage1 containous/whoami:v1.5.0 && pulumi up

# Replace only workload 2
pulumi config set containerImage2 containous/whoami:v1.5.0 && pulumi up

# Replace both at once
pulumi config set containerImage1 containous/whoami:v1.5.0
pulumi config set containerImage2 containous/whoami:v1.5.0
pulumi up
```

`pulumi up` will show, for whichever pair(s) you changed:

```text
+-  datarobot:index:Artifact  app-1   replace     # actually a new version, `app-1` itself is created fresh
 ~  datarobot:index:Workload  api-1   update      # artifact_id changed -> triggers in-place replacement
```

(`app-N` is a brand-new `Artifact` resource version under the hood since
it's `locked`; `api-N` keeps its identity — `workload_N_id`/
`workload_N_endpoint` don't change — while the provider swaps the running
version behind it.)

**3. Verify:**

```bash
pulumi stack output artifact_1_version_id   # should differ from before step 2
pulumi stack output artifact_2_version_id
curl "$(pulumi stack output workload_1_endpoint)"
curl "$(pulumi stack output workload_2_endpoint)"
```

`whoami` doesn't print a version label — confirm the swap via
`artifact_1_version_id`/`artifact_2_version_id` changing, or by comparing
the `Hostname`/container id in the curl responses before and after.

## Tear down

```bash
pulumi destroy
```
