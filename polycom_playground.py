#!/usr/bin/env python
###############################################################################
# This program is free software; you can redistribute it and/or modify it 
# under the terms of the GNU public license as published by the Free Software
# Foundation.
# 
# This program is distributed in the hopes that it will be useful but without 
# any warranty, even implied, of merchantability or fitness for a particular
# purpose.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Author Jeffrey McAnarney from U.S. 7/26/2013
# 
#
#  Beautiful is better than ugly
#  Explicit is better than implicit
#  Simple is better than complex
#  Complex is better than complicated
#  Readability counts
#
###############################################################################
import requests
import json
from requests.auth import HTTPDigestAuth as digest



#Set globals
USER='Push'
PWD='Push'
AUTH=digest(USER, PWD)
URL=r"http://10.17.220.218/push"
HEADERS={"Content-Type":"application/x-com-polycom-spipx"}
PAYLOAD=r"<PolycomIPPhone><Data priority=\"Critical\">tel:\\5552112</Data></PolycomIPPhone>"
DATA=json.dumps(PAYLOAD)


def main():
  #r=requests.post(URL, auth=AUTH, verify=False, data=DATA, headers=HEADERS)
  r=requests.get("http://10.17.220.218/polling/callstateHandler", auth=AUTH)
  print r
  print r.text

if __name__=="__main__":
  main()

