from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.job_state import JobState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource import Resource


T = TypeVar("T", bound="Job")


@attr.s(auto_attribs=True)
class Job:
    """A job information that is known to Sky Port

    Attributes:
        id (Union[Unset, str]): Job ID
        name (Union[Unset, str]): Job name
        state (Union[Unset, JobState]): Current job state
        state_details (Union[Unset, str]): Job state details
        submit_time (Union[Unset, str]): Job submit time
        start_time (Union[Unset, str]): Job start time
        end_time (Union[Unset, str]): Job end time
        duration (Union[Unset, int]): Job run time
        exitcode (Union[Unset, int]): Job exit code
        signal (Union[Unset, int]): Signal if job is terminated with a signal
        node_names (Union[Unset, List[str]]): List of hostnames of nodes allocated for job
        node_ips (Union[Unset, List[str]]): List of node IP addresses allocated for job
        remote_id (Union[Unset, str]): Remote site ID
        flavor_id (Union[Unset, str]): Node flavor ID
        request (Union[Unset, List['Resource']]): List of resources that are requested by job
        resources (Union[Unset, List['Resource']]): List of resources that are actually allocated for job
        comment (Union[Unset, str]): A comment associated with job
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    state: Union[Unset, JobState] = UNSET
    state_details: Union[Unset, str] = UNSET
    submit_time: Union[Unset, str] = UNSET
    start_time: Union[Unset, str] = UNSET
    end_time: Union[Unset, str] = UNSET
    duration: Union[Unset, int] = UNSET
    exitcode: Union[Unset, int] = UNSET
    signal: Union[Unset, int] = UNSET
    node_names: Union[Unset, List[str]] = UNSET
    node_ips: Union[Unset, List[str]] = UNSET
    remote_id: Union[Unset, str] = UNSET
    flavor_id: Union[Unset, str] = UNSET
    request: Union[Unset, List["Resource"]] = UNSET
    resources: Union[Unset, List["Resource"]] = UNSET
    comment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        state_details = self.state_details
        submit_time = self.submit_time
        start_time = self.start_time
        end_time = self.end_time
        duration = self.duration
        exitcode = self.exitcode
        signal = self.signal
        node_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.node_names, Unset):
            node_names = self.node_names

        node_ips: Union[Unset, List[str]] = UNSET
        if not isinstance(self.node_ips, Unset):
            node_ips = self.node_ips

        remote_id = self.remote_id
        flavor_id = self.flavor_id
        request: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.request, Unset):
            request = []
            for request_item_data in self.request:
                request_item = request_item_data.to_dict()

                request.append(request_item)

        resources: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.resources, Unset):
            resources = []
            for resources_item_data in self.resources:
                resources_item = resources_item_data.to_dict()

                resources.append(resources_item)

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
        if state_details is not UNSET:
            field_dict["state_details"] = state_details
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
        if node_ips is not UNSET:
            field_dict["node_ips"] = node_ips
        if remote_id is not UNSET:
            field_dict["remote_id"] = remote_id
        if flavor_id is not UNSET:
            field_dict["flavor_id"] = flavor_id
        if request is not UNSET:
            field_dict["request"] = request
        if resources is not UNSET:
            field_dict["resources"] = resources
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.resource import Resource

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, JobState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = JobState(_state)

        state_details = d.pop("state_details", UNSET)

        submit_time = d.pop("submit_time", UNSET)

        start_time = d.pop("start_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        duration = d.pop("duration", UNSET)

        exitcode = d.pop("exitcode", UNSET)

        signal = d.pop("signal", UNSET)

        node_names = cast(List[str], d.pop("node_names", UNSET))

        node_ips = cast(List[str], d.pop("node_ips", UNSET))

        remote_id = d.pop("remote_id", UNSET)

        flavor_id = d.pop("flavor_id", UNSET)

        request = []
        _request = d.pop("request", UNSET)
        for request_item_data in _request or []:
            request_item = Resource.from_dict(request_item_data)

            request.append(request_item)

        resources = []
        _resources = d.pop("resources", UNSET)
        for resources_item_data in _resources or []:
            resources_item = Resource.from_dict(resources_item_data)

            resources.append(resources_item)

        comment = d.pop("comment", UNSET)

        job = cls(
            id=id,
            name=name,
            state=state,
            state_details=state_details,
            submit_time=submit_time,
            start_time=start_time,
            end_time=end_time,
            duration=duration,
            exitcode=exitcode,
            signal=signal,
            node_names=node_names,
            node_ips=node_ips,
            remote_id=remote_id,
            flavor_id=flavor_id,
            request=request,
            resources=resources,
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
