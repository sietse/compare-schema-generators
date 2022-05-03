#!/bin/sh

# Clone and install xsdata
if ! { pip list | grep xsdata; }; then
    hg clone git+https://github.com/tefra/xsdata
    hg clone git+https://github.com/tefra/xsdata-pydantic
    pip install --user -e ./xsdata/[cli,lxml]
    pip install --user -e ./xsdata-pydantic/[cli]
fi

# ---- Generate the various options for generating classes
# NB: `--kw-only` and `--slots` require Python >= 3.10

# default
xsdata generate -p tryoptions_default .

# fancy with only safe hashes
xsdata generate --compound-fields --frozen -p tryoptions_safe_hashes .

# fancy with unsafe hashes
xsdata generate --compound-fields --frozen --unsafe-hash -p tryoptions_unsafe_hashes .

# Pydantic -- I have high hopes for this one
xsdata generate --output pydantic -p tryoptions_pydantic .


# ---- Compare the various ways of splitting into files
# Use the default generation options each time
for style in filenames namespaces clusters single-package namespace-clusters;
do
    xsdata generate --structure-style $style . --package trystructure_$style
done


