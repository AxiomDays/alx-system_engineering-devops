#!/bin/bash
curl -s -I 0.0.0.0:5000 | grep -Fi Content-Length | awk '{print $2}'
