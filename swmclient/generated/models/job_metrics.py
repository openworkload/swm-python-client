from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.metric_avg_max import MetricAvgMax

T = TypeVar("T", bound="JobMetrics")


@attr.s(auto_attribs=True)
class JobMetrics:
    """Per-job resource metrics from Prometheus (Porter samples scraped from Sky Port gauges).
    Missing series are null.

    Attributes:
        job_id (str): Job ID
        cpu_percent (MetricAvgMax): Aggregated average and maximum for one metric over the job lifetime
        mem_bytes (MetricAvgMax): Aggregated average and maximum for one metric over the job lifetime
        gpu_util_percent (MetricAvgMax): Aggregated average and maximum for one metric over the job lifetime
        gpu_mem_bytes (MetricAvgMax): Aggregated average and maximum for one metric over the job lifetime
    """

    job_id: str
    cpu_percent: "MetricAvgMax"
    mem_bytes: "MetricAvgMax"
    gpu_util_percent: "MetricAvgMax"
    gpu_mem_bytes: "MetricAvgMax"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_id = self.job_id
        cpu_percent = self.cpu_percent.to_dict()
        mem_bytes = self.mem_bytes.to_dict()
        gpu_util_percent = self.gpu_util_percent.to_dict()
        gpu_mem_bytes = self.gpu_mem_bytes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_id": job_id,
                "cpu_percent": cpu_percent,
                "mem_bytes": mem_bytes,
                "gpu_util_percent": gpu_util_percent,
                "gpu_mem_bytes": gpu_mem_bytes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.metric_avg_max import MetricAvgMax

        d = src_dict.copy()
        job_id = d.pop("job_id")
        cpu_percent = MetricAvgMax.from_dict(d.pop("cpu_percent"))
        mem_bytes = MetricAvgMax.from_dict(d.pop("mem_bytes"))
        gpu_util_percent = MetricAvgMax.from_dict(d.pop("gpu_util_percent"))
        gpu_mem_bytes = MetricAvgMax.from_dict(d.pop("gpu_mem_bytes"))

        job_metrics = cls(
            job_id=job_id,
            cpu_percent=cpu_percent,
            mem_bytes=mem_bytes,
            gpu_util_percent=gpu_util_percent,
            gpu_mem_bytes=gpu_mem_bytes,
        )

        job_metrics.additional_properties = d
        return job_metrics

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
