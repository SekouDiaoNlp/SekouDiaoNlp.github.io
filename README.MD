
# An easy step-by-step guide to build and publish GitHub Pages. 

        ```python
        pelican content -o output -s publishconf.py
        ```
    
    
        ```
        cd output
        ```
    
    
        ```python
        python -m pelican.server
        ```
    
    
        ```
        cd..
        ```
    
    
        ```python
        ghp-import -m "message" --no-jekyll -b master output
        ```
    
    
        ```
        checkout master and push
        ```
    
    
        ```
        checkout content and push
        ```
