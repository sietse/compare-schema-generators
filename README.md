## Compare schema generators

Folders to click around in.
                                                                                                                                     |
| folder                          | command                                                                                          |
| ------                          | -------                                                                                          |
| tryoptions_default              | xsdata generate -p tryoptions_default .                                                          |
| tryoptions_safe_hashes          | xsdata generate --compound-fields --frozen -p tryoptions_safe_hashes .                           |
| tryoptions_unsafe_hashes        | xsdata generate --compound-fields --frozen --unsafe-hash -p tryoptions_unsafe_hashes .           |
| tryoptions_pydantic             | xsdata generate --output pydantic -p tryoptions_pydantic .                                       |
| trystructure_filenames          | xsdata generate --structure-style filenames . --package trystructure_filenames                   |
| trystructure_namespaces         | xsdata generate --structure-style namespaces . --package trystructure_namespaces                 |
| trystructure_clusters           | xsdata generate --structure-style clusters . --package trystructure_clusters                     |
| trystructure_single-package     | xsdata generate --structure-style single-package . --package trystructure_single-package         |
| trystructure_namespace-clusters | xsdata generate --structure-style namespace-clusters . --package trystructure_namespace-clusters |
