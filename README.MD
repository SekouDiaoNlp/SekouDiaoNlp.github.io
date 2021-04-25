    :::python
    pelican content -o output -s publishconf.py

    :::python
    cd output

    :::python
    python -m pelican.server

    :::python
    ghp-import -m "message" --no-jekyll -b master output

    :::python
    checkout master and push

    :::python
    checkout content and push