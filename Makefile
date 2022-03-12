release: build refine

install:
	docker run -it -v `pwd`:/gitbook registry.cn-beijing.aliyuncs.com/maxim-resource/gitbook gitbook install
build:
	docker run -it -v `pwd`:/gitbook registry.cn-beijing.aliyuncs.com/maxim-resource/gitbook gitbook build

refine:
	docker run -it -w /gitbook -v `pwd`:/gitbook erlang:21  escript scripts/subdirectory_summary.escript
	docker run -it -w /gitbook -v `pwd`:/gitbook erlang:21  escript scripts/gitbook_text_replace.escript
	mv _book/zh-hans/* _book/
	cp _book/assets/favicon.ico _book/gitbook/images/favicon.ico
