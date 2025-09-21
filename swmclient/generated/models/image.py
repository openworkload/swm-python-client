from typing import Any, Dict, List, Type, Union, TypeVar

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Image")


@attr.s(auto_attribs=True)
class Image:
    """A virtual machine or container image information

    Attributes:
        id (Union[Unset, str]): Image ID
        name (Union[Unset, str]): Image name
        remote_id (Union[Unset, str]): Related remote object ID configured in swm-core
        kind (Union[Unset, str]): Image kind
        comment (Union[Unset, str]): Image comment
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    remote_id: Union[Unset, str] = UNSET
    kind: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        remote_id = self.remote_id
        kind = self.kind
        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if remote_id is not UNSET:
            field_dict["remote_id"] = remote_id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        remote_id = d.pop("remote_id", UNSET)

        kind = d.pop("kind", UNSET)

        comment = d.pop("comment", UNSET)

        image = cls(
            id=id,
            name=name,
            remote_id=remote_id,
            kind=kind,
            comment=comment,
        )

        image.additional_properties = d
        return image

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
