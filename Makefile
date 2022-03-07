build:
	docker run -it -v `pwd`:/gitbook -p 4000:4000 registry.cn-beijing.aliyuncs.com/maxim-resource/gitbook gitbook build && mv _book/zh-hans/* _book/
serve:
	docker run -it -v `pwd`:/gitbook -p 4000:4000 registry.cn-beijing.aliyuncs.com/maxim-resource/gitbook gitbook serve
move:
	mv _book/zh-hans/* _book/
