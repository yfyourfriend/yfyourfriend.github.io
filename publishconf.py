#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
# IMPORTANT. pelicanconf import should come after path.append
from pelicanconf import *

if os.environ.get("CONTEXT") == "production":
    SITEURL = "https://yfyourfriend.github.io"
    FEED_DOMAIN = SITEURL
    FEED_ALL_ATOM = "feeds/all.atom.xml"
    CLAIM_BING = os.environ.get("CLAIM_BING_PROD")
    CLAIM_GOOGLE = os.environ.get("CLAIM_GOOGLE_PROD")
    STAT_COUNTER_PROJECT = os.environ.get("STAT_COUNTER_PROJECT_PROD")
    STAT_COUNTER_SECURITY = os.environ.get("STAT_COUNTER_SECURITY_PROD")
    GOOGLE_ANALYTICS = os.environ.get("GOOGLE_ANALYTICS_PROD")
else:
    SITEURL = "https://yfyourfriend.github.io"

MAILCHIMP_FORM_ACTION = os.environ.get("MAILCHIMP_FORM_ACTION")

RELATIVE_URLS = False

PLUGINS.append("filetime_from_git")
PLUGINS.append("sitemap")

DELETE_OUTPUT_DIRECTORY = True
