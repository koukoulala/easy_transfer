import numpy as np
import re

def deal_dates(date_path,community_path):
    node_community=[]
    with open(date_path,'r')as f:
        for lines in f.readlines():
            line=lines.strip("\n\r").split("\t")
            year=re.split(r'[-]',line[1])[0]
            if year=='1992':
                node_community.append((int(line[0]),0))
            if year=='1993':
                node_community.append((int(line[0]),1))
            if year == '1994':
                node_community.append((int(line[0]),2))
            if year=='1995':
                node_community.append((int(line[0]),3))
            if year=='1996':
                node_community.append((int(line[0]),4))
            if year=='1997':
                node_community.append((int(line[0]),5))
            if year=='1998':
                node_community.append((int(line[0]),6))
            if year=='1999':
                node_community.append((int(line[0]),7))
            if year=='2000':
                node_community.append((int(line[0]),8))
            if year=='2001':
                node_community.append((int(line[0]),9))
            if year=='2002':
                node_community.append((int(line[0]),10))

    np.savetxt(community_path,node_community,fmt='%d',delimiter=" ")


if __name__=="__main__":
    deal_dates("/Users/didi/Desktop/store/data/cit-HepPh/cit-HepPh-dates.txt",
               "/Users/didi/Desktop/store/data/cit-HepPh/cit-HepPh_communities.txt")
