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
URL_A=r"http://"
URL_B=r"/push"
URL=r"http://10.17.220.10/push"
HEADERS={"Content-Type":"application/x-com-polycom-spipx", "User-Agent":"Voice DVT Automation"}
PAYLOAD_A=r"<PolycomIPPhone><Data priority=\"Critical\">"
PAYLOAD_B=r"</Data></PolycomIPPhone>"
PAYLOAD=r"<PolycomIPPhone><Data priority=\"Critical\">tel:\\5552112</Data></PolycomIPPhone>"
DATA=json.dumps(PAYLOAD)

"""
Keys for VVX400 and VVX500 series:

Line1	    Line21	Line41	        Softkey1	DoNotDisturb
Line2	    Line22	Line42	        Softkey2	Select
Line3	    Line23	Line43	        Softkey3	Conference
Line4	    Line24	Line44	        Softkey4	Transfer
Line5	    Line25	Line45	        Softkey5	Redial
Line6	    Line26	Line46	        VolDown	        Hold
Line7	    Line27	Line47	        VolUp	        Status
Line8	    Line28	Line48	        Headset	        Call List
Line9	    Line29	Dialpad0	Handsfree	 
Line10	    Line30	Dialpad1	MicMute	 
Line11	    Line31	Dialpad2	Menu	 
Line12	    Line32	Dialpad3	Messages	 
Line13	    Line33	Dialpad4	Applications	 
Line14	    Line34	Dialpad5	Directories	 
Line15	    Line35	Dialpad6	Setup	 
Line16	    Line36	Dialpad7	ArrowUp	 
Line17	    Line37	Dialpad8	ArrowDown	 
Line18	    Line38	Dialpad9	ArrowLeft	 
Line19	    Line39	DialPadStar	ArrowRight	 
Line20	    Line40	DialPadPound	Backspace
"""

#Define state machine transistions
"""
HOME (DEFAULT)
RINGING
INCOMING
ACTIVE
HOLD
ATTENDEDTRANSFER
BLINDTRANSFER
UNATTENDEDTRANSFER
DISCONNECT
"""

def go_home(ip):
  """
  Sets phone at IP back to home screen
  STATE==?=>HOME
  """
  pass

def isRinging(ip):
  """
  Returns True if phone has incoming call, else False
  STATE==?=>INCOMING
  """
  pass

def answer(ip):
  """
  IFF isRinging(ip): answers phone
  STATE==INCOMING=>ACTIVE
  """
  pass

def isActive(ip):
  """
  Returns True if phone has active call, else False
  STATE==?=>ACTIVE
  """
  pass

def transfer(ip, number):
  """
  IFF isActive(ip): transfer call
  From active call, performs attended transfer to number
  """
  pass

def unattendedTransfer(ip, number):
  """
  IFF isActive(ip): transfer call
  From active call, performs unattended transfer to number
  """
  pass

def blindTransfer(ip, number):
  """
  IFF isActive(ip): transfer call
  From active call, performs blind transfer to number
  """
  pass

def conference(ip, number):
  """
  IFF isActive(ip): conference with number
  From active call, conferences with number
  """
  pass

def disconnect(ip):
  """
  IFF isActive(ip): disconnect
  From active call, disconnect
  """
  pass

def main():
  r=requests.post(URL, auth=AUTH, verify=False, data=DATA, headers=HEADERS)

if __name__=="__main__":
  main()

