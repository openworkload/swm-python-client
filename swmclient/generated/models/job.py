from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.job_state import JobState
from ..types import UNSET, Unset

T = TypeVar("T", bound="Job")


@attr.s(auto_attribs=True)
class Job:
    """A job information that is known to SkyPort"""

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    state: Union[Unset, JobState] = UNSET
    submit_time: Union[Unset, str] = UNSET
    start_time: Union[Unset, str] = UNSET
    end_time: Union[Unset, str] = UNSET
    duration: Union[Unset, int] = UNSET
    exitcode: Union[Unset, int] = UNSET
    signal: Union[Unset, int] = UNSET
    node_names: Union[Unset, List[str]] = UNSET
    remote_id: Union[Unset, str] = UNSET
    flavor_id: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        submit_time = self.submit_time
        start_time = self.start_time
        end_time = self.end_time
        duration = self.duration
        exitcode = self.exitcode
        signal = self.signal
        node_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.node_names, Unset):
            node_names = self.node_names

        remote_id = self.remote_id
        flavor_id = self.flavor_id
        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if state is not UNSET:
            field_dict["state"] = state
        if submit_time is not UNSET:
            field_dict["submit_time"] = submit_time
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if duration is not UNSET:
            field_dict["duration"] = duration
        if exitcode is not UNSET:
            field_dict["exitcode"] = exitcode
        if signal is not UNSET:
            field_dict["signal"] = signal
        if node_names is not UNSET:
            field_dict["node_names"] = node_names
        if remote_id is not UNSET:
            field_dict["remote_id"] = remote_id
        if flavor_id is not UNSET:
            field_dict["flavor_id"] = flavor_id
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, JobState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = JobState(_state)

        submit_time = d.pop("submit_time", UNSET)

        start_time = d.pop("start_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        duration = d.pop("duration", UNSET)

        exitcode = d.pop("exitcode", UNSET)

        signal = d.pop("signal", UNSET)

        node_names = cast(List[str], d.pop("node_names", UNSET))

        remote_id = d.pop("remote_id", UNSET)

        flavor_id = d.pop("flavor_id", UNSET)

        comment = d.pop("comment", UNSET)

        job = cls(
            id=id,
            name=name,
            state=state,
            submit_time=submit_time,
            start_time=start_time,
            end_time=end_time,
            duration=duration,
            exitcode=exitcode,
            signal=signal,
            node_names=node_names,
            remote_id=remote_id,
            flavor_id=flavor_id,
            comment=comment,
        )

        job.additional_properties = d
        return job

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
