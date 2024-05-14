#!/bin/bash
#  checks response body size
curl -s "$1" | wc -c
