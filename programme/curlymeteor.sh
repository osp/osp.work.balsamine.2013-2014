#! /usr/bin/bash
curl http://osp.constantvzw.org:9001/p/balsa2014-css/export/txt > meteor.html && \
cat meteor/*.html >> meteor.html
