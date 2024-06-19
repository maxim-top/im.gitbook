
# 
URL_R0="https://docs.lanyingim.com"

cat SUMMARY.md | grep articles | awk -F'(' '{print substr($2,1,length($2)-1)}' > articles.list

cat articles.list| grep -v README | awk -v URL_R0=$URL_R0 -F'/' '{old=URL_R0"/"substr($0,1,length($0)-3)".html" ; new=URL_R0"/articles/"substr($3,1,length($3)-3)".html"; print old,new}' > urls-change.txt.2

cat SUMMARY.md| grep enterprise-im-book | grep .md | grep -v README | awk -F'(' '{print substr($2,1,length($2)-1)}' > articles.eim
cat articles.eim | grep -v README | awk -v URL_R0=$URL_R0 -F'/' '{old=URL_R0"/"substr($0,1,length($0)-3)".html" ; new=URL_R0"/articles/"substr($3,1,length($3)-3)".html"; print old,new}' > urls-change.txt.3

