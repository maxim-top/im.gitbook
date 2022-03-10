build:
	docker run -it -v `pwd`:/gitbook  registry.cn-beijing.aliyuncs.com/maxim-resource/gitbook gitbook build

serve:
	docker run -it -v `pwd`:/gitbook -p 4000:4000 registry.cn-beijing.aliyuncs.com/maxim-resource/gitbook gitbook serve

release: build
	escript scripts/subdirectory_summary.escript
	mv _book/zh-hans/* _book/
