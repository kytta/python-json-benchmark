# python-json-benchmark

> Benchmarks of Python's builtin `json` vs. `simplejson`

## Running

```sh
pip install -r requirements.txt
python3 bench.py
```

## Results

Benchmarks done on Macbook Pro 2016 (Intel Core i7, 2.7 GHz) on Python 3.10.0

```txt
Benchmarking: '{"glossary": {"title": "example ...'
      json.dumps: 0.852s / 0.876s / 0.901s
simplejson.dumps: 1.495s / 1.519s / 1.533s
      json.loads: 0.592s / 0.596s / 0.602s
simplejson.loads: 0.641s / 0.646s / 0.652s

Benchmarking: '{"menu": {"id": "file", "value":...'
      json.dumps: 0.657s / 0.676s / 0.689s
simplejson.dumps: 1.258s / 1.286s / 1.304s
      json.loads: 0.453s / 0.473s / 0.517s
simplejson.loads: 0.525s / 0.541s / 0.555s

Benchmarking: '{"widget": {"debug": "on", "wind...'
      json.dumps: 1.002s / 1.160s / 1.414s
simplejson.dumps: 1.555s / 1.702s / 1.855s
      json.loads: 0.815s / 0.829s / 0.847s
simplejson.loads: 0.997s / 1.140s / 1.472s

Benchmarking: '{"web-app": {"servlet": [{"servl...'
      json.dumps: 3.508s / 3.751s / 4.088s
simplejson.dumps: 4.858s / 5.287s / 5.990s
      json.loads: 2.535s / 2.699s / 3.156s
simplejson.loads: 3.074s / 3.155s / 3.321s

Benchmarking: '{"menu": {"header": "SVG Viewer"...'
      json.dumps: 1.828s / 1.897s / 1.939s
simplejson.dumps: 3.299s / 3.485s / 3.886s
      json.loads: 1.041s / 1.065s / 1.110s
simplejson.loads: 1.101s / 1.140s / 1.176s
```

As you can see, using `simplejson` with modern Python versions is unnecessary.

## Licence

Dedicated to public domain via
 [CC0](https://creativecommons.org/publicdomain/zero/1.0/).
