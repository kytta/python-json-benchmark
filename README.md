# python-json-benchmark

> Benchmarks of Python's builtin `json` vs. `simplejson`

## Running

```sh
pip install -r requirements.txt
python3 bench.py
```

## Results

Benchmarks done on Macbook Pro (14", 2021, M1 Pro, 16 GB RAM) on Python 3.11.1

```txt
Benchmarking: '{"glossary": {"title": "example ...'
      json.dumps: 0.336s / 0.345s / 0.368s
simplejson.dumps: 0.612s / 0.614s / 0.617s
      json.loads: 0.226s / 0.227s / 0.227s
simplejson.loads: 0.247s / 0.249s / 0.250s

Benchmarking: '{"menu": {"id": "file", "value":...'
      json.dumps: 0.262s / 0.263s / 0.263s
simplejson.dumps: 0.522s / 0.522s / 0.524s
      json.loads: 0.180s / 0.181s / 0.182s
simplejson.loads: 0.195s / 0.195s / 0.195s

Benchmarking: '{"widget": {"debug": "on", "wind...'
      json.dumps: 0.386s / 0.387s / 0.388s
simplejson.dumps: 0.604s / 0.605s / 0.607s
      json.loads: 0.309s / 0.309s / 0.310s
simplejson.loads: 0.358s / 0.358s / 0.359s

Benchmarking: '{"web-app": {"servlet": [{"servl...'
      json.dumps: 1.492s / 1.502s / 1.511s
simplejson.dumps: 1.998s / 2.013s / 2.042s
      json.loads: 1.063s / 1.067s / 1.071s
simplejson.loads: 1.188s / 1.196s / 1.201s

Benchmarking: '{"menu": {"header": "SVG Viewer"...'
      json.dumps: 0.754s / 0.758s / 0.765s
simplejson.dumps: 1.402s / 1.404s / 1.410s
      json.loads: 0.434s / 0.435s / 0.438s
simplejson.loads: 0.458s / 0.462s / 0.464s
```

As you can see, there is no need to use `simplejson` with modern Python versions, as it is way slower.

## Licence

Dedicated to public domain via
 [CC0](https://creativecommons.org/publicdomain/zero/1.0/).
