# psc-cfp-visualizations

Recreating the Public Service Commission of Canada (PSC)'s Time to Staff (TTS)D3.js graphic in Plotly. To access PSC's Time to Staff (TTS) [data](/https://www5.psc-cfp.gc.ca/dsad-dsda/time-to-staff/index-en.html) go to 'Select a department or an agency' and download each 'Time Period'.

### Components
- Website framework in [Flask](/https://flask.palletsprojects.com/en/2.3.x/) using HTML and CSS 
- Python graphing library [Plotly](/https://plotly.com/python/)

<br />
<img src="docs\psc-plotly-figure.PNG" alt="drawing" width="400" />

## Installation

```bash
pip install -r requirements.txt
```

## Comparison

Attribute | PSC |  Repository
:-------------------------:|:-------------------------:|:-------------------------:
Figure | <img src="docs\psc-javascript-figure.PNG" alt="drawing" width="400"/> | <img src="docs\psc-plotly-figure.PNG" alt="drawing" width="400"/>
Language | Javascript | Python
Libary | D3 | Plotly
Lines of Code | <1600 | <200
Histogram | overlayed median legend | overlayed median legend; built-in: hover-over values, png download, zoom/pan/etc.
Table | dynamic: dropdown, filter, sort ; text hyper-linked | static: basic scroll


## Review
Plotly is able to recreate the figure in fewer lines of code but lacks dynamic features that make the D3.js implementation more user-friendly. For example, while plotly's 'updatemenus' allows the user to filter the TTS data used in the histogram and tables dynamically (in a single div), the D3.js's separation of these charts enables the page to hide table rows in a dropdown. In addition,plotly lacks a text feature in ['update_layout'](/https://plotly.com/python/reference/layout/updatemenus/) (used to display 'Time Period') required annotations, anchored in different x/y axes, make webpage resizing clunky. Overall, for serving single dynamic charts or multiple static charts Plotly is great, but for dynamically linked charts D3.js seems to be better.


