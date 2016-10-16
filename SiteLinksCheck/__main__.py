import sys

from Sitecheck import Sitecheck

z= Sitecheck(sys.argv[1])
print z.getalllinks()
print z.getinternallinks()
print z.getbrokeninternallinks()
print z.getallbrokenlinks()
