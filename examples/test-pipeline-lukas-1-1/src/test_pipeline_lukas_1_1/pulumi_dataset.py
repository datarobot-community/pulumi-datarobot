from kedro.io import AbstractDataset, MemoryDataset
from pulumi import Output


class PulumiResourceDataSet(AbstractDataset):
    def __init__(self, resource_type, resource_args):
        self._resource_type = resource_type
        self._resource_args = resource_args
        self._resource = None

    def _load(self) -> dict:
        if self._resource is None:
            raise ValueError("Resource has not been created yet")
        return {
            "resource_type": self._resource_type,
            "resource_args": self._resource_args,
            "resource_id": self._resource.id,
        }

    def _save(self, data: Output):
        self._resource = data

    def _describe(self):
        return dict(
            resource_type=self._resource_type, resource_args=self._resource_args
        )
