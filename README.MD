    ``` python
    pelican content -o output -s publishconf.py

    ``` console
    cd output

    ``` python
    python -m pelican.server

    ``` console
    cd..

    ``` python
    ghp-import -m "message" --no-jekyll -b master output

    :::python
    checkout master and push

    ``` console
    checkout content and push
