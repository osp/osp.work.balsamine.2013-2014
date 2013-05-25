#! /usr/bin/bash
curl http://osp.constantvzw.org:9001/p/balsa2014-css/export/txt > balsa2014.html && \
cat articles/*.html >> balsa2014.html

