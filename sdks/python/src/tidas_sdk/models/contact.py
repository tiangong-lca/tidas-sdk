"""
Contact entity wrapper class for TIDAS SDK.
"""

from typing import Any, Dict, Optional

from ..core.base import TidasEntity
from ..core.wrappers.contacts_wrappers import ContactsDataSetWrapper
from ..core.validation import ValidationConfig
from ..types.tidas_contacts import Model as ContactModel


class TidasContact(TidasEntity):
    """Wrapper class for Contact entities with pythonic API.

    Represents a contact or organization in TIDAS/ILCD format.

    Example:
        >>> contact = TidasContact()
        >>> contact.contact_data_set.contact_information.data_set_information.name.set_text(
        ...     "Dr. Jane Smith", "en"
        ... )
        >>> contact.validate()
    """

    def __init__(
        self,
        data: Optional[Dict[str, Any]] = None,
        validation_config: Optional[ValidationConfig] = None,
    ):
        """Initialize Contact entity.

        Args:
            data: Contact data as dictionary (TIDAS JSON format)
            validation_config: Validation configuration. If None, uses global default.
        """
        super().__init__(data, validation_config)
        self._pydantic_model = ContactModel

        # Initialize default structure if data is empty
        if not self._data:
            self._data = {
                "contactDataSet": {
                    "contactInformation": {
                        "dataSetInformation": {}
                    },
                    "administrativeInformation": {}
                }
            }

    @property
    def contact_data_set(self) -> ContactsDataSetWrapper:
        """Access contactDataSet field with IDE autocomplete and type hints.

        This property provides typed access to the contact dataset, enabling
        IDE autocomplete for all nested fields.

        Example:
            >>> contact = TidasContact()
            >>> # IDE shows autocomplete as you type:
            >>> contact.contact_data_set.contact_information.data_set_information.uuid = "..."
            >>> contact.contact_data_set.contact_information.data_set_information.name.set_text(
            ...     "Dr. Smith", "en"
            ... )

        Returns:
            Auto-generated typed wrapper for the contactDataSet field
        """
        return self._get_typed_field("contactDataSet", ContactsDataSetWrapper)
