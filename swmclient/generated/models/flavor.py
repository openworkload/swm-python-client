from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Flavor")


@attr.s(auto_attribs=True)
class Flavor:
    """A flavor information that is known to SkyPort"""

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    remote_id: Union[Unset, str] = UNSET
    cpus: Union[Unset, int] = UNSET
    mem: Union[Unset, int] = UNSET
    storage: Union[Unset, int] = UNSET
    price: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        remote_id = self.remote_id
        cpus = self.cpus
        mem = self.mem
        storage = self.storage
        price = self.price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if remote_id is not UNSET:
            field_dict["remote_id"] = remote_id
        if cpus is not UNSET:
            field_dict["cpus"] = cpus
        if mem is not UNSET:
            field_dict["mem"] = mem
        if storage is not UNSET:
            field_dict["storage"] = storage
        if price is not UNSET:
            field_dict["price"] = price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        remote_id = d.pop("remote_id", UNSET)

        cpus = d.pop("cpus", UNSET)

        mem = d.pop("mem", UNSET)

        storage = d.pop("storage", UNSET)

        price = d.pop("price", UNSET)

        flavor = cls(
            id=id,
            name=name,
            remote_id=remote_id,
            cpus=cpus,
            mem=mem,
            storage=storage,
            price=price,
        )

        flavor.additional_properties = d
        return flavor

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
