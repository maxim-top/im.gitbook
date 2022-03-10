release:
	docker run -it -v `pwd`:/gitbook registry.cn-beijing.aliyuncs.com/maxim-resource/gitbook gitbook build
	docker run -it -w /gitbook -v `pwd`:/gitbook erlang:21  escript scripts/subdirectory_summary.escript
	mv _book/zh-hans/* _book/
