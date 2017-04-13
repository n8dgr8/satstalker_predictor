#!/usr/bin/env bash

pushd ~/.virtualenvs/satstalker_predictor/lib/python2.7/site-packages
zip -ur ~/src/satstalker_predictor/satstalker_predictor.zip .

popd
zip -u satstalker_predictor.zip satstalker_predictor.py awesome_satellites.json
