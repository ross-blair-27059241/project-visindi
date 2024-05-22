#                 COPYRIGHT & LICENSE TERMS NOTICE
# =============================================================================
# All following code and content is © 2024 Ross Blair,
# and falls under the licensing terms of Ross Blair's
# derivative of the Business Source License \(BSL\).
# The precise license and warranty terms of the BSL can be found in the file 
# `LICENSE.BSL.md`, which should have been distributed
# along with this code file.  All other use of original-work code and content
# falling outside of this BSL license is prohibited.
# =============================================================================



""" A module for instantiating the runtime configuration of the DRSF object.

Extended Summary
----------------
The drsf_init_config.py module's `DRSFInitConfig()` class is responsible for
instantiating the runtime configuration of the DRSF object.  Certain "core"
configuration values are defined in this class's attributes, while other
"user-defined" configuration values are retrieved from a`.toml`-
formatted configuration file specified by the caller code.

"""

# Python Standard Library Imports
import tomllib
import os

# Other Python Library Imports

# DRSF Codebase Module Imports
import 



class DRSFInitConfig():
    """ A class encapsulating the configuration for a DRSF object.

    Extended Summary
    ----------------

    Attributes
    ----------

    Methods
    -------

    """

    # Definition of the `__init__()` constructor method and instance-level attributes.
    def __init__(self, drsf_entry_templates_dir: str="", drsf_source_docs_template_dir: str="",
                 drsf_source_docs_dev_dir: str="", drsf_source_docs_staging_dir: str="",
                 drsf_source_docs_build_dir: str=""):

        self._drsf_core_config = self.DRSF_CORE_CONFIG
        self._drsf_entry_templates_dir = drsf_entry_templates_dir
        self._drsf_source_docs_template_dir = drsf_source_docs_template_dir
        self._drsf_source_docs_dev_dir = drsf_source_docs_dev_dir
        self._drsf_source_docs_staging_dir = drsf_source_docs_staging_dir
        self._drsf_source_docs_build_dir = drsf_source_docs_build_dir


    # Definition of any necessary "getter", "setter", and/or "deleter" methods
    # using the `@property` decorator.

    @property
    def drsf_entry_templates_dir(self):
        if self.drsf_entry_templates_dir == "":
            raise AttributeError("The `drsf_entry_templates_dir` directory is currently designated as an empty string.  This attribute's value must define a valid relative file path to a directory containing template files for DRSF entries.  Otherwise critical DRSF functions will fail.")
        elif os.path.exists(os.path.join(os.getcwd(), self.drsf_entry_templates_dir)) != True:
            raise AttributeError("The `drsf_entry_templates_dir` directory does not exist.  This attribute's value must define a valid relative file path to a directory containining template files for DRSF entries.  Otherwise critical DRSF functions will fail.")
        else:
            return self._drsf_entry_templates_dir
    
    @drsf_entry_templates_dir.setter
    def drsf_entry_templates_dir(self, input_dir):
        if input_dir == "":
            raise ValueError("The directory-file-path input to this function is an empty string.  This value must define a valid relative file path to a directory containing template files for DRSF entries.  Otherwise critical DRSF functions will fail.")
        elif os.path.exists(os.path.join(os.getcwd(), input_dir)) != True:
            raise ValueError("The directory-file-path input to this function does not exist.  This value must define a valid relative file path to a directory containing template files for DRSF entries.  Otherwise critical DRSF functions will fail.")
        else:
            self._drsf_entry_templates_dir = input_dir

    @property
    def drsf_source_docs_template_dir(self):
        """ A "getter" method for the DRSF's template-source-docs-directory.

        Notes
        -----
        Unlike the other attributes of the DRSF object that designate important source document directories, you don't necessarily require a template-source-document-directory when instantiating and working with a DRSF.  For example, if you've already created a "DEV" source document directory that the DRSF is being instantiated from, and you have no need to "start from scratch" and re-build that DEV directory, then you'd have no need of this template directory.  Therefore we are not going to raise an AttributeError in the case of an empty string being supplied to our "getter" method.


        """
        if os.path.exists(os.path.join(os.getcwd(), self.drsf_source_docs_template_dir)) != True:
            raise AttributeError("The currently designated `drsf_source_docs_template_dir` directory does not exist.  This attribute's value must define a valid relative file path to a directory that serves as the template for building the DRSF's \"DEV\" directory.  Otherwise critical DRSF functions will fail.")
        else:
            return self.drsf_source_docs_template_dir

    @property.setter
    def drsf_source_docs_template_dir(self, input_dir):
        if input_dir == "":
            raise ValueError("The directory-file-path input to this function is an empty string.  This value must define a valid relative path to a directory containing the myst-markdown-formatted source documents that comprise the DRSF's entries and documentation book.  Otherwise critical DRSF functions will fail.")
        elif os.path.exists(os.path.join(os.getcwd(), self))
        pass

    @property
    def drsf_source_docs_dev_dir():
        pass

    @property.setter
    def drsf_source_docs_dev_dir():
        pass

    @property
    def drsf_source_docs_staging_dir():
        pass

    @property.setter
    def drsf_source_docs_staging_dir():
        pass

    @property
    def drsf_source_docs_build_dir():
        pass

    @property.setter
    def drsf_source_docs_build_dir():
        pass

