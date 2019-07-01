# Student Support (Scraping Amazon)

## Setup

```sh
conda create -n soup-env python=3.7
conda activate soup-env
```

```sh
pip install -r requirements.txt
```


## Notes

After searching for a product, the container is:

```html
<div class="s-result-list s-search-results sg-row">
```

And each item is nested under this, resembling:

```html
<div data-asin="B005YR0F40" data-index="2" class="sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item sg-col-4-of-28 sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32" data-cel-widget="search_result_2">

```
