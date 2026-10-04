from typing import Any, Dict, List, Type, Union, TypeVar, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetricAvgMax")


@attr.s(auto_attribs=True)
class MetricAvgMax:
    """Aggregated average and maximum for one metric over the job lifetime

    Attributes:
        avg (Union[Unset, None, float]): Average over the query range (null if no samples)
        max_ (Union[Unset, None, float]): Maximum over the query range (null if no samples)
    """

    avg: Union[Unset, None, float] = UNSET
    max_: Union[Unset, None, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        avg: Union[Unset, None, float]
        if isinstance(self.avg, Unset):
            avg = UNSET
        else:
            avg = self.avg

        max_: Union[Unset, None, float]
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg is not UNSET:
            field_dict["avg"] = avg
        if max_ is not UNSET:
            field_dict["max"] = max_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_avg(data: Any) -> Union[Unset, None, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, None, float], data)

        avg = _parse_avg(d.pop("avg", UNSET))

        def _parse_max_(data: Any) -> Union[Unset, None, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, None, float], data)

        max_ = _parse_max_(d.pop("max", UNSET))

        metric_avg_max = cls(
            avg=avg,
            max_=max_,
        )

        metric_avg_max.additional_properties = d
        return metric_avg_max

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
