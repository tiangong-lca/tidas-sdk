"""Auto-generated builder classes for TIDAS entities."""

# Builders enable incremental construction of complex TIDAS entities
# Usage:
#   from tidas_sdk.builders import ContactBuilder
#   builder = ContactBuilder()
#   builder.contact_data_set.contact_information.data_set_information.email = 'test@example.com'
#   contact = builder.build()

from .tidas_contacts_builders import *
from .tidas_flowproperties_builders import *
from .tidas_flows_builders import *
from .tidas_lciamethods_builders import *
from .tidas_lifecyclemodels_builders import *
from .tidas_processes_builders import *
from .tidas_sources_builders import *
from .tidas_unitgroups_builders import *

__all__ = [
    "# All builder classes are exported"
]
