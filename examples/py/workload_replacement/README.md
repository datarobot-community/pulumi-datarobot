# Pulumi: minimal Workload replacement example

Pulumi port of `terraform-provider-datarobot`'s
[`examples/workflows/workload_replacement/main.tf`](../../../../terraform-provider-datarobot/examples/workflows/workload_replacement/main.tf).

## How it triggers a replacement

One `Artifact` (`app`) feeding one `Workload` (`api`), defined in
[`__main__.py`](__main__.py):

- `app`'s `image_uri` is driven by the `containerImage` Pulumi config value
  (defaults to `containous/whoami:latest`).
- Artifacts default to `status="locked"`, so any spec change — changing
  `containerImage` — makes Pulumi create a **new artifact version with a new
  `artifact_id`** on the next `pulumi up`, instead of updating in place.
- `api.artifact_id` is wired to `app.artifact_id`. Per the `Workload` schema,
  changing `artifact_id` forces an **in-place replacement** of the workload
  (`workload_id` and `workload_endpoint` stay stable — only the running
  version behind them changes).

So the whole demo is: change `containerImage`, re-apply, watch `api` get
replaced.

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

**1. First deploy** — creates `app` (Artifact) and `api` (Workload built from
`app`), serving `containous/whoami:latest`:

```bash
pulumi up
```

**2. Trigger the replacement** — change the image and re-apply in one go:

```bash
pulumi config set containerImage containous/whoami:v1.5.0 && pulumi up
```

`pulumi up` will show:

```text
+-  datarobot:index:Artifact  app   replace     # actually a new version, `app` itself is created fresh
 ~  datarobot:index:Workload  api   update      # artifact_id changed -> triggers in-place replacement
```

(`app` is a brand-new `Artifact` resource version under the hood since it's
`locked`; `api` keeps its identity — `workload_id`/`workload_endpoint` don't
change — while the provider swaps the running version behind it.)

**3. Verify:**

```bash
pulumi stack output artifact_version_id   # should differ from before step 2
curl "$(pulumi stack output workload_endpoint)"
```

`whoami` doesn't print a version label — confirm the swap via
`artifact_version_id` changing, or by comparing the `Hostname`/container id
in the curl response before and after.

## Tear down

```bash
pulumi destroy
```
