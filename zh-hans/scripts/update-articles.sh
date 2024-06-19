
DIR="articles"

cat SUMMARY.md | awk -F'/' '{if($3 != "" && substr($1, length($1)-7, 8) == "articles") print $1"/"$3; else print $0}' > SUMMARY-articles.md 
