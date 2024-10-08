serve:
	gitbook serve --log=debug --debug --no-live
refine:
	docker run -t -w /gitbook -v `pwd`:/gitbook erlang:21  escript scripts/subdirectory_summary.escript
	docker run -t -w /gitbook -v `pwd`:/gitbook erlang:21  escript scripts/gitbook_text_replace.escript
	mv _book/sitemap.xml _book/zh-hans/
	rm -rf _book/scripts
	mv _book/zh-hans/* _book/
