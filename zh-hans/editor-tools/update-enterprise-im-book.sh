
git submodule update

DIR="enterprise-im-book"
cat $DIR/SUMMARY.md | awk -F'(' '{if($2 != "") print $1"(enterprise-im-book/"$2; else print $0}' > SUMMARY-EIM.md
