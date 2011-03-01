# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Raindrop.
#
# The Initial Developer of the Original Code is
# Mozilla Messaging, Inc..
# Portions created by the Initial Developer are Copyright (C) 2009
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#

import cgi
import json
import urllib
from pylons import config, url

def shorten_link(long_url):
    longUrl = cgi.escape(long_url)
    bitly_userid= config.get('bitly.userid')
    bitly_key = config.get('bitly.key')
    bitly_result = urllib.urlopen("http://api.bit.ly/v3/shorten?login=%(bitly_userid)s&apiKey=%(bitly_key)s&longUrl=%(longUrl)s&format=json" % locals()).read()
    bitly_data = json.loads(bitly_result)['data']
    return bitly_data["url"]