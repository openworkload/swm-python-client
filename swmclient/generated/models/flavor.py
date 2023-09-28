from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource import Resource


T = TypeVar("T", bound="Flavor")


@_attrs_define
class Flavor:
    """A flavor information that is known to Sky Port

    Attributes:
        id (Union[Unset, str]): Flavor ID
        name (Union[Unset, str]): Flavor name
        remote_id (Union[Unset, str]): Related remote object ID configured in swm-core
        resources (Union[Unset, List['Resource']]): List of resources flavor provides
        price (Union[Unset, float]): Price of a node of this flavor per hour
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    remote_id: Union[Unset, str] = UNSET
    resources: Union[Unset, List["Resource"]] = UNSET
    price: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        remote_id = self.remote_id
        resources: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.resources, Unset):
            resources = []
            for resources_item_data in self.resources:
                resources_item = resources_item_data.to_dict()

                resources.append(resources_item)

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
        if resources is not UNSET:
            field_dict["resources"] = resources
        if price is not UNSET:
            field_dict["price"] = price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.resource import Resource

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        remote_id = d.pop("remote_id", UNSET)

        resources = []
        _resources = d.pop("resources", UNSET)
        for resources_item_data in _resources or []:
            resources_item = Resource.from_dict(resources_item_data)

            resources.append(resources_item)

        price = d.pop("price", UNSET)

        flavor = cls(
            id=id,
            name=name,
            remote_id=remote_id,
            resources=resources,
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
