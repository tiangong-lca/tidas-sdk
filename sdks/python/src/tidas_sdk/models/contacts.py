"""
TidasContacts entity wrapper class for TIDAS SDK.
"""

import datetime
import uuid
from typing import Any, Dict, Optional

from ..core.base import TidasEntity
from ..core.wrappers.contacts_wrappers import ContactsDataSetWrapper
from ..core.validation import ValidationConfig
from ..types.tidas_contacts import Model as ContactsModel


class TidasContacts(TidasEntity):
    """Wrapper class for Contacts entities with pythonic API.

    Represents a contacts in LCA.

    Example:
        >>> contacts = TidasContacts()
        >>> contacts.contacts_data_set.contacts_information.data_set_information.name.set_text(
        ...     "Example Contacts", "en"
        ... )
        >>> contacts.validate()
    """

    def __init__(
        self,
        data: Optional[Dict[str, Any]] = None,
        validation_config: Optional[ValidationConfig] = None,
    ):
        """Initialize Contacts entity.

        Args:
            data: Contacts data as dictionary (TIDAS JSON format)
            validation_config: Validation configuration. If None, uses global default.
        """
        super().__init__(data, validation_config)
        self._pydantic_model = ContactsModel

        # Initialize default structure if data is empty
        if not self._data:
            self._data = {
                "contactDataSet": {
                    "contactsInformation": {
                        "dataSetInformation": {}
                    },
                    "modellingAndValidation": {},
                    "administrativeInformation": {}
                }
            }

    def initialize_defaults(self) -> None:
        """Initialize default values and ensure required structure.

        This method is called during initialization to set up
        required namespace attributes and default field values.
        """

    @property
    def contacts_data_set(self) -> ContactsDataSetWrapper:
        """Access contactDataSet field with IDE autocomplete and type hints.

        This property provides typed access to the dataset, enabling
        IDE autocomplete for all nested fields.

        Example:
            >>> contacts = TidasContacts()
            >>> # IDE shows autocomplete as you type:
            >>> contacts.contacts_data_set.contacts_information.data_set_information.uuid = "..."
        """
        return self._get_typed_field("contactDataSet", ContactsDataSetWrapper)
